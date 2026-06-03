from pathlib import Path

from idpflow_core.models import DocInput, DocType
from idpflow_core.package import build_package
from idpflow_core.render import render_package


def test_build_package_stub():
    docs = [
        DocInput(file_path="x.pdf", doc_type="paystub"),
        DocInput(file_path="y.pdf", doc_type="w2"),
    ]
    pkg = build_package("PKG", docs, profile="mortgage")
    assert pkg.package_id == "PKG"
    assert len(pkg.ordered_stack) == 2
    assert pkg.key_fields
    assert all(k.source_doc in (DocType.PAYSTUB, DocType.W2) for k in pkg.key_fields)


def test_review_queue_flags_ungrounded():
    # The stub bank_statement includes an ungrounded account.holder.
    pkg = build_package("PKG2", [DocInput(file_path="b.pdf", doc_type="bank_statement")])
    assert len(pkg.review_queue) >= 1
    assert all(k.needs_review for k in pkg.review_queue)


def test_no_decision_surface():
    pkg = build_package("PKG3", [DocInput(file_path="x.pdf", doc_type="paystub")])
    # The package model carries no decision field; it only surfaces data.
    assert not hasattr(pkg, "decision")


def test_render_creates_pdf_and_json(tmp_path: Path):
    pkg = build_package("PKG4", [DocInput(file_path="x.pdf", doc_type="paystub")])
    r = render_package(pkg, output_dir=str(tmp_path))
    assert Path(r.pdf_path).exists()
    assert Path(r.json_path).exists()
    assert r.page_count >= 1

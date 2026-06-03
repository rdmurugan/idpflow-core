from idpflow_core.classify import classify_document
from idpflow_core.models import DocType


def test_explicit_hint_wins():
    r = classify_document("anything.pdf", hint="w2")
    assert r.doc_type == DocType.W2
    assert r.method == "hint"


def test_filename_heuristic_offline():
    # No API key in CI => not live => filename fallback.
    assert classify_document("/x/W2_2025.pdf").doc_type == DocType.W2
    assert classify_document("/x/paystub_jan.pdf").doc_type == DocType.PAYSTUB
    assert classify_document("/x/1003_application.pdf").doc_type == DocType.URLA_1003


def test_unknown_filename_is_other():
    assert classify_document("/x/random_file.pdf").doc_type == DocType.OTHER

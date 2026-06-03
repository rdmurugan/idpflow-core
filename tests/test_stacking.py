from idpflow_core import stacking as S
from idpflow_core.models import DocType


def test_profiles_exist():
    assert "mortgage" in S.profiles()
    assert "auto_indirect" in S.profiles()


def test_stack_orders_by_profile():
    # Scrambled input; mortgage profile puts the 1003 first.
    present = [(DocType.BANK_STATEMENT, "b.pdf"), (DocType.URLA_1003, "a.pdf")]
    res = S.stack_documents(present, profile="mortgage")
    assert res.ordered_stack[0].doc_type == DocType.URLA_1003
    assert [it.position for it in res.ordered_stack] == [1, 2]


def test_missing_required_flagged():
    res = S.stack_documents([(DocType.URLA_1003, "a.pdf")], profile="mortgage")
    assert res.is_complete is False
    assert any(m.doc_type == DocType.PAYSTUB for m in res.missing_docs)


def test_custom_order_overrides_profile():
    present = [(DocType.W2, "w.pdf"), (DocType.PAYSTUB, "p.pdf")]
    res = S.stack_documents(
        present, profile="mortgage", custom_order=[DocType.W2, DocType.PAYSTUB]
    )
    assert res.ordered_stack[0].doc_type == DocType.W2


def test_extra_doc_appended_out_of_profile():
    present = [(DocType.OTHER, "x.pdf"), (DocType.URLA_1003, "a.pdf")]
    res = S.stack_documents(present, profile="mortgage")
    # OTHER is not in the mortgage profile, so it is appended at the end.
    assert res.ordered_stack[-1].doc_type == DocType.OTHER
    assert res.ordered_stack[-1].in_profile is False

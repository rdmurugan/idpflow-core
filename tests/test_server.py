import asyncio


def test_all_tools_registered():
    from idpflow_core.server import mcp

    tools = asyncio.run(mcp.list_tools())
    names = {t.name for t in tools}
    expected = {
        "extract_document",
        "classify_document_tool",
        "stack_documents",
        "process_documents",
        "render_document_package",
    }
    assert expected <= names


def test_unauthenticated_by_default_in_stub():
    # With no OAuth env configured, the server runs unauthenticated (local dev).
    from idpflow_core.server import _token_verifier

    assert _token_verifier is None

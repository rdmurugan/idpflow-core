# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project aims to follow
[Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-05-30

### Added
- MCP server with five tools: `extract_document`, `classify_document`, `stack_documents`,
  `process_documents`, `render_document_package`.
- LandingAI ADE wrapper (parse then extract) with grounding mapped to page, bounding box, and
  confidence; ungrounded values flagged for review.
- Document-source-agnostic ingestion and configurable stacking profiles (mortgage, auto_indirect,
  auto_direct) plus `custom_order`.
- Review-package rendering: combined PDF (cover + source docs in stack order) plus JSON sidecar.
- OAuth 2.1 resource-server auth for remote (streamable-HTTP) transport; fails closed.
- Dockerfile, Databricks batch job, and integration guides for Claude, Lyzr, LangGraph, CrewAI.
- Stub mode (no API key) that runs the full pipeline on synthetic data.
- Test suite, CI (lint + tests + build), secret-guard pre-commit hook, and a product landing page.

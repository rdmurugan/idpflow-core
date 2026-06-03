# Security Policy

## Reporting a vulnerability

Please report security issues privately through
[GitHub Security Advisories](https://github.com/rdmurugan/idpflow-core/security/advisories/new),
or by opening an issue that does not include exploit details. We aim to acknowledge within a few days.

## Secrets

Never commit API keys. `.env` is gitignored, and a pre-commit secret-guard hook
(`.githooks/pre-commit`) blocks staged `.env` files and key-looking values. Enable it per clone:

```bash
git config core.hooksPath .githooks
```

## Data handling

Live extraction sends documents to LandingAI ADE, a third-party API. Stub mode (no API key) is
fully local. If you process regulated data, treat ADE as a sub-processor in your data agreements,
and use a LandingAI on-prem / VPC deployment where documents must not leave your network.

## Authentication

The remote (streamable-HTTP) server requires OAuth 2.1 and refuses to start unauthenticated unless
`MCP_ALLOW_INSECURE=1` is explicitly set behind your own trusted gateway.

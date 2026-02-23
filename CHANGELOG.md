# Changelog

Todas as mudanças relevantes deste projeto serão registradas aqui.

O formato é inspirado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e segue versionamento semântico quando aplicável.

## [Unreleased]

### Added
- `CONTRIBUTING.md` com guia de contribuição e guardrails do repositório.
- `CHANGELOG.md` na raiz para histórico de mudanças.

## [0.1.0] - 2026-02-23

### Added
- CLI inicial para busca de sinopse de filmes via OMDb (`filmes.py`).
- `README.md` com instruções de uso e configuração.
- `requirements.txt` e `.env.example`.

### CI/CD e Automação
- Workflow de CI para lint/test/smoke test/security audit.
- Dependabot configurado para dependências Python (weekly, limite 5 PRs).
- Workflow de release automática por tags `v*.*.*`.

### Qualidade e Colaboração
- Templates de PR e Issues (bug report + feature request).
- `Makefile` com alvos `install`, `lint`, `test`, `fmt`.
- Configuração mínima de `ruff` e `pytest`.
- Teste mínimo em `tests/test_filmes.py`.

### Docs
- Badge de CI no `README.md`.

---

[Unreleased]: https://github.com/pdonizete/sinopse-filmes/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/pdonizete/sinopse-filmes/releases/tag/v0.1.0

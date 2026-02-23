# Contributing Guide

Obrigado por contribuir com o **sinopse-filmes** 🎬

## Princípios deste repositório

- Não altere a lógica/funcionalidade do app CLI sem alinhamento prévio.
- Mudanças de infra/automação/qualidade são bem-vindas.
- Não adicionar empacotamento (`pyproject.toml`, scripts de build, etc.) se isso não existir no projeto.

## Fluxo recomendado

1. Crie uma branch para sua alteração.
2. Faça mudanças pequenas e com commits claros.
3. Rode os comandos locais equivalentes ao CI.
4. Abra PR usando o template do repositório.

## Setup local

```bash
make install
```

## Checklist local (antes de commit/PR)

```bash
make lint
make test
```

Opcional (formatação):

```bash
make fmt
```

## Convenção de commits (sugestão)

- `chore:` manutenção/infra
- `ci:` pipeline/workflows
- `docs:` documentação
- `test:` testes

## Pull Request

Ao abrir PR, descreva:

- O que mudou e por quê
- Como testar
- Impactos (se houver)

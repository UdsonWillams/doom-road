# AGENTS.md — Doom Road

## Comandos

- **Instalar deps / sync do ambiente**: `uv sync`
- **Rodar o jogo**: `uv run doom-road`
- **Rodar os testes**: `uv run pytest`
- **Lint**: `uv run ruff check .`
- **Formatar**: `uv run ruff format .`
- **Checar formatação (CI)**: `uv run ruff format --check .`
- **Pre-commit (todos os hooks)**: `pre-commit run --all-files`

## Stack

- Python >= 3.10
- [pygame-ce](https://github.com/pygame-community/pygame-ce) (fork comunitária do pygame; `import pygame` funciona igual).
- Empacotamento: `hatchling`. Ambiente gerenciado por `uv`.

## Estrutura

```
doom_road/        # pacote do jogo
  main.py         # entry point (main())
  game.py         # loop principal, telas, estado
  spawner.py      # agendamento de inimigos anti-agrupamento
  entities/       # Player, Enemy
  utils/          # constants, resource_loader
tests/            # pytest
assets/{images,sounds}/
```

## Convenções de código

- Sem `from x import *` — sempre imports explícitos.
- Type hints em todas as assinaturas públicas.
- Movimento baseado em `dt` (segundos), nunca por frame fixo.
- Constantes de ajuste de jogo ficam em `doom_road/utils/constants.py`.

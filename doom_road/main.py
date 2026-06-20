"""Entry point do Doom Road."""

from doom_road.game import Game


def main() -> None:
    """Inicia o jogo."""
    Game().run()


if __name__ == "__main__":
    main()

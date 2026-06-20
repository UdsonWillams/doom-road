"""Setup do pytest: inicializa o pygame em modo headless."""

import os

import pygame

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")


def pytest_configure(config) -> None:
    pygame.init()
    pygame.display.set_mode((1, 1))


def pytest_unconfigure(config) -> None:
    pygame.quit()

"""Carro do jogador."""

from __future__ import annotations

from collections.abc import Sequence

import pygame

from doom_road.utils.constants import (
    CAR_SIZE,
    PLAYER_CLAMP_VERTICAL,
    PLAYER_MAX_X,
    PLAYER_MIN_X,
    PLAYER_SPEED,
    PLAYER_START_X,
    PLAYER_START_Y,
    SCREEN_HEIGHT,
)
from doom_road.utils.resource_loader import load_image


class Player(pygame.sprite.Sprite):
    """Carro controlado pelo jogador (WASD)."""

    def __init__(self) -> None:
        super().__init__()
        self.image = load_image("carro.png", size=CAR_SIZE)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._x = 0.0
        self._y = 0.0
        self.reset()

    def reset(self) -> None:
        """Volta para a posição inicial."""
        self.rect.topleft = (PLAYER_START_X, PLAYER_START_Y)
        self._x = float(self.rect.x)
        self._y = float(self.rect.y)

    def update(self, keys: Sequence[int], dt: float) -> None:
        """Move o carro conforme as teclas, em px/seg independente do FPS."""
        dx = 0.0
        dy = 0.0
        if keys[pygame.K_w]:
            dy -= PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            dy += PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            dx += PLAYER_SPEED * dt
        if keys[pygame.K_a]:
            dx -= PLAYER_SPEED * dt

        self._x += dx
        self._y += dy

        # limites horizontais (canto esquerdo do carro)
        if self._x < PLAYER_MIN_X:
            self._x = PLAYER_MIN_X
        elif self._x > PLAYER_MAX_X:
            self._x = PLAYER_MAX_X

        if PLAYER_CLAMP_VERTICAL:
            if self._y < 0:
                self._y = 0
            elif self._y + self.rect.height > SCREEN_HEIGHT:
                self._y = SCREEN_HEIGHT - self.rect.height

        self.rect.x = int(self._x)
        self.rect.y = int(self._y)

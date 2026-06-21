"""Carro inimigo que desce a tela com reciclagem por faixa.

Três carros fixos — um por faixa. Cada um recicla ao sair da tela
com um Y aleatório dentro do range da sua faixa (criando stagger
imprevisível) e nova velocidade com boost de dificuldade.
"""

from __future__ import annotations

import random

import pygame

from doom_road.utils.constants import (
    CAR_SIZE,
    DIFFICULTY_MAX_SPEED,
    ENEMY_MIN_SPEED,
    ENEMY_SPEED_RANGE,
    ENEMY_Y_RANGES,
)
from doom_road.utils.resource_loader import load_image

_ENEMY_SPRITES = ("carro1.png", "carro2.png", "carro3.png")


class Enemy(pygame.sprite.Sprite):
    """Carro inimigo fixo — recicla sozinho ao sair da tela."""

    def __init__(self, lane_x: int, lane_index: int) -> None:
        super().__init__()
        self.lane_x = lane_x
        self.lane_index = lane_index

        self.image = load_image(random.choice(_ENEMY_SPRITES), size=CAR_SIZE)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = lane_x
        self._y = float(self.rect.y)

        base = random.uniform(*ENEMY_SPEED_RANGE)
        self.speed = max(base, ENEMY_MIN_SPEED)

    def update(self, dt: float) -> None:
        """Desce pela tela. Devolve nada — Game cuida da reciclagem."""
        self._y += self.speed * dt
        self.rect.y = int(self._y)

    def recycle(self, speed_boost: float) -> None:
        """Reposiciona no range de Y da faixa com nova velocidade."""
        lo, hi = ENEMY_Y_RANGES[self.lane_index]
        self.rect.y = random.randint(lo, hi)
        self._y = float(self.rect.y)

        base = random.uniform(*ENEMY_SPEED_RANGE)
        self.speed = min(base + speed_boost, DIFFICULTY_MAX_SPEED)
        self.speed = max(self.speed, ENEMY_MIN_SPEED)

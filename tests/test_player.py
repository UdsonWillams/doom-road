"""Testes do Player."""

import pygame

from doom_road.entities.player import Player
from doom_road.utils.constants import (
    PLAYER_MAX_X,
    PLAYER_MIN_X,
    PLAYER_SPEED,
    PLAYER_START_X,
    PLAYER_START_Y,
    SCREEN_HEIGHT,
)


def _no_keys() -> list[int]:
    keys = [0] * 512
    return keys


def _keys(*codes: int) -> list[int]:
    keys = _no_keys()
    for c in codes:
        keys[c] = 1
    return keys


def test_reset_position() -> None:
    p = Player()
    assert p.rect.topleft == (PLAYER_START_X, PLAYER_START_Y)


def test_moves_up_with_dt() -> None:
    p = Player()
    y0 = p.rect.y
    p.update(_keys(pygame.K_w), 0.5)
    assert p.rect.y == y0 - int(PLAYER_SPEED * 0.5)


def test_moves_right_with_dt() -> None:
    p = Player()
    x0 = p.rect.x
    p.update(_keys(pygame.K_d), 0.5)
    assert p.rect.x == x0 + int(PLAYER_SPEED * 0.5)


def test_horizontal_clamp_max() -> None:
    p = Player()
    # leva até o limite direito em vários passos
    for _ in range(200):
        p.update(_keys(pygame.K_d), 0.1)
    assert p.rect.x <= PLAYER_MAX_X


def test_horizontal_clamp_min() -> None:
    p = Player()
    for _ in range(200):
        p.update(_keys(pygame.K_a), 0.1)
    assert p.rect.x >= PLAYER_MIN_X


def test_vertical_clamp() -> None:
    p = Player()
    for _ in range(200):
        p.update(_keys(pygame.K_w), 0.1)
    assert p.rect.top >= 0
    for _ in range(400):
        p.update(_keys(pygame.K_s), 0.1)
    assert p.rect.bottom <= SCREEN_HEIGHT


def test_no_movement_without_keys() -> None:
    p = Player()
    x0, y0 = p.rect.x, p.rect.y
    p.update(_no_keys(), 0.5)
    assert (p.rect.x, p.rect.y) == (x0, y0)

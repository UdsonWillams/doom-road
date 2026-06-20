"""Testes do Enemy (reciclagem por faixa)."""

from doom_road.entities.enemy import Enemy
from doom_road.utils.constants import (
    DIFFICULTY_MAX_SPEED,
    ENEMY_LANES,
    ENEMY_SPEED_RANGE,
    ENEMY_Y_RANGES,
    SCREEN_HEIGHT,
)


def test_lane_assignment() -> None:
    e = Enemy(ENEMY_LANES[1], 1)
    assert e.rect.x == ENEMY_LANES[1]
    assert e.lane_index == 1


def test_moves_down_with_dt() -> None:
    e = Enemy(ENEMY_LANES[0], 0)
    e.speed = 300.0
    y0 = e.rect.y
    e.update(0.5)
    assert e.rect.y == y0 + int(300.0 * 0.5)


def test_recycle_changes_position_to_faixa_range() -> None:
    e = Enemy(ENEMY_LANES[0], 0)
    e.recycle(0.0)
    lo, hi = ENEMY_Y_RANGES[0]
    assert lo <= e.rect.y <= hi
    assert ENEMY_SPEED_RANGE[0] <= e.speed <= ENEMY_SPEED_RANGE[1]


def test_recycle_speed_capped() -> None:
    e = Enemy(ENEMY_LANES[0], 0)
    e.recycle(10_000.0)
    assert e.speed <= DIFFICULTY_MAX_SPEED


def test_stays_alive_after_offscreen() -> None:
    """Inimigo não se autodestrói; Game que decide reciclar."""
    e = Enemy(ENEMY_LANES[0], 0)
    e.rect.y = SCREEN_HEIGHT + 100
    e._y = float(e.rect.y)
    e.update(0.016)
    # ainda tem rect válido (não chamou kill)
    assert e.rect.y > SCREEN_HEIGHT
    assert e.lane_x == ENEMY_LANES[0]


def test_faixa1_spawns_further_than_faixa0() -> None:
    """Lane 1 (meio) range é mais negativo (mais acima) que lane 0."""
    lo0, hi0 = ENEMY_Y_RANGES[0]
    lo1, hi1 = ENEMY_Y_RANGES[1]
    assert hi1 < lo0  # lane 1 respawna sempre mais longe

"""Testes de integração da Game (colisão, win, game over, telas)."""

import pygame

from doom_road.game import Game
from doom_road.utils.constants import (
    END_SCREEN_TIME,
    INITIAL_LIVES,
    START_SCREEN_TIME,
    WIN_TIME,
)


def _make_game() -> Game:
    return Game()


def test_initial_state_is_start() -> None:
    g = _make_game()
    assert g.state == "start"
    assert g.screen_timer == START_SCREEN_TIME
    assert g.lives == INITIAL_LIVES
    assert len(g.enemy_list) == 3
    assert len(g.enemies) == 3


def test_start_screen_transitions_after_timer() -> None:
    g = _make_game()
    g._update(START_SCREEN_TIME + 0.01)
    assert g.state == "playing"


def test_start_screen_skippable_by_key() -> None:
    g = _make_game()
    g.state = "start"
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
    g._events()
    assert g.state == "playing"


def test_collision_reduces_life_and_resets_round() -> None:
    g = _make_game()
    g.state = "playing"
    # posiciona o primeiro inimigo sobre o player
    e = g.enemy_list[0]
    e.rect.center = g.player.rect.center
    e._y = float(e.rect.y)
    lives_before = g.lives
    g._update(1 / 60)
    assert g.lives == lives_before - 1
    assert g.state == "playing"


def test_game_over_when_lives_reach_zero() -> None:
    g = _make_game()
    g.state = "playing"
    g.lives = 1
    e = g.enemy_list[0]
    e.rect.center = g.player.rect.center
    e._y = float(e.rect.y)
    g._update(1 / 60)
    assert g.lives == 0
    assert g.state == "gameover"
    assert g.screen_timer == END_SCREEN_TIME


def test_win_when_time_reaches_goal() -> None:
    g = _make_game()
    g.state = "playing"
    g.time_seconds = WIN_TIME - 0.01
    g._update(0.02)
    assert g.state == "win"
    assert g.screen_timer == END_SCREEN_TIME


def test_end_screen_exits_after_timer() -> None:
    g = _make_game()
    g.state = "win"
    g.screen_timer = END_SCREEN_TIME
    g._update(END_SCREEN_TIME + 0.01)
    assert g.running is False


def test_enemies_recycle_off_screen() -> None:
    """Inimigo que sai da tela é reciclado para o range da faixa."""
    g = _make_game()
    g.state = "playing"
    e = g.enemy_list[0]
    # força o inimigo a sair da tela
    e.rect.y = 700
    e._y = 700.0
    g._update(1 / 60)
    # deve ter sido reciclado (y < 0)
    assert e.rect.y < 0

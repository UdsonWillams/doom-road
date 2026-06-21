"""Loop principal, telas e estado do Doom Road."""

from __future__ import annotations

import contextlib
import random

import pygame

from doom_road.entities.enemy import Enemy
from doom_road.entities.player import Player
from doom_road.utils.constants import (
    DIFFICULTY_INTERVAL_S,
    DIFFICULTY_MAX_SPEED,
    DIFFICULTY_RAMP,
    END_SCREEN_TIME,
    ENEMY_INITIAL_Y,
    ENEMY_LANES,
    ENEMY_SPEED_RANGE,
    FPS,
    INITIAL_LIVES,
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    START_SCREEN_TIME,
    WHITE,
    WIN_TIME,
)
from doom_road.utils.resource_loader import (
    load_image,
    load_sound,
    play_music,
    stop_music,
)


class Game:
    """Orquestra o jogo: telas, loop, colisão e pontuação."""

    def __init__(self) -> None:
        pygame.init()
        with contextlib.suppress(pygame.error):
            pygame.mixer.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Doom Road")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial black", 20)

        self.bg_image = load_image("tela.png")
        self.start_image = load_image("inicio.png")
        self.gameover_image = load_image("gameover.png")
        self.win_image = load_image("vencedor.png")
        self.crash_sound = load_sound("batida.mp3")
        self.applause_sound = load_sound("apalusos.mp3")

        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.enemy_list: list[Enemy] = []

        self.running = True
        self._reset_match()

    # --- estado ---------------------------------------------------------

    def _reset_match(self) -> None:
        """Reinicia uma partida completa (tela de início)."""
        self.state = "start"
        self.screen_timer = START_SCREEN_TIME
        self.lives = INITIAL_LIVES
        self.time_seconds = 0.0
        self.time_alive = 0.0
        self.player.reset()
        self._create_enemies()

    def _reset_round(self) -> None:
        """Reinicia posições após uma batida, sem zerar tempo/vidas."""
        self.player.reset()
        for i, enemy in enumerate(self.enemy_list):
            enemy.rect.y = ENEMY_INITIAL_Y[i]
            enemy._y = float(enemy.rect.y)
            base = random.uniform(*ENEMY_SPEED_RANGE)
            enemy.speed = base

    def _create_enemies(self) -> None:
        """Cria os 3 carros inimigos fixos (um por faixa)."""
        self.enemies.empty()
        self.enemy_list.clear()
        for i, lane_x in enumerate(ENEMY_LANES):
            enemy = Enemy(lane_x, i)
            enemy.rect.y = ENEMY_INITIAL_Y[i]
            enemy._y = float(enemy.rect.y)
            self.enemy_list.append(enemy)
            self.enemies.add(enemy)

    # --- transições de tela ---------------------------------------------

    def _start_play(self) -> None:
        if self.state != "start":
            return
        self.state = "playing"
        play_music("music.wav")

    def _end_screen(self, state: str) -> None:
        stop_music()
        self.state = state
        self.screen_timer = END_SCREEN_TIME
        if state == "gameover" and self.crash_sound:
            self.crash_sound.play()
        elif state == "win" and self.applause_sound:
            self.applause_sound.play()

    # --- loop ------------------------------------------------------------

    def run(self) -> None:
        start_sound = load_sound("carroligando.mp3")
        if start_sound:
            start_sound.play()
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self._events()
            self._update(dt)
            self._draw()
        pygame.quit()

    def _events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == "start":
                    self._start_play()
                elif self.state in ("gameover", "win"):
                    self.running = False

    def _update(self, dt: float) -> None:
        if self.state == "start":
            self.screen_timer -= dt
            if self.screen_timer <= 0:
                self._start_play()
            return

        if self.state in ("gameover", "win"):
            self.screen_timer -= dt
            if self.screen_timer <= 0:
                self.running = False
            return

        # playing
        self.time_alive += dt
        self.time_seconds += dt

        boost = min(
            self.time_alive * (DIFFICULTY_RAMP / DIFFICULTY_INTERVAL_S),
            DIFFICULTY_MAX_SPEED - ENEMY_SPEED_RANGE[1],
        )

        keys = pygame.key.get_pressed()
        self.player.update(keys, dt)

        for enemy in self.enemies:
            enemy.update(dt)
            if enemy.rect.top > SCREEN_HEIGHT:
                enemy.recycle(boost)

        hits = pygame.sprite.spritecollide(
            self.player,
            self.enemies,
            False,
            pygame.sprite.collide_mask,
        )
        if hits:
            if self.crash_sound:
                self.crash_sound.play()
            self.lives -= 1
            if self.lives <= 0:
                self._end_screen("gameover")
                return
            self._reset_round()
            return

        if self.time_seconds >= WIN_TIME:
            self._end_screen("win")

    def _draw(self) -> None:
        if self.state == "start":
            self.screen.blit(self.start_image, (0, 0))
        elif self.state == "gameover":
            self.screen.blit(self.gameover_image, (0, 0))
        elif self.state == "win":
            self.screen.blit(self.win_image, (0, 0))
        else:
            self._draw_play()
        pygame.display.update()

    def _draw_play(self) -> None:
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        self.enemies.draw(self.screen)

        time_text = self.font.render(f"TEMPO: {int(self.time_seconds)}", True, WHITE, (0, 0, 0))
        self.screen.blit(time_text, (35, 30))
        lives_text = self.font.render(f"VIDAS: {self.lives}", True, RED, (0, 0, 0))
        self.screen.blit(lives_text, (35, 60))

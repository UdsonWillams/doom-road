import pygame
from time import sleep

from src.utils.constants import *
from src.utils.resource_loader import load_image, load_sound, play_music, stop_music
from src.entities.player import Player
from src.entities.enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Doom Road")
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial black', 20)
        
        # Load main assets
        self.bg_image = load_image("tela.png")
        self.start_image = load_image("inicio.png")
        self.gameover_image = load_image("gameover.png")
        self.win_image = load_image("vencedor.png")
        
        self.crash_sound = load_sound("batida.mp3")
        self.applause_sound = load_sound("apalusos.mp3")
        
        # State
        self.running = True
        self.timer_frames = 0
        self.time_seconds = 0
        self.lives = INITIAL_LIVES
        
        self.setup_entities()

    def setup_entities(self):
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        
        # Car 1
        self.enemy1 = Enemy(0, "carro1.png")
        # Car 2
        self.enemy2 = Enemy(1, "carro2.png")
        # Car 3
        self.enemy3 = Enemy(2, "carro3.png")
        
        self.enemies.add(self.enemy1, self.enemy2, self.enemy3)

    def show_start_screen(self):
        self.screen.blit(self.start_image, (0, 0))
        pygame.display.update()
        
        start_sound = load_sound("carroligando.mp3")
        if start_sound:
            start_sound.play()
            
        sleep(5.0)

    def reset_positions(self):
        self.player.reset()
        self.enemy1.reset_position(initial=True)
        self.enemy2.reset_position(initial=True)
        self.enemy3.reset_position(initial=True)

    def run(self):
        self.show_start_screen()
        play_music("music.wav")
        
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.lives <= 0:
            return
        if self.time_seconds > WIN_TIME:
            return

        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.enemies.update()
        
        # Timer logic
        self.timer_frames += 1
        if self.timer_frames >= FPS:
            self.time_seconds += 1
            self.timer_frames = 0
            
        # Collision logic
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        # We shrink the player bounding box implicitly by shrinking rect or we can just use defaults.
        # Original logic used to be heavily manual. If Pygame strict rects are too difficult, user can tell us later.
        if hits:
            if self.crash_sound:
                self.crash_sound.play()
            self.lives -= 1
            self.reset_positions()

        # Check win/loss state and handle them
        if self.lives <= 0:
            self.handle_game_over()
        elif self.time_seconds > WIN_TIME:
            self.handle_win()

    def handle_game_over(self):
        stop_music()
        if self.crash_sound:
            self.crash_sound.play()
        
        self.screen.blit(self.gameover_image, (0, 0))
        pygame.display.update()
        sleep(5)
        self.running = False

    def handle_win(self):
        stop_music()
        if self.applause_sound:
            self.applause_sound.play()
            
        self.screen.blit(self.win_image, (0, 0))
        pygame.display.update()
        sleep(5)
        self.running = False


    def draw(self):
        if self.lives <= 0 or self.time_seconds > WIN_TIME:
            return
            
        self.screen.blit(self.bg_image, (0, 0))
        
        # Draw entities
        self.screen.blit(self.player.image, self.player.rect)
        self.enemies.draw(self.screen)
        
        # Draw text
        time_text = self.font.render(f"TEMPO: {self.time_seconds}", True, WHITE, BLACK)
        self.screen.blit(time_text, (35, 30))
        
        lives_text = self.font.render(f"VIDAS: {self.lives}", True, RED, BLACK)
        self.screen.blit(lives_text, (35, 60))
        
        pygame.display.update()

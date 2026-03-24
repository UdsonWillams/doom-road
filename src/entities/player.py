import pygame
from src.utils.constants import PLAYER_SPEED, PLAYER_MIN_X, PLAYER_MAX_X, PLAYER_START_X, PLAYER_START_Y, SCREEN_HEIGHT
from src.utils.resource_loader import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("carro.png")
        self.rect = self.image.get_rect()
        self.reset()
        
    def reset(self):
        """Resets the player to the starting position."""
        self.rect.midtop = (PLAYER_START_X, PLAYER_START_Y)
        
    def update(self, keys):
        """Updates player position based on keyboard input."""
        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED
        if keys[pygame.K_d] and self.rect.centerx <= PLAYER_MAX_X:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_a] and self.rect.centerx >= PLAYER_MIN_X:
            self.rect.x -= PLAYER_SPEED

        # Keep player on screen vertically
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


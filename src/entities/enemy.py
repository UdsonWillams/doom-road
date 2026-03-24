import pygame
from random import randint
from src.utils.resource_loader import load_image
from src.utils.constants import ENEMY_LANES, ENEMY_SPEEDS, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, lane_index, image_name):
        """
        lane_index: 0, 1, or 2 (maps to lanes)
        image_name: 'carro1.png', 'carro2.png', or 'carro3.png'
        """
        super().__init__()
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()
        
        self.lane_index = lane_index
        self.speed = ENEMY_SPEEDS[lane_index]
        self.base_x = ENEMY_LANES[lane_index]
        self.rect.x = self.base_x
        
        self.reset_position(initial=True)
        
    def reset_position(self, initial=False):
        """Returns the enemy to the top of the screen at a random delay distance."""
        # The logic is based on the original game's random range for each car
        if self.lane_index == 0:
            offset = randint(80, 600)
            base_y = -500 if initial else 0
        elif self.lane_index == 1:
            offset = randint(1700, 2200)
            base_y = -200 if initial else 0
        elif self.lane_index == 2:
            offset = randint(800, 1500)
            base_y = -400 if initial else 0
            
        self.rect.y = base_y - offset
        
    def update(self):
        """Moves the enemy down and respawns if they pass the screen."""
        self.rect.y += self.speed
        
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

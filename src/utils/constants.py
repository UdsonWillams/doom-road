# src/utils/constants.py
import pygame

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 20  # Based on the original delay of 50ms (1000/50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player Configuration
PLAYER_START_X = 350
PLAYER_START_Y = 360
PLAYER_SPEED = 12
PLAYER_MIN_X = 170
PLAYER_MAX_X = 510

# Enemy Configuration
ENEMY_LANES = [180, 340, 500]  # The X positions of the 3 lanes from original game
ENEMY_SPEEDS = [14, 16, 16]    # Speeds of car1, car2, car3
ENEMY_START_Y = [-500, -200, -400]

# Game Rules
INITIAL_LIVES = 3
WIN_TIME = 60

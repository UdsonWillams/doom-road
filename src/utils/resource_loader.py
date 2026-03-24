import os
import pygame

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

def load_image(filename):
    """Loads an image from the assets/images directory."""
    path = os.path.join(IMAGES_DIR, filename)
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error as e:
        print(f"Cannot load image: {path} - {e}")
        # Return a red surface as a placeholder if not found
        surf = pygame.Surface((50, 100))
        surf.fill((255, 0, 0))
        return surf

def load_sound(filename):
    """Loads a sound from the assets/sounds directory."""
    path = os.path.join(SOUNDS_DIR, filename)
    try:
        return pygame.mixer.Sound(path)
    except pygame.error as e:
        print(f"Cannot load sound: {path} - {e}")
        return None

def play_music(filename, loops=-1):
    """Plays background music."""
    path = os.path.join(SOUNDS_DIR, filename)
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops)
    except pygame.error as e:
        print(f"Cannot stream music: {path} - {e}")

def stop_music():
    """Stops the background music."""
    pygame.mixer.music.stop()

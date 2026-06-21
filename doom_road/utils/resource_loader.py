"""Carregamento de assets com cache simples."""

from __future__ import annotations

from pathlib import Path

import pygame

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = BASE_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"

_image_cache: dict[tuple[str, float, tuple[int, int] | None], pygame.Surface] = {}
_sound_cache: dict[str, pygame.mixer.Sound | None] = {}


def load_image(
    filename: str,
    scale: float = 1.0,
    size: tuple[int, int] | None = None,
) -> pygame.Surface:
    """Carrega uma imagem de assets/images, com cache.

    Use ``size`` para redimensionar a um tamanho exato (largura, altura) — útil
    para padronizar sprites. ``scale`` aplica um fator relativo. Se ambos forem
    passados, ``size`` tem prioridade.
    """
    cache_key = (filename, scale, size)
    cached = _image_cache.get(cache_key)
    if cached is not None:
        return cached
    path = IMAGES_DIR / filename
    try:
        surf = pygame.image.load(str(path)).convert_alpha()
    except (pygame.error, FileNotFoundError) as exc:
        print(f"Cannot load image: {path} - {exc}")
        surf = pygame.Surface((50, 100), pygame.SRCALPHA)
        surf.fill((255, 0, 0, 255))
    if size is not None:
        surf = pygame.transform.scale(surf, size)
    elif scale != 1.0:
        w = round(surf.get_width() * scale)
        h = round(surf.get_height() * scale)
        surf = pygame.transform.scale(surf, (w, h))
    _image_cache[cache_key] = surf
    return surf


def load_sound(filename: str) -> pygame.mixer.Sound | None:
    """Carrega um som de assets/sounds, com cache."""
    if filename in _sound_cache:
        return _sound_cache[filename]
    path = SOUNDS_DIR / filename
    try:
        sound = pygame.mixer.Sound(str(path))
    except (pygame.error, FileNotFoundError) as exc:
        print(f"Cannot load sound: {path} - {exc}")
        sound = None
    _sound_cache[filename] = sound
    return sound


def play_music(filename: str, loops: int = -1) -> None:
    """Toca música de fundo (streaming)."""
    path = SOUNDS_DIR / filename
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play(loops)
    except (pygame.error, FileNotFoundError) as exc:
        print(f"Cannot stream music: {path} - {exc}")


def stop_music() -> None:
    """Para a música de fundo."""
    pygame.mixer.music.stop()

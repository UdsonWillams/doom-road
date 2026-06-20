"""Constantes de ajuste do jogo. Edite aqui para balancear."""

# Tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60  # loop baseado em dt -> roda igual em qualquer monitor

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Jogador (velocidades em px/seg; original era 12 px/frame @ 20fps = 240 px/s)
PLAYER_START_X = 350  # canto superior esquerdo inicial
PLAYER_START_Y = 360
PLAYER_SPEED = 240.0
PLAYER_MIN_X = 170  # limite esquerdo do canto do carro
PLAYER_MAX_X = 510  # limite direito do canto do carro
PLAYER_CLAMP_VERTICAL = True

# Inimigos / faixas
ENEMY_LANES = (180, 340, 500)  # x das 3 faixas (esquerda, meio, direita)
ENEMY_SPEED_RANGE = (260.0, 360.0)  # velocidade base sorteada (px/s)
ENEMY_MIN_SPEED = 200.0

# Sprites
# scale 0.85 = 85px; gap entre faixas = 75px > hitbox nula sem safe spot
SPRITE_SCALE = 0.85

# 3 carros fixos, 1 por faixa — cada faixa tem range de Y de respawn diferente.
# Quanto mais negativo, mais acima do topo o carro reaparece.
# Original: lane 0 = -80..-600, lane 1 = -1700..-2200, lane 2 = -800..-1500.
ENEMY_Y_RANGES = [
    (-600, -80),  # lane 0 (esquerda): respawna perto, aparece rápido
    (-2200, -1700),  # lane 1 (meio): respawna longe, demora mais
    (-1500, -800),  # lane 2 (direita): intermediário
]

# Y inicial de cada faixa (moderado, p/ ação começar rápido)
ENEMY_INITIAL_Y = (-500, -200, -400)

# Dificuldade progressiva suave
DIFFICULTY_RAMP = 18.0  # px/s adicionados a cada intervalo
DIFFICULTY_INTERVAL_S = 5.0  # a cada quantos segundos sobe
DIFFICULTY_MAX_SPEED = 520.0  # teto absoluto de velocidade

# Colisão — hitbox = sprite (scale 0.85 → 85px, gap 75px, sem safe spot)
HITBOX_RATIO = 1.0

# Regras
INITIAL_LIVES = 3
WIN_TIME = 60  # segundos para vencer

# Telas não-bloqueantes (segundos)
START_SCREEN_TIME = 4.5
END_SCREEN_TIME = 5.0

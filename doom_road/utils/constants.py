"""Constantes de ajuste do jogo. Edite aqui para balancear."""

# Tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60  # loop baseado em dt -> roda igual em qualquer monitor

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Sprites — todos os carros têm o MESMO tamanho (largura, altura), para visual
# uniforme e geometria de colisão previsível. Largura 64 deixa um vão de ~91px
# entre faixas (centros a 155px), maior que o carro do jogador → dá pra desviar.
CAR_SIZE = (64, 128)
_CAR_HALF_W = CAR_SIZE[0] // 2

# Pista (medida em tela.png): cinza vai de x=182 a 600; centros das 3 faixas
# (divisórias amarelas em ~291 e 491) ficam em 236, 391 e 545.
_LANE_CENTERS = (236, 391, 545)

# Jogador (velocidades em px/seg; original era 12 px/frame @ 20fps = 240 px/s)
PLAYER_START_X = _LANE_CENTERS[1] - _CAR_HALF_W  # 359 -> faixa do meio
PLAYER_START_Y = 440  # perto da base da tela
PLAYER_SPEED = 240.0
PLAYER_MIN_X = 184  # limite esquerdo do canto do carro (dentro da pista, x>=182)
PLAYER_MAX_X = 536  # limite direito do canto do carro (pista termina em 600)
PLAYER_CLAMP_VERTICAL = True

# Inimigos / faixas — x = canto esquerdo, centralizado em cada faixa real
ENEMY_LANES = tuple(c - _CAR_HALF_W for c in _LANE_CENTERS)  # (204, 359, 513)
ENEMY_SPEED_RANGE = (260.0, 360.0)  # velocidade base sorteada (px/s)
ENEMY_MIN_SPEED = 200.0

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

# Colisão — pixel-perfect (pygame.sprite.collide_mask); só conta batida quando
# os pixels visíveis dos carros realmente se tocam (sem falsos-positivos de canto).

# Regras
INITIAL_LIVES = 3
WIN_TIME = 60  # segundos para vencer

# Telas não-bloqueantes (segundos)
START_SCREEN_TIME = 4.5
END_SCREEN_TIME = 5.0

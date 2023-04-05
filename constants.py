SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARD_WIDTH = 10
BOARD_HEIGHT = 15
BORDER_WIDTH = 4
BORDER_COLOR = (255, 255, 255)
BLOCK_COLOR = (100, 100, 100)
BACKGROUND_COLOR = (0, 0, 255)
BORDER_PADDING = 20
BLOCK_BORDER_WIDTH = 1
PIECE_SPEED = .1

# Definer fargene for hver type brikke
YELLOW = (255, 255, 102)
GREEN = (102, 255, 102)
BLUE = (102, 178, 255)
RED = (255, 102, 102)
TURQUOISE = (64, 224, 208)
DARK_PURPLE = (83, 26, 119)
PINK = (219, 48, 122)

COLORS = {
    1: YELLOW,
    2: GREEN,
    3: BLUE,
    4: RED,
    5: TURQUOISE,
    6: DARK_PURPLE,
    7: PINK
}

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 0]],
]

SCORE_FOR_LINES = [
    0,
    40,
    100,
    300,
    1200
]



from copy import deepcopy
import random
from block import draw_block
from constants import *

class Piece:
    def __init__(self, shape, type):
        self.shape = shape
        self.type = type
        self.x = int(BOARD_WIDTH / 2 - len(self.shape[0]) / 2)
        self.y = 0
        self.color = COLORS[self.type]
        self.rotation = 0
        
    def rotate_clockwise2(self, board):
        """Rotates the piece clockwise"""
        # Make a copy of the piece to try rotating
        rotated_piece = deepcopy(self)
        # Rotate the copied piece
        rotated_piece.shape = list(zip(*self.shape[::-1]))
        # Check if the rotated piece collides with any existing blocks on the board
        if not board.check_collision(rotated_piece):
            self.shape = rotated_piece.shape
    
    def move_horizontally(self, board, direction):
        if (self.x == 0 and direction < 0):
            return
        elif (self.x == BOARD_WIDTH - len(self.shape[0])) and direction > 0:
            return

        moved_piece = deepcopy(self)
        moved_piece.x += direction
        if not board.check_collision(moved_piece):
            self.x = moved_piece.x

    def rotate_clockwise(self):
        self.rotation = (self.rotation + 1) % 4
        self.shape = self.get_rotated_shape()
        
    def get_rotated_shape(self):
        rotated_shape = []
        for y in range(len(self.shape[0])):
            new_row = []
            for x in range(len(self.shape)):
                new_row.append(self.shape[len(self.shape)-1-x][y])
            rotated_shape.append(new_row)
        return rotated_shape

    def draw_piece(self, screen, block_size):
        """Tegner Tetris-brikken på skjermen."""
        shape = self.shape
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] == 1:
                    draw_block(screen, self.x + j, self.y + i, self.color)

def generate_piece():
    """Genererer en tilfeldig Tetris-brikke."""
    shape = random.choice(SHAPES)
    type = SHAPES.index(shape) + 1
    return Piece(shape, type)

def get_dimensions(self):
    height = len(self.shape)
    width = len(self.shape[0])
    return width, height
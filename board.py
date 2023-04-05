import pygame
from block import draw_block
from constants import *

class Board:
    def __init__(self):
        self.board = []
        for i in range(BOARD_HEIGHT):
            row = [0] * BOARD_WIDTH
            self.board.append(row)

    def draw(self, screen):
        """Tegn brettet på skjermen."""

        # Tegn brettet
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if self.board[y][x] != 0:
                    # Tegn en blokk på posisjonen
                    draw_block(screen, x, y, self.board[y][x])
                else:
                    # Tegn en blokkramme på posisjonen
                    pygame.draw.rect(screen, BORDER_COLOR, (BORDER_PADDING + x * BLOCK_SIZE, BORDER_PADDING + y * BLOCK_SIZE,
                                                            BLOCK_SIZE, BLOCK_SIZE), BLOCK_BORDER_WIDTH)

    def check_collision(self, piece):
        """
        Checks if a piece would collide with existing blocks on the board if it were to be placed at position (x, y).
        Returns True if there is a collision, False otherwise.
        """
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[0])):
                # Check if the cell in the piece is non-empty
                if piece.shape[row][col] != 0:
                    # Calculate the position of the cell on the board
                    board_row = row + piece.y
                    board_col = col + piece.x
                    
                    # Check if the cell is out of bounds
                    if board_col < 0 or board_col >= BOARD_WIDTH or board_row >= BOARD_HEIGHT:
                        return True
                    # Check if the cell collides with an existing block on the board
                    if board_row >= 0 and board_col >= 0 and board_row < BOARD_HEIGHT and board_col < BOARD_WIDTH:
                        if self.board[board_row][board_col] != 0:
                            return True
        # If we reach this point, there is no collision
        return False

    def attach_piece(self, piece):
        """Legg til brikken i brettet."""
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j] != 0:
                    self.board[piece.y + i][piece.x + j] = piece.color

    def remove_full_rows(self):
        rows_to_remove = []
        for y in range(len(self.board)):
            if all(self.board[y]):
                rows_to_remove.append(y)
        for y in reversed(rows_to_remove):
            del self.board[y]
            self.board.insert(0, [0] * BOARD_WIDTH)
        return len(rows_to_remove)

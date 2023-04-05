import pygame

from constants import *

def draw_block(screen, x, y, color):
    """Tegn en blokk på skjermen."""
    rect = (BORDER_PADDING + BLOCK_SIZE * x, 
            BORDER_PADDING + BLOCK_SIZE * y, 
            BLOCK_SIZE, 
            BLOCK_SIZE)
    pygame.draw.rect(screen, color, rect)
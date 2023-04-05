import pygame

from constants import *


def draw_background(screen):
    """Tegn bakgrunn og ramme rundt brettet."""
    # Definer konstanter for bakgrunn og ramme

    
    # Tegn bakgrunn
    screen.fill(BACKGROUND_COLOR)
    
    # Tegn ramme rundt brettet
    pygame.draw.rect(screen, BORDER_COLOR, (BORDER_PADDING - BORDER_WIDTH,
                                            BORDER_PADDING - BORDER_WIDTH,
                                            BLOCK_SIZE * BOARD_WIDTH + BORDER_WIDTH * 2,
                                            BLOCK_SIZE * BOARD_HEIGHT + BORDER_WIDTH * 2),
                                            BORDER_WIDTH)


def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.x = BORDER_WIDTH + BLOCK_SIZE * BOARD_WIDTH + 20  # øker x-posisjonen med bredden på brettet pluss en margin
    score_rect.y = BORDER_WIDTH
    screen.blit(score_text, score_rect)

import pygame
from constants import *

def game_over_screen(screen, score):
    # Grå ut bakgrunnen
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))

    # Tegn teksten "GAME OVER" med store bokstaver
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("GAME OVER", True, WHITE)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(game_over_text, text_rect)

    # Tegn poengsummen
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))
    screen.blit(score_text, score_rect)

    pygame.display.flip()

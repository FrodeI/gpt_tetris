import pygame
import background
from board import Board
from client import TetrisClient
from constants import *
from game_over import game_over_screen
from piece import generate_piece

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
background.draw_background(screen)
clock = pygame.time.Clock()

# Hovedspill-løkken
def main():
    current_piece = generate_piece()
    board = Board()
    piece_fall_counter = 0  # Teller for å bestemme når brikken skal falle nedover
    game_over = False
    score = 0
    client = TetrisClient('127.0.0.1', 12345)
    client.connect()
    message = {'action': 'start_game'}
    client.send_message(message)

    """Hovedspill-løkken."""
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move_horizontally(board, -1)
                elif event.key == pygame.K_RIGHT:
                    current_piece.move_horizontally(board, 1)
                elif event.key == pygame.K_SPACE:
                    current_piece.rotate_clockwise2(board)
        
        # Tegne og bevege brikken
        piece_fall_counter += clock.tick(FPS)
        if piece_fall_counter >= 1000 / (PIECE_SPEED * FPS):
            piece_fall_counter = 0
            current_piece.y += 1
            if board.check_collision(current_piece):
                # Flytt brikken tilbake dit den var
                # Feste brikken til brettet og trekke en ny brikke
                current_piece.y -= 1
                board.attach_piece(current_piece)
                score += SCORE_FOR_LINES[board.remove_full_rows()]
                current_piece = generate_piece()
                if board.check_collision(current_piece):
                    # Kan ikke plassere ny brikke uten å kollidere med eksisterende blokker
                    game_over = True

        # Tegn bakgrunn
        background.draw_background(screen)
        background.draw_score(screen, score)

        # Tegn brettet
        board.draw(screen)

        # Tegn brikken
        # Flytt brikken nedover etter en viss tid
        current_piece.draw_piece(screen, BLOCK_SIZE)
        
        # Oppdater skjermen
        # pygame.display.update()
        pygame.display.flip()
        
    game_over_screen(screen, score)
    while True:  # Ny while-løkke
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Avslutt programmet hvis spilleren trykker på lukk-knappen

# Kjør hovedfunksjonen
if __name__ == '__main__':
    main()

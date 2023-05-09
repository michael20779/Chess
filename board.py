import pygame
import sys
from piece import King, Advisor, Elephant, Horse, Chariot, Cannon, Soldier



# Screen dimensions
WIDTH = 800
HEIGHT = 900


# Board dimensions
BOARD_SIZE = 8, 9
SQUARE_SIZE = WIDTH // BOARD_SIZE[0]
 
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_board(screen):
    screen.fill(WHITE)

    # Draw horizontal lines
    for i in range(BOARD_SIZE[1]):
        start_pos = (0, i * SQUARE_SIZE)
        end_pos = (WIDTH, i * SQUARE_SIZE)
        pygame.draw.line(screen, BLACK, start_pos, end_pos, 3)

    # Draw vertical lines
    for i in range(BOARD_SIZE[0]):
        if i > 0 and i < BOARD_SIZE[0] - 0:
            start_pos = (i * SQUARE_SIZE, 1)
            end_pos = (i * SQUARE_SIZE, SQUARE_SIZE * 4)
            pygame.draw.line(screen, BLACK, start_pos, end_pos, 3)

            start_pos = (i * SQUARE_SIZE, SQUARE_SIZE * 5)
            end_pos = (i * SQUARE_SIZE, HEIGHT)
            pygame.draw.line(screen, BLACK, start_pos, end_pos, 3)
        else:
            start_pos = (i * SQUARE_SIZE, 0)
            end_pos = (i * SQUARE_SIZE, HEIGHT)
            pygame.draw.line(screen, BLACK, start_pos, end_pos, 3)

    # Draw palace diagonals
    pygame.draw.line(screen, BLACK, (3 * SQUARE_SIZE, 0), (5 * SQUARE_SIZE, 2 * SQUARE_SIZE), 3)
    pygame.draw.line(screen, BLACK, (5 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, 2 * SQUARE_SIZE), 3)
    pygame.draw.line(screen, BLACK, (3 * SQUARE_SIZE, 7 * SQUARE_SIZE), (5 * SQUARE_SIZE, 9 * SQUARE_SIZE), 3)
    pygame.draw.line(screen, BLACK, (5 * SQUARE_SIZE, 7 * SQUARE_SIZE), (3 * SQUARE_SIZE, 9 * SQUARE_SIZE), 3)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chinese Chess")

    clock = pygame.time.Clock()
    # Create a red King piece at position (4, 0)
    red_king = King(4 * SQUARE_SIZE, 0, "RED")

    # Create a black King piece at position (4, 8)
    black_king = King(4 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")

    # Create red Advisor pieces
    red_advisor1 = Advisor(3 * SQUARE_SIZE, 0, "RED")
    red_advisor2 = Advisor(5 * SQUARE_SIZE, 0, "RED")

    # Create black Advisor pieces
    black_advisor1 = Advisor(3 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")
    black_advisor2 = Advisor(5 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")

    # Create red Elephant pieces
    red_elephant1 = Elephant(2 * SQUARE_SIZE, 0, "RED")
    red_elephant2 = Elephant(6 * SQUARE_SIZE, 0, "RED")

    # Create black Elephant pieces
    black_elephant1 = Elephant(2 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")
    black_elephant2 = Elephant(6 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")

    # Create red Horse pieces
    red_horse1 = Horse(1 * SQUARE_SIZE, 0, "RED")
    red_horse2 = Horse(7 * SQUARE_SIZE, 0, "RED")

    # Create black Horse pieces
    black_horse1 = Horse(1 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")
    black_horse2 = Horse(7 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")

    # Create red Chariot pieces
    red_chariot1 = Chariot(0 * SQUARE_SIZE, 0, "RED")
    red_chariot2 = Chariot(8 * SQUARE_SIZE, 0, "RED")

    # Create black Chariot pieces
    black_chariot1 = Chariot(0 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")
    black_chariot2 = Chariot(8 * SQUARE_SIZE, 9 * SQUARE_SIZE, "BLACK")


    # Create red Cannon pieces
    red_cannon1 = Cannon(1 * SQUARE_SIZE, 2 * SQUARE_SIZE, "RED")
    red_cannon2 = Cannon(7 * SQUARE_SIZE, 2 * SQUARE_SIZE, "RED")

    # Create black Cannon pieces
    black_cannon1 = Cannon(1 * SQUARE_SIZE, 7 * SQUARE_SIZE, "BLACK")
    black_cannon2 = Cannon(7 * SQUARE_SIZE, 7 * SQUARE_SIZE, "BLACK")

    # Create red Soldier pieces
    red_soldiers = [Soldier(i * SQUARE_SIZE, 3 * SQUARE_SIZE, "RED") for i in range(BOARD_SIZE[1]) if i % 2 == 0]

    # Create black Soldier pieces
    black_soldiers = [Soldier(i * SQUARE_SIZE, 6 * SQUARE_SIZE, "BLACK") for i in range(BOARD_SIZE[1]) if i % 2 == 0]

    selected_piece = None
    current_player = "RED"

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = mouse_x // SQUARE_SIZE
                    grid_y = mouse_y // SQUARE_SIZE

                    if not selected_piece:
                        # Check if a piece is clicked
                        for piece in (red_king, black_king, red_advisor1, red_advisor2, black_advisor1, black_advisor2,
                                    red_elephant1, red_elephant2, black_elephant1, black_elephant2, red_horse1, red_horse2,
                                    black_horse1, black_horse2, red_chariot1, red_chariot2, black_chariot1, black_chariot2,
                                    red_cannon1, red_cannon2, black_cannon1, black_cannon2, *red_soldiers, *black_soldiers):
                            if piece.color == current_player and grid_x * SQUARE_SIZE == piece.x and grid_y * SQUARE_SIZE == piece.y:
                                selected_piece = piece
                                break
                    else:
                        # Move the selected piece
                        selected_piece.move(grid_x * SQUARE_SIZE, grid_y * SQUARE_SIZE)
                        selected_piece = None

                        # Change the current player
                        current_player = "BLACK" if current_player == "RED" else "RED"
            draw_board(screen)

            # Draw the King pieces on the board
            red_king.draw(screen)
            black_king.draw(screen)

            # Draw the Advisor pieces on the board
            red_advisor1.draw(screen)
            red_advisor2.draw(screen)
            black_advisor1.draw(screen)
            black_advisor2.draw(screen)

            # Draw the Elephant pieces on the board
            red_elephant1.draw(screen)
            red_elephant2.draw(screen)
            black_elephant1.draw(screen)
            black_elephant2.draw(screen)

            # Draw the Horse pieces on the board
            red_horse1.draw(screen)
            red_horse2.draw(screen)
            black_horse1.draw(screen)
            black_horse2.draw(screen)

            # Draw the Chariot pieces on the board
            red_chariot1.draw(screen)
            red_chariot2.draw(screen)
            black_chariot1.draw(screen)
            black_chariot2.draw(screen)

            # Draw the Cannon pieces on the board
            red_cannon1.draw(screen)
            red_cannon2.draw(screen)
            black_cannon1.draw(screen)
            black_cannon2.draw(screen)

            # Draw the Soldier pieces on the board
            for red_soldier in red_soldiers:
                red_soldier.draw(screen)
            for black_soldier in black_soldiers:
                black_soldier.draw(screen)



            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()

import pygame
import pygame.font
from dotenv import load_dotenv

load_dotenv('./env', override=True)

# Set the dimensions of the board and each cell
CELL_SIZE = 100
NUM_ROWS = 5
NUM_COLS = 5

# Calculate the size of the window
WINDOW_WIDTH = CELL_SIZE * NUM_COLS
WINDOW_HEIGHT = CELL_SIZE * (NUM_ROWS + 2)  # Extra rows for the top space and score bar

# Set the colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_board():
    # Initialize Pygame
    pygame.init()

    # Create the game window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Connect Four Board")

    # Clear the window
    window.fill(BLACK)

    # Create font objects for the score text
    font = pygame.font.Font(None, 36)

    # Draw the score bar for Player 1 (yellow) and display the score
    pygame.draw.rect(window, YELLOW, (0, 0, WINDOW_WIDTH // 2, CELL_SIZE // 2))
    player1_score = 0  # Example score for Player 1 - you'd want to use game logic to make this run
    player1_text = font.render("Player 1: " + str(player1_score), True, BLACK)
    window.blit(player1_text, (10, 10))

    # Draw the score bar for Player 2 (red) and display the score
    pygame.draw.rect(window, RED, (WINDOW_WIDTH // 2, 0, WINDOW_WIDTH // 2, CELL_SIZE // 2))
    player2_score = 0  # Example score for Player 2 - you'd want to use game logic to make this run
    player2_text = font.render("Player 2: " + str(player2_score), True, BLACK)
    window.blit(player2_text, (WINDOW_WIDTH // 2 + 10, 10))

    # Draw the board
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pygame.draw.rect(window, BLUE, (col * CELL_SIZE, (row + 2) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(window, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, (row + 2) * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

    # Update the display
    pygame.display.flip()

    # Wait until the user closes the window
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    # Quit the game
    pygame.quit()

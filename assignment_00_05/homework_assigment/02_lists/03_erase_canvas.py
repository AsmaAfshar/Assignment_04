#Problem Statement
#Implement an 'eraser' on a canvas.

#The canvas consists of a grid of blue 'cells' which are drawn as 
# rectangles on the screen. We then create an eraser rectangle which, 
# when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ERASER_SIZE = 60
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BG_COLOR = (200, 200, 200)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create the grid
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position and draw eraser rectangle
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser_rect = pygame.Rect(mouse_x, mouse_y, ERASER_SIZE, ERASER_SIZE)

    # Erase cells under eraser
    if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
        for row in range(rows):
            for col in range(cols):
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if eraser_rect.colliderect(cell_rect):
                    grid[row][col] = WHITE

    # Draw grid
    for row in range(rows):
        for col in range(cols):
            cell_color = grid[row][col]
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, cell_color, cell_rect)
            pygame.draw.rect(screen, (150, 150, 150), cell_rect, 1)  # Grid lines

    # Draw eraser outline
    pygame.draw.rect(screen, (0, 0, 0), eraser_rect, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

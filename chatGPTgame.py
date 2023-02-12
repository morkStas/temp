import pygame
import numpy as np

# Initialize Pygame and screen
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))

# Define the grid size and create a numpy array to store the state of each cell
grid_size = 50
grid = np.zeros((grid_size, grid_size))

# Initialize the state of the cells
grid[2, 3] = 1
grid[3, 4] = 1
grid[4, 2] = 1
grid[4, 3] = 1
grid[4, 4] = 1

# Set the size of each cell in the grid
cell_size = width // grid_size

# Set the game loop to run until the user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            if grid[row, col] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rect)

    # Calculate the number of live neighbors for each cell
    neighbors = np.zeros((grid_size, grid_size))
    for row in range(grid_size):
        for col in range(grid_size):
            # Check the top left cell
            if row > 0 and col > 0:
                neighbors[row, col] += grid[row - 1, col - 1]
            # Check the top cell
            if row > 0:
                neighbors[row, col] += grid[row - 1, col]
            # Check the top right cell
            if row > 0 and col < grid_size - 1:
                neighbors[row, col] += grid[row - 1, col + 1]
            # Check the left cell
            if col > 0:
                neighbors[row, col] += grid[row, col - 1]
            # Check the right cell
            if col < grid_size - 1:
                neighbors[row, col] += grid[row, col + 1]
            # Check the bottom left cell
            if row < grid_size - 1 and col > 0:
                neighbors[row, col] += grid[row + 1, col - 1]
            # Check the bottom cell
            if row < grid_size - 1:
                neighbors[row, col] += grid[row + 1, col]
            # Check the bottom right cell
            if row < grid_size - 1 and col < grid_size - 1:
                neighbors[row, col] += grid[row + 1, col + 1]

    # Update the state of each cell based on the number of live neighbors
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row, col] == 1 and (neighbors[row, col] < 2 or neighbors[row, col] > 3):
                grid[row, col] = 0
            elif grid[row, col] == 0 and neighbors[row, col] == 3:
                grid[row, col] = 1

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
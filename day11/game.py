import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = (CELL_SIZE, 0)  # moving right

# Food setup
food = (random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE))

# Font
font = pygame.font.SysFont("Arial", 24)

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, CELL_SIZE):
        snake_direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_direction != (0, -CELL_SIZE):
        snake_direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_direction != (CELL_SIZE, 0):
        snake_direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-CELL_SIZE, 0):
        snake_direction = (CELL_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + snake_direction[0],
                snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Check collision with food
    if snake[0] == food:
        score += 1
        snake.append(snake[-1])  # grow snake
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))

    # Check collision with walls
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
        snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        text = font.render("Game Over! Final Score: " + str(score), True, WHITE)
        screen.blit(text, (WIDTH//6, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Check collision with self
    if snake[0] in snake[1:]:
        text = font.render("Game Over! Final Score: " + str(score), True, WHITE)
        screen.blit(text, (WIDTH//6, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Show score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # snake speed

pygame.quit()
sys.exit()

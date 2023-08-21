import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
BLOCK_WIDTH, BLOCK_HEIGHT = 60, 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
BLOCK_ROWS = 5
BLOCK_COLS = 10
BLOCK_GAP = 10
PADDLE_SPEED = 5
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Create the paddle
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]

# Create the blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * (BLOCK_WIDTH + BLOCK_GAP), row * (BLOCK_HEIGHT + BLOCK_GAP) + 50, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddle
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]
            break

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddle, ball, and blocks
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.circle(screen, BLUE, ball.center, BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()

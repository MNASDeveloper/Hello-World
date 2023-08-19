import pygame
import random

# Initialize pygame
pygame.init()

# Set up display dimensions
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'

# Food position
food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize score
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for key presses
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                snake_direction = 'LEFT'
            if keys[pygame.K_RIGHT]:
                snake_direction = 'RIGHT'
            if keys[pygame.K_UP]:
                snake_direction = 'UP'
            if keys[pygame.K_DOWN]:
                snake_direction = 'DOWN'

    # Update snake position based on direction
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,
                    random.randrange(1, (height//10)) * 10]
        food_spawn = True

    # Draw snake and food
    display.fill(black)
    for pos in snake_body:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(display, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        pygame.quit()
        quit()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        pygame.quit()
        quit()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(15)

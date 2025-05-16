import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and properties
snake_block = 10
snake_speed = 15
x1 = screen_width / 2
y1 = screen_height / 2
x1_change = 0
y1_change = 0
snake_list = []
snake_length = 1

# Food initial position and properties
foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Font
font = pygame.font.SysFont(None, 30)

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Main game loop
clock = pygame.time.Clock()

def game_over():
    # Display game over message and score
    message = font.render("Game Over! Your score: " + str(snake_length - 1), True, red)
    screen.blit(message, [screen_width / 3, screen_height / 3])
    pygame.display.update()
    pygame.time.wait(2000)

game_over_flag = False

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Boundary conditions for game over
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over()
        game_over_flag = True

    # Move the snake
    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over()
            game_over_flag = True

    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Check if snake has eaten food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

pygame.quit()
quit()

import pygame
import random

# Initialize the game
pygame.init()

# Set up the window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 48)

# Set up the snake and food positions
snake_pos = [[100, 50]]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (width // 10)) * 10,
            random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set up the initial direction
direction = 'RIGHT'
change_to = direction

# Set up the game over flag
game_over = False


# Function to display the score on the screen
def show_score(score):
    text_surface = font.render("Score: " + str(score), True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (width / 2, 10)
    window.blit(text_surface, text_rect)


# Function to display the game over message
def game_over_message():
    text_surface = font.render("Game Over!", True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (width / 2, height / 4)
    window.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)


# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update the direction of the snake
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_pos[0][1] -= 10
    elif direction == 'DOWN':
        snake_pos[0][1] += 10
    elif direction == 'LEFT':
        snake_pos[0][0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0][0] += 10

    # Check for game over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos[0] == block:
            game_over = True

    # Check if the snake has eaten the food
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food if necessary
    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10,
                    random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Update the game window
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, blue, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the snake's body
    snake_body.insert(0, list(snake_pos[0]))

    # Display the score
    show_score(len(snake_body) - 1)

    # Refresh the game screen
    pygame.display.update()

    # Control the game speed
    clock.tick(15)

# Show game over message and quit the game
game_over_message()
pygame.quit()

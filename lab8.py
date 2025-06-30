# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Speeds and scores
SPEED = 5
SCORE = 0
COINS = 0  # Number of collected coins

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create main window
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Coin sprite class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Set up sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:

    # Check events (keyboard, close window, speed increment)
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Draw score and coin count
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check collision with coins
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Refresh game screen and maintain FPS
    pygame.display.update()
    FramePerSec.tick(FPS)

# the second challange :
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Grid size
BLOCK_SIZE = 20

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 10  # initial speed

# Fonts for score & level
font = pygame.font.SysFont("Verdana", 20)

# Snake starting variables
snake_pos = [[100, 50], [80, 50], [60, 50]]  # list of positions, head first
snake_dir = "RIGHT"  # current direction
change_to = snake_dir

# Food variables
food_pos = [random.randrange(1, SCREEN_WIDTH//BLOCK_SIZE) * BLOCK_SIZE,
            random.randrange(1, SCREEN_HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]

# Score & Level
score = 0
level = 1

# Function to generate new food avoiding the snake
def spawn_food():
    while True:
        pos = [random.randrange(1, SCREEN_WIDTH//BLOCK_SIZE) * BLOCK_SIZE,
               random.randrange(1, SCREEN_HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]
        if pos not in snake_pos:
            return pos

# Main game loop
while True:
    # Check for events (key presses & quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_dir == "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and not snake_dir == "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and not snake_dir == "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and not snake_dir == "LEFT":
                change_to = "RIGHT"

    # Update direction
    snake_dir = change_to

    # Move the snake
    if snake_dir == "UP":
        new_head = [snake_pos[0][0], snake_pos[0][1] - BLOCK_SIZE]
    elif snake_dir == "DOWN":
        new_head = [snake_pos[0][0], snake_pos[0][1] + BLOCK_SIZE]
    elif snake_dir == "LEFT":
        new_head = [snake_pos[0][0] - BLOCK_SIZE, snake_pos[0][1]]
    elif snake_dir == "RIGHT":
        new_head = [snake_pos[0][0] + BLOCK_SIZE, snake_pos[0][1]]

    # Insert new head
    snake_pos.insert(0, new_head)

    # Check if snake eats the food
    if snake_pos[0] == food_pos:
        score += 1
        food_pos = spawn_food()
        # Increase level every 4 foods
        if score % 4 == 0:
            level += 1
            FPS += 2  # Increase speed
    else:
        # Remove last segment (move forward)
        snake_pos.pop()

    # Check for collision with walls
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= SCREEN_WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT):
        pygame.quit()
        sys.exit()

    # Check for collision with itself
    if snake_pos[0] in snake_pos[1:]:
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)

    # Draw snake
    for block in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw score & level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(FPS)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'line'
    color_mode = 'blue'
    points = []
    start_pos = None
    drawing_shape = False
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Change color
                if event.key == pygame.K_r:
                    color_mode = 'red'
                elif event.key == pygame.K_g:
                    color_mode = 'green'
                elif event.key == pygame.K_b:
                    color_mode = 'blue'
                
                # Change drawing mode
                if event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rect'
                elif event.key == pygame.K_l:
                    mode = 'line'
            
            # Adjust radius
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing_shape = True
                    if mode == 'line':
                        points.append(start_pos)
                        points = points[-256:]
                elif event.button == 3: # Right click shrinks
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape:
                    end_pos = event.pos
                    if mode == 'rect':
                        drawRectangle(screen, start_pos, end_pos, radius, color_mode)
                    elif mode == 'circle':
                        drawCircle(screen, start_pos, end_pos, radius, color_mode)
                    drawing_shape = False
                    start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if mode == 'line' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
        
        # Fill background
        if mode != 'eraser':
            screen.fill((0, 0, 0))
        
        # Draw lines
        if mode == 'line' or mode == 'eraser':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color_mode, mode)
                i += 1
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, mode):
    # Create fading color effect
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (c1, c1, c2)
        elif color_mode == 'red':
            color = (c2, c1, c1)
        elif color_mode == 'green':
            color = (c1, c2, c1)
    
    # Draw small circles along the line
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, width, color_mode):
    # Calculate color
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    # Draw rectangle
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, rect, width)

def drawCircle(screen, start, end, width, color_mode):
    # Calculate color
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    # Calculate radius
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    pygame.draw.circle(screen, color, start, radius, width)

main()


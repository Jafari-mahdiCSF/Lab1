# this is the content of the lab 7
# first problem 
import pygame
import sys
import math
import time
from datetime import datetime

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load images
background = pygame.image.load("mickey_body.png").convert_alpha()
right_hand = pygame.image.load("right_hand.png").convert_alpha()  # minutes
left_hand = pygame.image.load("left_hand.png").convert_alpha()    # seconds

# Resize if needed
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clock center
center = (WIDTH // 2, HEIGHT // 2)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    now = datetime.now()
    second = now.second
    minute = now.minute

    # Convert to angles
    sec_angle = -second * 6   # 360 / 60
    min_angle = -minute * 6

    # Rotate hands
    rotated_left = pygame.transform.rotate(left_hand, sec_angle)
    rotated_right = pygame.transform.rotate(right_hand, min_angle)

    # Get new rects centered around the pivot
    left_rect = rotated_left.get_rect(center=center)
    right_rect = rotated_right.get_rect(center=center)

    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(rotated_left, left_rect)
    screen.blit(rotated_right, right_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# music player


import pygame
import os

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Window setup (not required but allows event loop)
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Keyboard Music Player")

# Load music files
music_folder = "music"
playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]
playlist.sort()  # Sort files alphabetically

# Track state
current_track = 0
is_playing = False

# Function to load and play music
def play_music(index):
    global is_playing
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    is_playing = True
    print(f"Now Playing: {os.path.basename(playlist[index])}")

# Function to stop music
def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("Stopped")

# Function to pause/resume
def toggle_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
        print("Paused")
    else:
        pygame.mixer.music.unpause()
        is_playing = True
        print("Resumed")

# Start event loop
running = True
print("Controls: P = Play/Pause, S = Stop, N = Next, B = Previous")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    toggle_pause()
                else:
                    play_music(current_track)
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

    pygame.display.flip()

pygame.quit()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
 # red ball (circle) of size 50×50 
import pygame
import sys

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Red Ball")

# Ball setup
RADIUS = 25
ball_color = (255, 0, 0)  # Red
bg_color = (255, 255, 255)  # White
x, y = WIDTH // 2, HEIGHT // 2  # Start in the center

# Movement step
STEP = 20

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(bg_color)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (x, y), RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - STEP - RADIUS >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + STEP + RADIUS <= HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x - STEP - RADIUS >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + STEP + RADIUS <= WIDTH:
                x += STEP

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



import pygame 
import sys 
import random 

# Initialize Pygame 
pygame.init() 

# Constants 
SCREEN_WIDTH, 
SCREEN_HEIGHT = 400, 600 
GRAVITY = 0.25 
BIRD_MOVEMENT = 0 
GAME_SPEED = -4 

# Set up the display 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock() 
font = pygame.font.Font(None, 50) 

# Load images 
bg_surface = pygame.image.load('background.png').convert() 
floor_surface = pygame.image.load('floor.png').convert() 
bird_surface = pygame.image.load('bird.png').convert_alpha() 
pipe_surface = pygame.image.load('pipe.png').convert_alpha() 

# Scale images 
bg_surface = pygame.transform.scale(bg_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)) 
floor_surface = pygame.transform.scale(floor_surface, (SCREEN_WIDTH, 100)) 
pipe_surface = pygame.transform.scale(pipe_surface, (80, 400)) 

# Bird rectangle 
bird_rect = bird_surface.get_rect(center = (100, SCREEN_HEIGHT//2)) 

# Pipe list and timer 
pipe_list = [] 
SPAWNPIPE = pygame.USEREVENT pygame.time.set_timer(SPAWNPIPE, 1200) 

def create_pipe(): 
 random_pipe_pos = random.choice([300, 400, 500]) 
 bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos)) 
 top_pipe = pipe_surface.get_rect(midbottom = (500, random_pipe_pos - 150)) 
 return bottom_pipe, top_pipe 
 def move_pipes(pipes): 
 for pipe in pipes: 
  pipe.centerx += 
  GAME_SPEED 
  visible_pipes = [pipe for pipe in pipes if pipe.right > 0] 
  return visible_pipes 
  
  def draw_pipes(pipes): 
  for pipe in pipes: 
  if pipe.bottom >= 
  SCREEN_HEIGHT: 
   screen.blit(pipe_surface, pipe) else: flip_pipe = pygame.transform.flip(pipe_surface, False, True) screen.blit(flip_pipe, pipe) 
   
# Main game loop 
while True: 
for event in pygame.event.get(): 
if event.type == 
pygame.QUIT: 
 pygame.quit() 
 sys.exit() 
 if event.type == 
 pygame.KEYDOWN: 
 if event.key == 
 pygame.K_SPACE: 
  BIRD_MOVEMENT = 0 
  BIRD_MOVEMENT -= 10 
  if event.type == SPAWNPIPE: 
   pipe_list.extend(create_pipe()) 
   screen.blit(bg_surface, (0, 0)) 
   
# Bird 
BIRD_MOVEMENT += GRAVITY 
bird_rect.centery += 
BIRD_MOVEMENT screen.blit(bird_surface, bird_rect) 

# Pipes 
pipe_list = move_pipes(pipe_list) 
draw_pipes(pipe_list) 

# Floor 
screen.blit(floor_surface, (0, SCREEN_HEIGHT - 100)) 
pygame.display.update() clock.tick(120)

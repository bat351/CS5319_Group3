import pygame, sys

# ModelCe
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
SCREEN = pygame.display.set_mode((800, 800))

CHECKERS_WINS = [0, 0]
CONNECT_4_WINS = [0, 0]
TIC_TAC_TOE_WINS = [0, 0]

CURRENT_PLAYER = 'Player 1'

BG = pygame.image.load("assets/Background.png")

def change_player():
  global CURRENT_PLAYER
  if CURRENT_PLAYER == 'Player 1':
    CURRENT_PLAYER = 'Player 2'
  else:
    CURRENT_PLAYER = 'Player 1'

def get_player():
  return CURRENT_PLAYER

def reset_player():
  global CURRENT_PLAYER
  CURRENT_PLAYER = 'Player 1'
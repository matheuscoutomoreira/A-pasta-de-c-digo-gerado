# C
import pygame

COLOR_ORANGE = 255, 128, 0
COLOR_WHITE = 255, 255, 255
COLOR_YELLOW = 255, 252, 46
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               "EXIT")
# W
WIN_WIDTH = 576
WIN_HEIGTH = 324

# E
ENTITY_SPEED = {'level1_backgroud 0': 0,
                'level1_backgroud 1': 1,
                'level1_backgroud 2': 2,
                'level1_backgroud 3': 3,
                'level1_backgroud 4': 4,
                'level1_backgroud 5': 5,
                'level1_backgroud 6': 6,
                'player1': 3, 'player2': 3,
                'inimigo1': 2,
                'inimigo2': 1}

PLAYER_UP = {'player1': pygame.K_UP,
             'player2': pygame.K_w}

PLAYER_DOWN = {'player1': pygame.K_DOWN,
               'player2': pygame.K_s}

PLAYER_LEFT = {'player1': pygame.K_LEFT,
               'player2': pygame.K_a}

PLAYER_RIGHT = {'player1': pygame.K_RIGHT,
                'player2': pygame.K_d}
EVENT_ENEMY = pygame.USEREVENT +1
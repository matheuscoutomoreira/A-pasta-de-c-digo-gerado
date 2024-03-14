#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import menu as menu
import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Menu import Menu
from code.level import level
from const import WIN_WIDTH, WIN_HEIGTH, MENU_OPTION


class game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu1 = Menu(self.window)
            menu_return = menu1.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level1 = level(self.window, 'level1', menu_return)
                level_return = level1.run()
            else:
                pygame.quit()
                sys.exit()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import menu as menu
import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Menu import Menu
from const import WIN_WIDTH, WIN_HEIGTH


class game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)

            menu.run()



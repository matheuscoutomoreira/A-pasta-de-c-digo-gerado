#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/PRE_ORIG_SIZE.png')
        self.react = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.react)
            self.menu_text(50, "montain", (255, 32, 21), ((WIN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)


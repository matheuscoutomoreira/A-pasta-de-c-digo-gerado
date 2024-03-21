#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

from pygame.font import Font

from code.const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.entity import entity

import pygame.display
from pygame import Surface, Rect

from code.entityFactori import entityFactori


class level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[entity] = []  # Informando ao IDE que entity_list contém objetos da classe Entity
        self.entity_list.extend(entityFactori.get_entity('level1_backgroud', (0, 0)))
        self.entity_list.append(entityFactori.get_entity('player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(entityFactori.get_entity('player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # aqui eu desenho as minhas entidades
                self.level_text(14, f'fps : {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(entityFactori.get_entity(choice))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text__position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text__position[0], top=text__position[1])
        self.window.blit(source=text_surf, dest=text_rect)

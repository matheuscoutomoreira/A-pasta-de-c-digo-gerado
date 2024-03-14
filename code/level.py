#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.entity import entity

import pygame.display
from pygame import Surface

from code.entityFactori import entityFactori


class level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[entity] = []  # Informando ao IDE que entity_list contém objetos da classe Entity
        self.entity_list.extend(entityFactori.get_entity('level1_backgroud', (0, 0)))

    def run(self,):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass


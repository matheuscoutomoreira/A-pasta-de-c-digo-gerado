#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGTH, PLAYER_UP, PLAYER_DOWN, PLAYER_LEFT, PLAYER_RIGHT, WIN_WIDTH
from code.entity import entity


class pleyer(entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[
            PLAYER_UP[
                self.nome]] and self.rect.top > 0:  # se a tecla para cima for pressionada temos que mover o retangulo
            # para cima
            self.rect.centery -= ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_DOWN[
            self.nome]] and self.rect.bottom < WIN_HEIGTH:
            self.rect.centery += ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_LEFT[
            self.nome]] and self.rect.left > 0:  # se a tecla para cima for pressionada temos que mover o retangulo para cima
            self.rect.centerx -= ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_RIGHT[
            self.nome]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.nome]

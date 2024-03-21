#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import entity


class enemy(entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.nome]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

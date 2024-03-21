#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import entity
from code.const import WIN_WIDTH, ENTITY_SPEED


class bacgraud(entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.nome]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass

#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.bacgraud import bacgraud
from code.const import WIN_WIDTH, WIN_HEIGTH
from code.enemy import enemy
from code.pleyer import pleyer


class entityFactori:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1_backgroud':
                list_bg = []
                for i in range(7):
                    list_bg.append(bacgraud(f'level1_backgroud {i}', position))
                    list_bg.append(bacgraud(f'level1_backgroud {i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'player1':
                return pleyer('player1', (10, WIN_HEIGTH / 2 - 20))

            case 'player2':
                return pleyer('player2', (10, WIN_HEIGTH / 2 + 20))

            case 'inimigo1':
                return enemy('inimigo1', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGTH-40)))

            case 'inimigo2':
                return enemy('inimigo2', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGTH-40)))

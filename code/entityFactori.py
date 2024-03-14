#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.bacgraud import bacgraud
from const import WIN_WIDTH


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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rotacao
import unittest


def imprime_rotacao (rotacao):
    for pessoa in rotacao:
        print(pessoa[0], end=' - ')
        if pessoa[1]:
            print(pessoa[1], end=' - ')
        if pessoa[2]:
            print(pessoa[2], end='')
        print()


class Testa (unittest.TestCase):

    def testa_actualiza(self):
        rotacao = le_rotacao()
        lugares = le_lugares()
        ultima_actualizacao = date(2017, 9, 25)
        rotacao2 = actualiza(rotacao, lugares, ultima_actualizacao)
        self.assertNotEqual(rotacao, rotacao2)
        # imprime_rotacao(rotacao)
        # imprime_rotacao(rotacao)


if __name__ == "__main__":
    pass

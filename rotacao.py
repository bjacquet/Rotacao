#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2017 by Bruno Jacquet (bruno.jacquet@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from datetime import date       
from dateutil.relativedelta import relativedelta
from csv import reader

__ficheiro__ = 'dados/rotacao.csv'

def le_dados(ficheiro=__ficheiro__):
    rotacao = []
    with open(ficheiro) as dados:
        leitor = reader(dados, delimiter=',')
        for linha in leitor:
            rotacao.append(linha)
    return rotacao[1:]

def actual (rotacao):
    return rotacao[:4]

def actualiza (rotacao, ultima_actualizacao):
    if ultima_actualizacao.month == date.today().month and \
       ultima_actualizacao.year == date.today().year:
        return ultima_actualizacao
    for i in range(4):
        rotacao.append(rotacao.pop(0))
    ultima_actualizacao += relativedelta(months=1)
    return actualiza(rotacao, ultima_actualizacao)

def adiciona (rotacao, colaborador, mes=0):
    rotacao.append(colaborador)
    return rotacao

def remove (rotacao, colaborador, mes=0):
    rotacao.remove(colaborador)
    return rotacao

if __name__ == "__main__":
    rotacao = le_dados()
    ultima_actualizacao = date(2017, 9, 25)

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


__rotacao__ = 'dados/rotacao.csv'
__lugares__ = 'dados/lugares.csv'


def le_dados (ficheiro, parser):
    dados = []
    with open(ficheiro) as fd:
        leitor = reader(fd, delimiter=',')
        leitor.__next__()
        for linha in leitor:
            dados.append(parser(linha))
    return dados

def leitor_data (data):
    if data.isdigit():
        return date.fromordinal(int(data))
    else:
        return None

def leitor_pessoa (pessoa):
    nome  = pessoa[0]
    entrada = leitor_data(pessoa[1])
    saida   = leitor_data(pessoa[2])
    return [nome, entrada, saida]

def le_rotacao ():
    return le_dados(__rotacao__, leitor_pessoa)

def pessoa_entrada (pessoa):
    return pessoa[1] or 0

def leitor_lugar (lugar):
    return lugar[:2]

def le_lugares():
    return le_dados(__lugares__, leitor_lugar)

def num_lugares(lugares):
    return len(lugares)

def actual (rotacao, lugares):
    return rotacao[:num_lugares(lugares)]

def actualiza (rotacao, lugares, ultima_actualizacao):
    if ultima_actualizacao.month == date.today().month and \
       ultima_actualizacao.year == date.today().year:
        return ultima_actualizacao
    for i in range(num_lugares(lugares)):
        rotacao.append(rotacao.pop(0))
    ultima_actualizacao += relativedelta(months=1)
    rotacao = priotiriza(rotacao, ultima_actualizacao)
    return actualiza(rotacao, lugares, ultima_actualizacao)

def adiciona (rotacao, colaborador, mes=0):
    rotacao.append(colaborador)
    return rotacao

def priotiriza (rotacao, hoje=date.today()):
    """Estabelece a ordem na lista de rotação."""
    frente, mantem, tras = [], [], []
    for pessoa in rotacao:
        if pessoa[1] == None:
            mantem.append(pessoa)
        elif pessoa[1].month == hoje.month and pessoa[1].year == hoje.year:
            frente.append(pessoa)
        else:
            tras.append(pessoa)
    return frente + mantem + tras

def remove (rotacao, colaborador, mes=0):
    rotacao.remove(colaborador)
    return rotacao

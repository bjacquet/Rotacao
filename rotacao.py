#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 by Bruno Jacquet (bruno.jacquet@gmail.com)
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

from datetime import datetime        


__timekeeper__ = datetime(2013, 1, 25)


class Rotacao:
    def __init__ (self):
        self.rotacao = []
        self.ultima_actualizacao = 0

    def actual (self):
        return self.rotacao[:4]

    def actualiza (self):
        if self.ultima_actualizacao != __timekeeper__.today.month:
            for i in range(4):
                self.rotacao = self.rotacao.append(self.rotacao.pop(0))
            self.ultima_actualizacao = __timekeeper__.today().month
        return self.rotacao

    def adiciona (self, colaborador, mes=0):
        self.rotacao.append(colaborador)
        return self.rotacao

    def remove (self, colaborador, mes=0):
        self.rotacao.remove(colaborador)
        return self.rotacao

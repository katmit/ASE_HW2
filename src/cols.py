
import num
import sym
import row

import abc
import re
from enum import Enum

class ColTypeInterface:

    @abc.abstractclassmethod
    def add(value):
        pass

    @abc.abstractclassmethod
    def at(self) -> int:
        pass

    @abc.abstractclassmethod
    def txt(self) -> str:
        pass

class Cols:

    def __init__(self, t: list[str]):
        self.names = t
        self.all = []
        self.x = []
        self.y = []

        for n, s in enumerate(t):
            col = num.Num(n, s) if re.search("^[A-Z]+", s) != None else sym.Sym(n, s)
            self.all.append(col)
            if re.search("X$", s) is None:

                if(re.search("[!+-]$", s)):
                    self.y.append(col)
                else:
                    self.x.append(col)
                
    def add(self, row: row.Row):
        col: ColTypeInterface # declare that a col is of the ColTypeInterface type
        for col in all:
            col.add(row.cells[col.at()])



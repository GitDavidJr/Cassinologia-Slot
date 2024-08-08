from utils import random_slot
from dataclasses import dataclass, field
from typing import List


@dataclass
class Game:
    slots: List[List[str]]

    def girar_roleta(self):
        self.slots = [
            [random_slot(),random_slot(),random_slot()],
            [random_slot(),random_slot(),random_slot()],
            [random_slot(),random_slot(),random_slot()]
        ]

    def desenhar(self):
        for c in self.slots:
            print(c)
        

    def verificar(self):

        count_horizontal = 0
        #verificar horizotal
        for c in self.slots:
            if c[0] == c[1] == c[2]:
                print(f"horizontal {count_horizontal} ganhou")
                count_horizontal += 1

        count_vertical = 0
        #verificar vertical
        for c in range(3):
            if self.slots[0][c] == self.slots[1][c] == self.slots[2][c]:
                print(f"vertical {count_horizontal} ganhou")
                count_vertical += 1


        #verificar diagonal

        #decendo
        if self.slots[0][0] == self.slots[1][1] == self.slots[2][2]:
            print("diagonal ganhou")

        #subindo
        if self.slots[0][2] == self.slots[1][1] == self.slots[2][0]:
            print("diagonal ganhou")
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        atual = 0

        for valor in reversed(satisfaction):
            atual += valor
            if atual <= 0:
                break
            total += atual

        return total
from math import ceil
from collections import Counter


class Solution:
    def numRabbits(self, answers):
        if not answers:
            return 0
        return sum([(size+1)*int(ceil(rabbits/(size+1))) for size, rabbits in Counter(answers).items()])

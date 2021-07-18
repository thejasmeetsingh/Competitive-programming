import random
from collections import defaultdict


class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, n in enumerate(nums):
            self.indices[n].append(i)

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        idx = random.randrange(len(indices))
        return indices[idx]

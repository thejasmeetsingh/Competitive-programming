class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        return [[0 if val else 1 for val in B[::-1]] for B in A]
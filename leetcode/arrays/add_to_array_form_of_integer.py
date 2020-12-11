class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        return [el for el in str(int("".join(str(val) for val in A))+K)]
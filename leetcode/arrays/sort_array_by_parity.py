class Solution:
    def sortArrayByParity(self, A: list) -> list:
        if not A:
            return A

        A.sort(key=lambda x: x % 2)
        return A
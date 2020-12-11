class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        if not A:
            return A

        i = 0
        j = 1

        while j < len(A):
            if i % 2 != A[i] % 2:
                if i % 2 == A[j] % 2:
                    A[i], A[j] = A[j], A[i]
                    i += 2
                    j += 1
                    continue
                else:
                    j += 1
                    continue
            i += 1
            j += 1

        return A
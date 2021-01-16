class Solution:
    def canFormArray(self, arr: list, pieces: list) -> bool:
        if not arr or not pieces:
            return False

        for i in pieces:
            try:
                pos = arr.index(i[0])
            except ValueError:
                return False
            if arr[pos:pos + len(i)] != i:
                return False
        return True

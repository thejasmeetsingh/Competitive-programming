from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list):
        if not arr:
            return True

        counter = Counter(arr)
        arr.sort(key=abs)

        for el in arr:
            if counter[el] == 0:
                continue
            if counter[2 * el] == 0:
                return False

            counter[el] -= 1
            counter[2 * el] -= 1

        return True

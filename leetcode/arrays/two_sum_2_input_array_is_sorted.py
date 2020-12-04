class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        if not numbers:
            return []

        d = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in d:
                return [d[target - numbers[i]], i + 1]
            d[numbers[i]] = i + 1
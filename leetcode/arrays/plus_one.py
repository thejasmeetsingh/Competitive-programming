class Solution:
    def plusOne(self, digits: list) -> list:
        return list(map(int, str(int(''.join(map(str, digits))) + 1).zfill(len(digits))))

class Solution:
    def __init__(self):
        self.d = dict()

    def calculate(self, val):
        if int(val) not in self.d:
            self.d[int(val)] = int(val) ** 2
        return self.d[int(val)]

    def isHappy(self, n: int) -> bool:
        if n in {0, 2, 4, 5, 3}:
            return False

        if n in {1, 100, 19}:
            return True

        while n != 1:
            n = sum(list(map(lambda i: self.calculate(i), str(n))))
            if n == 4:
                return False
        return True
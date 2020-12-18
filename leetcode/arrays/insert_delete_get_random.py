from random import choice


class RandomizedSet:

    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        else:
            self._set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(list(self._set))
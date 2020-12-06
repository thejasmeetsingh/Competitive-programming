class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if not flowerbed:
            return False

        k = len(flowerbed)
        last = False

        for idx, el in enumerate(flowerbed):
            can_plant = False
            if not el and not last:
                can_plant = True

                if idx > 0 and flowerbed[idx-1]:
                    can_plant = False
                if idx < (k-1) and flowerbed[idx+1]:
                    can_plant = False

                if can_plant:
                    n -= 1
                    if n < 0:
                        break
            last = can_plant

        return n < 1
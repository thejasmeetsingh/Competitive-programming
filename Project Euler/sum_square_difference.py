if __name__ == "__main__":
    limit = 100
    _sum = limit * (limit + 1) // 2
    _sum_sq = (2 * limit + 1) * (limit + 1) * limit // 6
    print(_sum ** 2 - _sum_sq)
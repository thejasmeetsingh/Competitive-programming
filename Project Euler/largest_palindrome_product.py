if __name__ == "__main__":
    _max = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                _max = max(_max, product)

    print(_max)
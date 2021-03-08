if __name__ == '__main__':
    num = 1000000
    _max = [0, 0]
    d = dict()

    while num > 13:
        n = num
        count = 1

        if n in d:
            count = d[n]

        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3*n+1
            count += 1

            if n == 1:
                break

        d[n] = count
        if count > _max[1]:
            _max = [num, count]
        num -= 1

    print(_max[0])

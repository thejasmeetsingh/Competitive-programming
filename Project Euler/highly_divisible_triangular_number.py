def get_number_divisors(num):
    _n = num
    i = 2
    p = 1

    if num == 1:
        return 1

    while (i * i) <= _n:
        count = 1
        while _n % i == 0:
            _n //= i
            count += 1
        i += 1
        p *= count

    if _n == num or _n > 1:
        p *= 1 + 1

    return p


if __name__ == "__main__":
    target = 500
    n = 1
    d = 1

    while get_number_divisors(d) <= target:
        n += 1
        d += n

    print(d)

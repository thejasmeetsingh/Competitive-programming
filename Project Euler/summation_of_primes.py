def is_prime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0

    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6

    return 1


if __name__ == "__main__":
    n = 2000000
    _sum = 17

    for i in range(11, n+1):
        if is_prime(i):
            _sum += i

    print(_sum)

def number_of_strings(_n):
    result = 0
    result1 = 99
    result2 = 10
    if _n == 1:
        return result2
    if _n == 2:
        return result1
    for i in range(3, _n + 1):
        result = 10*result1 - result2
        result2 = result1
        result1 = result
    return result


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        print(number_of_strings(n) % 1000000009)

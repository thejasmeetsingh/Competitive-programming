from math import factorial

if __name__ == '__main__':
    n = 100
    fact = factorial(n)
    print(sum(map(int, str(fact))))
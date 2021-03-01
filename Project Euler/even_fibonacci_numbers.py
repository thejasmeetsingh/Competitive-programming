if __name__ == '__main__':
    n = 4000000
    _sum = 44
    a = 144
    b = 233

    while b < n:
        _sum += a if a % 2 == 0 else 0
        c = a
        a = b
        b = c + b
    
    _sum += a if a % 2 == 0 else 0
    print(_sum)
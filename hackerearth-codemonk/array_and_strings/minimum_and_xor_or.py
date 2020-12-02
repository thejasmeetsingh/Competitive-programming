from sys import maxsize

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = sorted(map(int, input().split()))
        _min = maxsize

        for i in range(n-1):
            _min = min(_min, arr[i] ^ arr[i+1])

        print(_min)
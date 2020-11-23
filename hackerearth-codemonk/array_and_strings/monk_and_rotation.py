if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, k = list(map(int, input().split()))
        arr = list(map(str, input().split()))
        x = k % n
        print(*(arr[n-x:] + arr[:n-x]))

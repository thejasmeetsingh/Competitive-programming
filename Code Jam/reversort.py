if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        total = 0

        for i in range(n-1):
            j = arr.index(min(arr[i:]))
            arr = arr[:i] + list(reversed(arr[i:j+1])) + arr[j+1:]
            total += j - i + 1

        print(f"Case #{_+1}: {total}")

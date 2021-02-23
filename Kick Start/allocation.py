if __name__ == '__main__':
    T = int(input())

    for _ in range(1, T+1):
        n, b = list(map(int, input().split()))
        arr = sorted(map(int, input().split()))
        count = 0
        for el in arr:
            if b >= el:
                count += 1
                b -= el
            else:
                break
        print(f"Case #{_}: {count}")
def mandragora(arr: list, n: int):
    if not arr:
        return 0
    
    if n == 1:
        return arr[0]
    
    arr.sort()
    _sum = sum(arr)
    max_p = 0

    for i in range(n):
        _sum -= arr[i]
        result = _sum * (i + 2)
        if result < max_p:
            return max_p
        else:
            max_p = result


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        H = list(map(int, input().rstrip().split()))
        result = mandragora(H, n)
        print(result)

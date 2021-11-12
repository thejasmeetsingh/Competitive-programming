def unboundedKnapsack(k: int, arr: list):
    dp = [False] * (k + 1)
    dp[0] = True
    _max = 0
    
    for el in arr:
        for i in range(el, len(dp)):
            dp[i] |= dp[i - el]
            if dp[i]:
                _max = max(i, _max)
            
    return _max
    

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        print(result)

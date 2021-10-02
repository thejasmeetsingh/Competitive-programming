def balancedSums(arr):
    _sum = sum(arr)
    left_sum = 0
    
    for el in arr:
        if 2 * left_sum == _sum - el:
            return "YES"
        else:
            left_sum += el
    
    return "NO"
    

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)

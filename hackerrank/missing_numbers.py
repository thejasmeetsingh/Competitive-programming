from collections import Counter
from bisect import insort


def missingNumbers(arr, brr):
    arr_counter = Counter(arr)
    brr_counter = Counter(brr)
    result = list()
    
    for brr_count in brr_counter:
        if (brr_count not in arr_counter) or (brr_count in arr_counter and brr_counter[brr_count] - arr_counter[brr_count] != 0):
            result.append(brr_count)
    
    result.sort()
    return result
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))

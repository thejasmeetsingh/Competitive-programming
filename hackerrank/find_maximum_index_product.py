def solve(arr, n):
    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and (arr[stack[-1]] < arr[i]):
            right[stack.pop()] = i + 1
        stack.append(i)

    stack = []
    for i in range(n):
        while stack and (arr[stack[-1]] < arr[n - 1 - i]):
            left[stack.pop()] = n - i
        stack.append(n - 1 - i)

    ans = 0
    for i in range(n):
        ans = max(ans, left[i] * right[i])

    return ans


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr, arr_count)

    print(result)

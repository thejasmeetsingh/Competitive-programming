def solve(t):
    arr = [0] * len(t)

    for i in range(len(t)):
        val = t[i]

        if val == 0 or val >= len(t) - 1:
            continue

        i1 = i - val + 1
        i2 = i + 1

        if i1 < 0:
            i1 += len(t)

        if i2 >= len(t):
            i2 -= len(t)

        arr[i1] -= 1
        arr[i2] += 1

    result, mv, temp = 0, 0, 0

    for i in range(len(t)):
        temp += arr[i]
        if i == 0 or temp > mv:
            result = i
            mv = temp

    return result + 1


if __name__ == '__main__':
    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    print(solve(t))

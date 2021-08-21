def calc(value):
    return value * (value - 1)


def solve(_arr):
    counter = dict()
    stack = []
    result = 0

    for val in _arr:
        while stack and val > stack[-1]:
            removed_item = stack.pop()
            result += calc(counter[removed_item])
            del counter[removed_item]

        if counter.get(val):
            counter[val] += 1
        else:
            counter[val] = 1
            stack.append(val)

    while stack:
        removed_item = stack.pop()
        result += calc(counter[removed_item])
        del counter[removed_item]

    return result


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(solve(arr))

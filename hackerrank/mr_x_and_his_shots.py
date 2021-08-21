from bisect import bisect_left, bisect_right


def solve(_a, _b, _c, _d):
    return sum(bisect_right(_c, v) for v in _b) - sum(bisect_left(_d, u) for u in _a)


if __name__ == '__main__':
    (a, b), (c, d) = (zip(*(map(int, input().split()) for _ in range(k))) for k in map(int, input().split()))
    print(solve(a, b, sorted(c), sorted(d)))

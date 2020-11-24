def update(_l, r, val, bit, N):
    i = _l
    while i <= N:
        j = r
        while j <= N:
            bit[i][j] += val
            j += j & -j
        i += i & -i


def query(_l, r, bit):
    ret = 0
    i = _l
    while i > 0:
        j = r
        while j > 0:
            ret += bit[i][j]
            j -= j & -j
        i -= i & -i

    return ret


def countInversionPairs(mat, N):
    bit = [[0 for i in range(N + 1)] for j in range(N + 1)]
    v = []

    for i in range(N):
        for j in range(N):
            v.append([-mat[i][j], [i + 1, j + 1]])
    v.sort()
    inv_pair_cnt = 0
    i = 0
    while i < len(v):

        curr = i
        pairs = []
        while curr < len(v) and (v[curr][0] == v[i][0]):
            pairs.append([v[curr][1][0], v[curr][1][1]])
            inv_pair_cnt += query(v[curr][1][0], v[curr][1][1], bit)
            curr += 1

        for it in pairs:
            x = it[0]
            y = it[1]
            update(x, y, 1, bit, N)
        i = curr

    return inv_pair_cnt


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [list(map(int, input().split())) for __ in range(n)]
        count = countInversionPairs(arr, n)
        print(count)

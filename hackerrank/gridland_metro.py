from collections import defaultdict


def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

def gridlandMetro(n, m, k, tracks):
    total_blocks = n * m

    for _, value in tracks.items():
        blocks_aquired = sum(map(lambda x: (x[1] - x[0]) + 1, value))
        if total_blocks - blocks_aquired <= 0:
            return 0
        total_blocks -= blocks_aquired

    return total_blocks
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    track = defaultdict(list)

    for _ in range(k):
        r, c1, c2 = list(map(int, input().rstrip().split()))
        track[r].append([c1, c2])
        track[r] = merge(track[r])

    result = gridlandMetro(n, m, k, track)

    print(str(result) + '\n')

if __name__ == "__main__":
    T = int(input())

    for _ in range(1, T+1):
        n = int(input())
        intervals = sorted([list(map(int, input().split())) for __ in range(n)], key=lambda x: x[0])

        if len(intervals) == 0:
            print(f"Case #{_}: IMPOSSIBLE")
            continue

        if len(intervals) == 1:
            print(f"Case #{_}: C")
            continue

        cameron_activity_last_interval = intervals[0][-1]
        jamie_activity_last_interval = intervals[1][-1]
        result = "CJ"

        for idx in range(2, len(intervals)):
            if cameron_activity_last_interval <= intervals[idx][0]:
                cameron_activity_last_interval = intervals[idx][1]
                result += "C"
            elif jamie_activity_last_interval <= intervals[idx][0]:
                jamie_activity_last_interval = intervals[idx][1]
                result += "J"
            else:
                result = 'IMPOSSIBLE'
                break
        
        print(f"Case #{_}: {result}")
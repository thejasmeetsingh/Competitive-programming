def get_cost(data: list):
    cost = 0

    for j in range(n - 1):
        sub_str = data[j] + data[j + 1]
        if sub_str == 'CJ':
            cost += x
        elif sub_str == 'JC':
            cost += y

    return cost


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        x, y, string = input().split()
        x = int(x)
        y = int(y)
        string = list(string)
        n = len(string)

        if len(string) == 1:
            print(f"Case #{_ + 1}: {0}")
            continue

        if 'C' not in string and string.count('J') == 1:
            print(f"Case #{_ + 1}: {0}")
            continue
        elif 'J' not in string and string.count('C') == 1:
            print(f"Case #{_ + 1}: {0}")
            continue

        if '?' in string:
            if x < y:
                insert = 'C'
            else:
                insert = 'J'

            for i in range(n):
                if string[i] == '?':
                    if i == 0:
                        string[i] = insert
                    else:
                        string[i] = string[i-1]

        print(f"Case #{_ + 1}: {get_cost(string)}")
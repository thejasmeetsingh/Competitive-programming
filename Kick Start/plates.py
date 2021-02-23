if __name__ == "__main__":
    T = int(input())

    for _ in range(1, T+1):
        n, k, p = list(map(int, input().split()))
        stacks = [list(map(int, input().split())) for __ in range(n)]
        prefixs = list()
        global_maximum = -1

        for i in range(n):
            temp = stacks[i]
            for j in range(1, len(temp)):
                temp[j] = temp[j] + temp[j-1]
            prefixs.append(temp)
        

        for i in range(n-1):
            for j in range(k):
                local_maximum = -1
                for l in range(i+1, n):
                    local_maximum = max(local_maximum, prefixs[i][j] + prefixs[l][k-j-1])
                global_maximum = max(global_maximum, local_maximum)
        
        print(f"Case #{_}: {global_maximum}")
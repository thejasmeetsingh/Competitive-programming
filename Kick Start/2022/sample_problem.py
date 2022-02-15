if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        N, M = list(map(int, input().split()))
        C = list(map(int, input().split()))
        
        total_candies = sum(C)
        max_candy_per_kid = M * int(total_candies / M)
        result = (total_candies - max_candy_per_kid) if total_candies >= \
        max_candy_per_kid else (max_candy_per_kid - total_candies)
        
        print(f"Case #{_ + 1}: {result}")

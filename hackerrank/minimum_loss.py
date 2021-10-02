def minimumLoss(price):
    sorted_prices = sorted(price.keys())
    min_cost = sorted_prices[-1]
    
    for idx in range(len(sorted_prices)-1):
        if price[sorted_prices[idx + 1]] < price[sorted_prices[idx]]:
            min_cost = min(min_cost, sorted_prices[idx + 1] - sorted_prices[idx])
    
    return min_cost


if __name__ == '__main__':
    n = int(input().strip())
    
    price = list(map(int, input().rstrip().split()))

    result = minimumLoss({price[idx]: idx for idx in range(len(price))})

    print(result)

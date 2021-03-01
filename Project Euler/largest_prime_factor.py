if __name__ == "__main__":
    num = 13195   
    n = int(num ** 0.5)
    result = []

    for i in range(2, n+1):
        if num % i == 0:
            result.append(i)
            if (i * i) != num:
                result.append(num // i)
    
    result.sort()
    print(result)
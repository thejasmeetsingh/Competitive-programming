if __name__ == "__main__":
    n = 1000
    for i in range(1, 333):
        for j in range(i+1, 500):
            k = n - i - j
            if (i**2) + (j**2) == (k**2):
                print(i*j*k)
                exit(0)

if __name__ == '__main__':
    num, count = 20, 1

    for i in range(1, num+1):
        count = count * (num + i) // i

    print(count)
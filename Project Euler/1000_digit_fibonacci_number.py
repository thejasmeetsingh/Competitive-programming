if __name__ == '__main__':
    fibonacci_numbers = [1, 1]

    while len(str(fibonacci_numbers[-1])) < 1000:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        if len(str(fibonacci_numbers[-1])) == 1000:
            print(len(fibonacci_numbers))
            exit(0)

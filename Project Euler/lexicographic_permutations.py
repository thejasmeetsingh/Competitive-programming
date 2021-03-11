from itertools import permutations, islice

if __name__ == '__main__':
    target = 1000000
    range_limit = 10
    digit_permutations = permutations(range(range_limit))
    digits = next(islice(digit_permutations, target - 1, target))
    answer = sum([digit * 10 ** (range_limit - 1 - i) for i, digit in enumerate(digits)])
    print(answer)

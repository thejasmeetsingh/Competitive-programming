def find_divisors(num):
    potential_divisor = 1
    list_of_divisor = []
    while potential_divisor < num:
        if num % potential_divisor == 0:
            list_of_divisor.append(potential_divisor)
        potential_divisor += 1
    return list_of_divisor


if __name__ == '__main__':
    limit = 10000
    n = 1
    result = 0

    while n < limit:
        list_of_divisors_of_number = find_divisors(n)
        sum_of_divisors_of_number = sum(list_of_divisors_of_number)
        list_of_divisors_of_new_number = find_divisors(sum_of_divisors_of_number)
        sum_of_divisors_of_new_number = sum(list_of_divisors_of_new_number)

        if sum_of_divisors_of_new_number == n and sum_of_divisors_of_number < limit and n < limit and \
                n < sum_of_divisors_of_number:
            result += n + sum_of_divisors_of_number
        n += 1

    print(result)
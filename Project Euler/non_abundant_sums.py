def sieve_of_eratosthenes(num):
    prime = [True] * (num + 1)
    p = 2
    while p * p <= num:
        if prime[p] is True:
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    return [_i for _i in range(num+1) if prime[_i]]


def sum_of_factors_prime(num, primes):
    number, _sum, p, i = num, 1, primes[0], 0

    while p * p <= number and i < len(primes):
        p = primes[i]
        i += 1
        if number % p == 0:
            j = p * p
            number //= p

            while number % p == 0:
                j = j * p
                number //= p

            _sum += (j-1) // (p-1)

    return _sum - number


if __name__ == '__main__':
    limit = 28123
    sum_divisors = sieve_of_eratosthenes(limit)

    abundant_subspace = list()
    answer = 0
    for n in range(2, limit + 1):
        if sum_of_factors_prime(n, sum_divisors) > n:
            abundant_subspace.append(n)

    abundant_numbers = [False] * (limit + 1)
    for i in range(len(abundant_subspace)):
        for j in range(i, len(abundant_subspace)):
            if abundant_subspace[i] + abundant_subspace[j] <= limit:
                abundant_numbers[abundant_subspace[i] + abundant_subspace[j]] = True
            else:
                break

    for i in range(1, limit + 1):
        if not abundant_numbers[i]:
            answer += i

    print(answer)

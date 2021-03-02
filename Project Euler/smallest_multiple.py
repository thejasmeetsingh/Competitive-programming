from functools import reduce


def lcm(*values):
    values = sorted(values)
    if values:
        n = values[-1]
        m = n
        values.remove(n)
        while any(n % value for value in values):
            n += m
        return n
    return 0


print(reduce(lcm, range(1, 21)))

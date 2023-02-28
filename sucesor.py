n = int(input())


def successor(number):

    rationals = []
    results = []

    for i in range(1, number + 1):

        rationals.append(f'\ufe68frac \u007b1\u007d \u007b10{i}\u007d')
        results.append(1/(10**i))

    return rationals, results


print(successor(n))

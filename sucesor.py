n = int(input())

def sucesor(N):

    rationals = []
    results = []

    for i in range (1, N + 1):
        rationals.append(f'1/10^{i}')
        results.append(1/(10**i))

    return rationals, results

print(sucesor(n))





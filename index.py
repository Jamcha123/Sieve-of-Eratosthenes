targets = [int(i) for i in range(2, 12)]

def func1(targets):
    return targets

notPrimes = []
for x in range(len(targets)):
    if targets[x] not in notPrimes:
        for y in range(len(targets)):
            if targets[y] % targets[x] == 0 and x != y and targets[y] not in notPrimes:
                notPrimes.append(targets[y])
primes = []
for x in range(len(targets)):
    if targets[x] not in notPrimes:
        primes.append(targets[x])
print("prime numbers are ", end="")
print(list(map(func1, primes)))

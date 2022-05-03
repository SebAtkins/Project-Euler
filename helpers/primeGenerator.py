import json

primes = [2]

for x in range(3, 1000000):
    prime = True
    for i in primes:
        if x % i == 0:
            prime = False
        if not prime:
            break
    if prime:
        primes.append(x)

with open('primes.json', 'w') as f:
    json.dump(primes, f)
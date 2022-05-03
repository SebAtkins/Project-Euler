primes = [2]

for x in range(3, 100000):
    prime = True
    for i in primes:
        if x % i == 0:
            prime = False
        if not prime:
            break
    if prime:
        primes.append(x)

primes = primes[::-1]

for x in primes:
    if 600851475143 % x == 0:
        print(x)
        break
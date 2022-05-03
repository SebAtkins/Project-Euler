import json

with open('primes.json', 'r') as f:
    primes = json.load(f)

for i in primes:
    print(i)
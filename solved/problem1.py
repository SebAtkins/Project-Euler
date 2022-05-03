total = 0

for x in range(1000):
    total = total + x if x % 3 == 0 or x % 5 == 0 else total

print(total)
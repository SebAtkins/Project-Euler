total = 2

prev = 1
current = 2

while current < 4000000:
    prev, current = current, prev + current

    total = total + current if current % 2 == 0 else total

print(total)
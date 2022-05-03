largest = 0

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        largest = i * j if str(i * j) == str(i * j)[::-1] and i * j > largest else largest

print(largest)
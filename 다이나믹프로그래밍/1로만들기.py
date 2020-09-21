n = int(input())
count = 0
while n != 1:
    if n % 5 == 0:
        n = n//5
        count += 1
        continue
    elif n % 3 == 0:
        n = n//3
        count += 1
        continue
    elif n % 3 != 0 and n % 5 != 0:
        n -= 1
        count += 1
        continue

print(count)

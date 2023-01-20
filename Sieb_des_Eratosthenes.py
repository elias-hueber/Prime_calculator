prime = []
x = 0
y = 2
result = 0
end = 1000
target = 100
for i in range(2, end + 1):
    prime.append(i)
while True:
    while result <= end:
        result = prime[x] * y
        y += 1
        if result in set(prime):
            prime.remove(result)
    if prime[x] * prime[x] > end:
        break
    x += 1
    y = 2
    result = 0

print(prime[target - 1])

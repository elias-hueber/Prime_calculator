prime = []
x = 0
y = 2
result = 0
for i in range(2, 1001):
    prime.append(i)
while True:
    while result <= 1000:
        result = prime[x] * y
        y += 1
        if result in set(prime):
            prime.remove(result)
    if prime[x] * prime[x] > 1000:
        break
    x += 1
    y = 2
    result = 0

print(prime[99])

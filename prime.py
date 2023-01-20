prime = []
x = 2
y = 1
end = 100
result = 100
while len(prime) <= end - 1:
    while x != y:
        if y == x - 1:
            prime.append(x)
        if x % y == 0:
            y = x
        else:
            y += 1
    x += 1
    y = 2
print(prime[result - 1])

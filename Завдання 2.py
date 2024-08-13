N = 30
S = 0
c = 0

for i in range(1, N + 1):
    S += 1 / i
    c += 1

print("Сума :", S)
print("Кількість всіх членів ряду:", c)
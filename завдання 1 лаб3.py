t = str(input("Введіть слово: "))

while len(t) < 3:
    t = str(input("Введіть слово, довжина якого не менше трьох символів: "))

print("Три останні символи рядка: ", t[-3:])
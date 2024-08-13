a = int(input ("Введіть число a: "))

while (a < 1 or a > 100):

    a = int(input ("Введіть ще раз число а: "))

b = int(input ("Введіть число b: "))

while (b < 1 or b > 100):

    b = int(input ("Введіть ще раз число b: "))

if a > b:

    r = (a / b + 1)

elif a == b:

    r = -2

else:

    r = (a - b) / a

print("Результат обчислення: " , r)
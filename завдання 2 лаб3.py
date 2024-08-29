word = str(input("Введiть слово: "))

underlining = 0

for char in word:
    if char == '_':
        underlining += 1

print("Кількість символів «_» у слові: ", underlining)

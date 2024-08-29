sentence = str(input("Введіть речення: "))

words = sentence.split()

each_words = set(words)

print("Виведення кожного слова ", each_words)
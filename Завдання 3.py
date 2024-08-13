N = int(input("введіть ціле число N (1 < N < 9): "))
if N <= 1 or N >= 9:
    print("число не попадає в діапазон")
else:
    for i in range(N, 0, -1):
        for j in range(N, N - i, -1):
            print(j, end=' ')
        print()
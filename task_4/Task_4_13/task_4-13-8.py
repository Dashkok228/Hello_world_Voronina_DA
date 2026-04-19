n = int(input("Введите размер массива n: "))
A = []
for _ in range(n):
    A.append(int(input("Введите элемент массива: ")))
i = 0
count = 0
while i < n:
    if A[i] > 0:
        count = count + 1
    i = i + 1
print(count)

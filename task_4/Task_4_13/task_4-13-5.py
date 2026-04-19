N = int(input("Введите число N: "))
x = int(input("Введите первое число x: "))
max = x
i = 2
while i <= N:
    x = int(input(f"Введите число x ({i}-е число): "))
    if x > max:
        max = x
    i = i + 1
print("Максимальное значение:", max)
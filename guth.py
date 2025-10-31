1.1
numbers = [31, 18, 79]
print(*numbers)
1.2
numbers = [47, 52, 150]
print(*numbers)
1.3
numbers = [50, 20]
for num in numbers:
    print(num)
1.4
numbers = [5, 10, 21]
for num in numbers:
    print(num)
1.5
numbers = [1, 2]
for num in numbers:
    print(num)
1.6
pi = 3.1415926
print(f"{pi:.3f}")
1.7
e = 2.71828
print(round(e, 1))
1.8
num = input("Введите число: ")
print("Вы ввели число", num)
1.9
num = input("Введите число: ")
print(num, "- вот какое число Вы ввели")
1.10
name = input("Введите ваше имя: ")
print(name)
1.11
team = input("Введите название футбольной команды: ")
print(team, "- это чемпион!")
1.12
name = input("Введите имя: ")
print(f"Привет, {name}!")
1.13
num = int(input("Введите целое число: "))
next_num = num + 1
prev_num = num - 1
print(f"Следующее за числом {num} число - {next_num}.")
print(f"Для числа {num} предыдущее число - {prev_num}.")
1.14
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
num3 = input("Введите третье число: ")
print(num1, num2, num3, sep="  ")
1.15
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
num3 = input("Введите третье число: ")
num4 = input("Введите четвёртое число: ")
print(num1, num2, num3, num4, sep=" ")
1.16
t = int(input("Введите число №1: "))
v = int(input("Введите число №2: "))
x = int(input("Введите число №3: "))
y = int(input("Введите число №4: "))
print(f'а) 5 10 \t б) 100 {t}\tв) {x} 25')
print(f'   7 см \t    1949 {v} \t   {x} {y}')
1.17
a = int(input("Введите число №1: "))
b = int(input("Введите число №2: "))
x = int(input("Введите число №3: "))
y = int(input("Введите число №4: "))
print(f'а) 2 кг \t б) {a} 1 \t в) {x} {y}')
print(f'   13 17 \t    19 {b} \t    5 {y}')


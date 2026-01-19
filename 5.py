# 5.1
for i in range(9):
    print("20", end=" ")
print("20")

# 5.2
num = 25
count = 7
for i in range(count):
    print(num, end=" ")
print()

# 5.3
for i in range(20, 36):
    print(i)

a = 40
for i in range(a, 51):
    print(i**2)

b = 15
for i in range(10, b+1):
    print(i**3)

a = 5
b = 12
for i in range(a, b+1):
    print(i)

# 5.4
for i in range(10, 26):
    print(f"{i} {i}.4")
for i in range(25, 36):
    print(f"{i} {i}.5 {i-0.2}")

# 5.5
for i in range(21, 9, -1):
    print(f"{i} {i-1.8}")
for i in range(45, 24, -1):
    print(f"{i} {i-0.5} {i-0.8}")

# 5.6
for i in range(21, 36):
    print(f"{i} {i-0.6}")
for i in range(16, 25):
    print(f"{i} {i-0.5} {i+0.8}")

# 5.7
price = 20.4
for i in range(2, 21):
    cost = i * price
    print(f"{i} - {cost:.1f} руб.")

# 5.8
print("Фунты    Кг")
for pounds in range(1, 11):
    kg = pounds * 0.453
    print(f"{pounds}    {kg:.3f}")

# 5.9
print("Дюймы    См")
for inches in range(10, 23):
    cm = inches * 2.54
    print(f"{inches}    {cm:.1f}")

# 5.10
exchange_rate = 75.5
for dollars in range(1, 21):
    rubles = dollars * exchange_rate
    print(f"{dollars} - {rubles:.2f} руб.")

# 5.11
import math
R = 6350
for h in range(1, 11):
    d = math.sqrt((R + h)**2 - R**2)
    print(f"{h} км - {d:.2f} км")

# 5.12
import math
p0 = 1.29
z = 1.25e-4
print("Высота (м)   Плотность (кг/м³)")
for h in range(0, 1100, 100):
    p = p0 * math.exp(-h * z)
    print(f"{h}           {p:.4f}")

# 5.13
for i in range(1, 10):
    print(f"{i} × 7 = {i*7}")

# 5.14
for i in range(1, 10):
    print(f"9 × {i} = {9*i}")

# 5.15
n = 6
for i in range(1, 10):
    print(f"{i} × {n} = {i*n}")

# 5.16
import math
for i in range(2, 16):
    print(f"sin({i}) = {math.sin(i):.4f}")

# 5.17
for x in range(4, 29):
    t = x + 3
    y = 3*t**2 + 4.87*t - 3
    print(f"x={x}, y={y:.2f}")

# 5.18
for a in range(2, 18):
    t = 3*a
    z = 4.3*t**2 - 8*t + 13
    print(f"a={a}, z={z:.2f}")

# 5.19
import math
x = 0.1
while x <= 1.5:
    print(f"sin({x:.1f}) = {math.sin(x):.4f}")
    x += 0.1

# 5.20
import math
x = 0.1
while x < 1.0:
    print(f"√{x:.1f} = {math.sqrt(x):.4f}")
    x += 0.1

# 5.21
price_per_kg = 800
for weight in range(50, 1050, 50):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight} г - {cost:.2f} руб.")

# 5.22
price_per_kg = 600
for weight in range(100, 2100, 100):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight} г - {cost:.2f} руб.")

# 5.23
x = 2.1
while x <= 2.8:
    print(f"{x:.1f}")
    x += 0.1

# 5.24
x = 3.2
while x <= 3.9:
    print(f"{x:.1f}")
    x += 0.1

# 5.25
x = 2.2
while x <= 4.2:
    print(f"{x:.1f}")
    x += 0.2

# 5.26
x = 4.4
while x <= 6.4:
    print(f"{x:.1f}")
    x += 0.2

# 5.27
total = 0
for i in range(200, 601):
    total += i
print(f"Сумма от 200 до 600: {total}")

a = 300
total = 0
for i in range(a, 401):
    total += i
print(f"Сумма от {a} до 400: {total}")

b = 10
total = 0
for i in range(-15, b+1):
    total += i
print(f"Сумма от -15 до {b}: {total}")

a = 5
b = 15
total = 0
for i in range(a, b+1):
    total += i
print(f"Сумма от {a} до {b}: {total}")

# 5.28
product = 1
for i in range(7, 15):
    product *= i
print(f"Произведение от 7 до 14: {product}")

a = 5
product = 1
for i in range(a, 16):
    product *= i
print(f"Произведение от {a} до 15: {product}")

b = 8
product = 1
for i in range(1, b+1):
    product *= i
print(f"Произведение от 1 до {b}: {product}")

a = 3
b = 7
product = 1
for i in range(a, b+1):
    product *= i
print(f"Произведение от {a} до {b}: {product}")

# 5.29
total = 0
count = 0
for i in range(1, 751):
    total += i
    count += 1
average = total / count
print(f"Среднее от 1 до 750: {average:.2f}")

b = 200
total = 0
count = 0
for i in range(150, b+1):
    total += i
    count += 1
average = total / count
print(f"Среднее от 150 до {b}: {average:.2f}")

a = 180
total = 0
count = 0
for i in range(a, 201):
    total += i
    count += 1
average = total / count
print(f"Среднее от {a} до 200: {average:.2f}")

a = 10
b = 20
total = 0
count = 0
for i in range(a, b+1):
    total += i
    count += 1
    average = total / count
print(f"Среднее от {a} до {b}: {average:.2f}")

# 5.30
total = 0
for i in range(25, 41):
    total += i**3
print(f"Сумма кубов от 25 до 40: {total}")

a = 40
total = 0
for i in range(a, 51):
    total += i**2
print(f"Сумма квадратов от {a} до 50: {total}")

n = 10
total = 0
for i in range(1, n+1):
    total += i**2
print(f"Сумма квадратов от 1 до {n}: {total}")

a = 5
b = 10
total = 0
for i in range(a, b+1):
    total += i**2
print(f"Сумма квадратов от {a} до {b}: {total}")
# 5.31
n = 5
total = 0
for i in range(n, 2*n + 1):
    total += i**2
print(total)

# 5.32
n = 10
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total)

# 5.33
total = 0
for i in range(2, 11):
    total += i / (i + 1)
print(total)

# 5.34
n = 10
total = 0
for i in range(1, n + 1):
    total += i**2
print(total)

# 5.35
n = 8
total = 0
for i in range(1, n):
    total += i * (i + 1)
print(total)

# 5.36
total = 1
term = 1
for i in range(1, 9):
    term /= 3
    total += term
print(total)

# 5.37
n = 10
total = 0
sign = 1
for i in range(1, n + 1):
    total += sign / i
    sign = -sign
print(total)

# 5.38
x = 2
total = 0
power = x
for i in range(1, 12, 2):
    total += power / i
    power *= x * x
print(total)

# 5.39
x = 2
total = 1
sign = -1
power = 1
for i in range(2, 12):
    power *= x
    term = (i / (i + 1)) * power * sign
    total += term
    sign = -sign
print(total)

# 5.40
num = 123456789
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)

# 5.41
num = 123456
n = 3
product = 1
total = 0
for i in range(n):
    digit = num % 10
    product *= digit
    total += digit
    num //= 10
print(f"Произведение: {product}, Сумма: {total}")

# 5.42
N = 100
position = 0
sign = 1
total_path = 0
for i in range(1, N + 1):
    step = 1 / i
    position += sign * step
    total_path += step
    sign = -sign
print(f"Положение: {position:.4f}")
print(f"Общий путь: {total_path:.4f}")

# 5.43
n = 5
a = [1]
for k in range(1, n + 1):
    a_k = k * a[k-1] + 1/k
    a.append(a_k)
print(a)

# 5.44
n = 10
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"n-й член: {fib[n-1]}")
print(f"Первые n членов: {fib}")

# 5.45
fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
for i in range(2, 10):
    print(f"Член {i+1}: {fib[i]}")

# 5.46
k = 8
numerators = [1, 2]
denominators = [1, 1]
for i in range(2, k):
    numerators.append(numerators[i-1] + numerators[i-2])
    denominators.append(denominators[i-1] + denominators[i-2])
print(f"k-й член: {numerators[k-1]}/{denominators[k-1]}")

n = 6
numerators = [1, 2]
denominators = [1, 1]
for i in range(2, n):
    numerators.append(numerators[i-1] + numerators[i-2])
    denominators.append(denominators[i-1] + denominators[i-2])
for i in range(n):
    print(f"{numerators[i]}/{denominators[i]}")

# 5.47
n = 8
v = [0, 0, 1.5]
for i in range(4, n + 1):
    v_i = ((i - 1) / (i**2 + 1)) * v[i-2] - v[i-3] + v[i-4]
    v.append(v_i)
print(f"v_{n} = {v[n-1]}")

# 5.48
cells = 1
for hours in range(3, 25, 3):
    cells *= 2
    print(f"Через {hours} часов: {cells} клеток")

# 5.49
deposit = 1000
rate = 0.02
for month in range(1, 11):
    increase = deposit * rate
    deposit += increase
    print(f"Месяц {month}: прирост {increase:.2f} руб.")

deposit = 1000
for month in range(1, 13):
    deposit *= 1.02
    if month >= 3:
        print(f"Месяц {month}: {deposit:.2f} руб.")

# 5.50
distance = 10
for day in range(2, 11):
    distance *= 1.1
    print(f"День {day}: {distance:.2f} км")

total = 10
distance = 10
for day in range(2, 8):
    distance *= 1.1
    total += distance
print(f"За 7 дней: {total:.2f} км")

# 5.51
area = 100
yield_per_ha = 20
for year in range(2, 9):
    area *= 1.05
    yield_per_ha *= 1.02
    print(f"Год {year}: урожайность {yield_per_ha:.2f} ц/га")

area = 100
for year in range(1, 8):
    area *= 1.05
    if year >= 4:
        print(f"Год {year}: площадь {area:.2f} га")

area = 100
yield_per_ha = 20
total_yield = 0
for year in range(1, 7):
    total_yield += area * yield_per_ha
    area *= 1.05
    yield_per_ha *= 1.02
print(f"Урожай за 6 лет: {total_yield:.2f} ц")

# 5.52
import math
total_volume = 0
diameter = 10
thickness = 0.5
for i in range(12):
    radius = diameter / 2
    volume = (4/3) * math.pi * radius**3
    total_volume += volume
    diameter += 2 * thickness
print(f"Суммарный объем: {total_volume/1000:.4f} л")

# 5.53
total = 0
for i in range(2, 11):
    total += i * i
print(total)

# 5.54
a = 2
n = 5
result = 1
for i in range(1, n + 1):
    result *= a
    print(f"{a}^{i} = {result}")

# 5.55
total = 0
sign = -1
for i in range(12, 103, 10):
    total += sign * (i * i)
    sign = -sign
print(total)

# 5.56
import math
area = 0
n = 1000
dx = math.pi / n
for i in range(n):
    x = i * dx
    area += math.sin(x) * dx
print(f"Площадь арки: {area:.4f}")

# 5.57
area = 0
n = 1000
dx = 2 / n
for i in range(n):
    x = 2 + i * dx
    y = 0.3 * (x - 1)**2 + 3
    if 2 <= y <= 4:
        area += dx
print(f"Площадь фигуры: {area:.4f}")

# 5.58
area = 0
n = 1000
dx = 2 / n
for i in range(n):
    x = i * dx
    y = 0.4 * (x + 2)**2 + 1
    if y <= 2:
        area += y * dx
print(f"Площадь фигуры: {area:.4f}")

# 5.59
n = 6
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# 5.60
n = 5
a = 3.5
result = 0
for i in range(n):
    result += a
print(result)

# 5.61
x = 7
y = 8
result = 0
for i in range(y):
    result += x
print(result)

result = 0
for i in range(x):
    result += y
print(result)

# 5.62
a = 2
n = 5
result = 1
for i in range(n):
    result *= a
print(f"{a}^{n} = {result}")

# 5.63
result = 20**2
for i in range(19, 11, -1):
    result = (result - i**2)**2
print(result)

# 5.64
num = 1234567
reversed_num = 0
temp = num
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
print(reversed_num)

# 5.65
n = 6
square = 0
for i in range(1, 2*n, 2):
    square += i
print(square)

# 5.66
total = 0
for n in range(1, 13):
    square = 0
    for i in range(1, 2*n, 2):
        square += i
    total += square
print(total)

# 5.67
n = 5
start = n * (n - 1) + 1
total = 0
for i in range(n):
    total += start + 2*i
print(total)

# 5.68
n = 5
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print(total)

# 5.69
n = 5
total = 1
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += 1 / factorial
print(total)

# 5.70
n = 5
x = 2
total = 1
factorial = 1
power = 1
for i in range(1, n + 1):
    factorial *= i
    power *= x
    total += power / factorial
print(total)

# 5.71
import math
result = math.sqrt(50)
for i in range(49, 0, -1):
    result = math.sqrt(i + result)
print(result)

# 5.72
import math
n = 5

total_a = 0
sin_sum = 0
for i in range(1, n + 1):
    sin_sum += math.sin(i)
    total_a += 1 / sin_sum
print(f"a) {total_a}")

result_b = math.sqrt(2)
for i in range(2, n + 1):
    result_b = math.sqrt(2 + result_b)
print(f"b) {result_b}")

total_c = 0
cos_sum = 0
for i in range(1, n + 1):
    cos_sum += math.cos(i)
    total_c += cos_sum
print(f"c) {total_c}")

total_d = 0
sin_sum = 0
for i in range(1, 2*n + 1):
    sin_sum += math.sin(i)
    total_d += sin_sum
print(f"d) {total_d}")

result_e = math.sqrt(3*n)
for i in range(n-1, 0, -1):
    result_e = math.sqrt(3*i + result_e)
print(f"e) {result_e}")

# 5.73
import math
length = 4.5
distance = 3
while distance > 0:
    angle = math.degrees(math.acos(distance / length))
    print(f"Расстояние: {distance:.1f} м, Угол: {angle:.1f}°")
    distance -= 0.2

# 5.74
print("Вариант 1:")
for i in range(10, 101):
    if i % 2 != 0:
        print(i)

print("Вариант 2:")
for i in range(11, 101, 2):
    print(i)

# 5.75
for i in range(100, 201):
    if i % 3 == 0:
        print(i)

# 5.76
a, b, c = 10, 50, 7
for i in range(a, b + 1):
    if i % c == 0:
        print(i)

# 5.77
for i in range(10, 100):
    if i % 2 != 0 and (i % 10 == 3 or i % 10 == 7):
        print(i)

# 5.78
for i in range(100, 1000):
    if i % 47 == 43 and i % 43 == 45:
        print(i)

# 5.79
for i in range(1000, 10000):
    if i % 133 == 125 and i % 134 == 111:
        print(i)

# 5.80
n = 3
for i in range(10, 100):
    if i % n == 0 or str(n) in str(i):
        print(i)

# 5.81
print("a):")
for i in range(100, 1000):
    if i**2 % 1000 == i:
        print(i)

print("б):")
for i in range(100, 1000):
    if i % 7 == 0:
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 7 == 0:
            print(i)

# 5.82
print("a):")
for i in range(10, 100):
    digits = [int(d) for d in str(i)]
    if (digits[0]**2 + digits[1]**2) % 13 == 0:
        print(i)

print("б):")
for i in range(10, 100):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum + digit_sum**2 == i:
        print(i)

# 5.83
total = 0
for i in range(1, 50, 2):
    total += i
print(total)

# 5.84
total = 0
for i in range(100, 1000, 2):
    total += i
print(total)

# 5.85
a, b = 10, 50
total = 0
for i in range(a, b + 1):
    if i % 4 == 0:
        total += i
print(total)

# 5.86
total = 0
for i in range(31, 100):
    if i % 3 == 0 and i % 10 in [2, 4, 8]:
        total += i
print(total)

# 5.87
count = 0
for i in range(100, 501):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum == 15:
        count += 1
print(count)

# 5.88
s = 15
count = 0
for i in range(100, 1000):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum == s:
        count += 1
print(count)

# 5.89
count = 0
for i in range(100, 1000):
    if i % 7 == 0:
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 7 == 0:
            count += 1
print(count)

# 5.90
n = 10
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
total = sum(fib[:n])
print(total % 2 == 0)

# 5.91
num = 28
print("a) Делители:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

print("б) Сумма делителей:")
div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
print(div_sum)

print("в) Сумма четных делителей:")
even_div_sum = sum(i for i in range(1, num + 1) if num % i == 0 and i % 2 == 0)
print(even_div_sum)

print("г) Количество делителей:")
div_count = sum(1 for i in range(1, num + 1) if num % i == 0)
print(div_count)

print("д) Количество нечетных делителей:")
odd_div_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i % 2 != 0)
print(odd_div_count)

print("е) Четных делителей:")
even_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i % 2 == 0)
print(even_count)

print("ж) Делителей больше d:")
d = 10
greater_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i > d)
print(greater_count)

# 5.92
num = 17
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)

# 5.93
num = 28
div_sum = sum(i for i in range(1, num) if num % i == 0)
print(div_sum == num)

# 5.94
n = 100
i = 1
while i*i <= n:
    print(i)
    i += 1

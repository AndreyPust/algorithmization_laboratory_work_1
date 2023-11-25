count = 0
max_element = 0
max_sum = 0

# Открытие файла
f = open('17_2024.txt')

# Чтение файла
s = f.readlines()

# Разбор по строкам:
for i in range(len(s)):
    s[i] = int(s[i])

# Определение максимального элемента, оканчивающегося на 13:
for i in range(len(s)):
    if abs(s[i]) % 100 == 13:
        max_element = max(max_element, s[i])

# Определение кол-ва троек чисел и максимальной из сумм:
for i in range(2, len(s)):
    bit_depth_1 = 0
    bit_depth_2 = 0
    bit_depth_3 = 0
    number_module_1 = abs(s[i-2])
    number_module_2 = abs(s[i-1])
    number_module_3 = abs(s[i])
    while number_module_1 > 0:
        bit_depth_1 = bit_depth_1 + 1
        number_module_1 = number_module_1 // 10
    while number_module_2 > 0:
        bit_depth_2 = bit_depth_2 + 1
        number_module_2 = number_module_2 // 10
    while number_module_3 > 0:
        bit_depth_3 = bit_depth_3 + 1
        number_module_3 = number_module_3 // 10
    if ((bit_depth_1 == 3 and bit_depth_2 == 3 and bit_depth_3 != 3)
            or (bit_depth_1 == 3 and bit_depth_2 != 3 and bit_depth_3 == 3)
            or (bit_depth_1 != 3 and bit_depth_2 == 3 and bit_depth_3 == 3)):
        if s[i-2] + s[i-1] + s[i] <= max_element:
            count = count + 1
            max_sum = max(max_sum, s[i-2] + s[i-1] + s[i])

# Закрытие файла
f.close()

print("Количество троек чисел:", count, "Максимальная из сумм троек:", max_sum)

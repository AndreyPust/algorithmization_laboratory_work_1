print("Введите наруральное число n:")
n = int(input())


# Функция поиска значения F(n):
def function_f(n):
    if n <= 2:
        return 1
    else:
        return function_f(n - 1) + 3 * function_f(n - 2)


print("F(", n, ") =", function_f(n))

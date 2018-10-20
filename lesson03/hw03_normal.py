# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    beefor = gen_n_member(n - 1)
    current = gen_n_member(n)
    result = [ current, beefor + current ]
    for i in range(1, m - n):
        result.append(result[i - 1] + result[i])
    return (result)

def gen_n_member(n):
    result = round(5**(-0.5) * ((5**0.5 + 1) / 2)**n)
    return result

print(fibonacci(3, 10))
print(fibonacci(5, 10))
print(fibonacci(8, 15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    array = origin_list
    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] > array[j]:
                tmp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = tmp
    return array

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, list):
    result = []
    for i in list:
        if(func(i)):
            result.append(i)
    return iter(result)

def even_filter(el):
    if el % 2 == 0:
        return True
    return False

list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for el in my_filter(even_filter, list): 
    print(el)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(A1, A2, A3, A4):
    V1 = (abs(A1[0] - A2[0]), abs(A1[1] - A2[1]))
    V2 = (abs(A2[0] - A3[0]), abs(A2[1] - A3[1]))
    V3 = (abs(A3[0] - A4[0]), abs(A3[1] - A4[1]))
    V4 = (abs(A4[0] - A1[0]), abs(A4[1] - A1[1]))
    if(V1 == V3 and V2 == V4):
        return "Это параллелограмм"
    else:
        return "Это не параллелограмм"

print(is_parallelogram((0, 0), (1, 2), (4, 2), (3, 0)))
print(is_parallelogram((1, 1), (3, 1), (7, 3), (5, 3)))
print(is_parallelogram((0, 0), (3, 1), (3, 3), (1, 3)))
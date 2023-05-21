# # task 9
# s = 1
# n = int(input("Введите целое неотрицательное число: "))
# while n != 0:
#     s *= n
#     n -= 1
# print(s)

# # task 11
# f = [0,1]
# i = 1
# n = int(input("Введите натуральное число больше 1: "))
# while f[i] < n:
#     i += 1
#     f.append(f[i-1] + f[i-2])
# if f[i] == n: 
#     res = i+1
# else:
#     res = -1
# print(res)

# task 13
MidTempData = []
N = int(input("Введите общее количество дней (от 1 до 100): "))
i = 0
while i < N:
    MidTempData.append(int(input(f"{i} {N} Введите среднесуточную температуру (от -50 до +50) за {i+1} число: ")))
    i += 1
print(MidTempData)

LongPeriod = 0
temp = 0
for i in MidTempData:
    if i > 0:
        temp += 1
    else:
        if temp > LongPeriod: LongPeriod = temp
        temp = 0
print(LongPeriod)

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

# # task 13
# MidTempData = []
# N = int(input("Введите общее количество дней (от 1 до 100): "))
# i = 0
# while i < N:
#     MidTempData.append(int(input(f"{i} {N} Введите среднесуточную температуру (от -50 до +50) за {i+1} число: ")))
#     i += 1
# print(MidTempData)

# LongPeriod = 0
# temp = 0
# for i in MidTempData:
#     if i > 0:
#         temp += 1
#     elif temp > LongPeriod: 
#         LongPeriod = temp
#         temp = 0
# if temp > LongPeriod: LongPeriod = temp
# print(LongPeriod)


# task 15
n = int(input("Введите количество арбузов: "))
massaMin = 1000
massaMax = 0
print(massaMin, massaMax)
for arbuz in range(1,n + 1):
    massa = int(input(f"Введите массу {arbuz} арбуза: "))
    if massa < massaMin: massaMin = massa
    if massa > massaMax: massaMax = massa
    

print(massaMin, massaMax)

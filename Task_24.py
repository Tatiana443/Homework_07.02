# Всего на грядке растет N кустов. Выросло различное 
# число ягод – на i-ом кусте выросло ai ягод.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9
n = int(input("Введите колличество кустов N: "))
ber = list(map(int, input("Введите колличество ягод на каждом кусте: ").split()))
max_sum = 0
for i in ber:
    pick_sum = sum(ber[i:i-3])
    if pick_sum > max_sum:
         max_sum = pick_sum
         print(f'Максимальное число ягод --> {max_sum}')


# i = 0
# for i in range(len(ber)):
#      pick_sum = (ber[i] + ber[i+1] + ber[i-1])
#      if pick_sum > max_sum:
#         max_sum = pick_sum
# print(max_sum)

#     i# print(f'Максимальное число ягод --> {max_sum}')
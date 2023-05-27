'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

'''

while(True):
    try:
        N = int(    input("Введите кол-во элементов массива:"  ))
    except:
        print('Введено не число!')
        continue
    if N > 0:
        break
    else:
        print('Число должно быть ,больше нуля!')

array = []
readInt = 0
for i in range(N):
    while(True):
        try:
            readInt = float(input(f"Введите {i} элементы массива (целое число):"  ))
        except:
            print('Введено не число!')
            continue
        if  int(readInt) == readInt:
            break
        else:
            print('Число должно быть, целым!')

    array.append(int(readInt))

print(array)
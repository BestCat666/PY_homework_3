#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10

num = int(input('Введите число: '))
excess = ""                 # сохраняется остаток
while num > 0:
    last = str(num % 2)
    excess = last + excess
    num = int(num // 2)

print(excess)                # это str!
#print(int(excess))



'''
вывод в обратном порядке! можно подставить другое число, чтобы перевести в другой разряд
num = int(input('Введите число: '))
while num > 0:
    last = str(num % 2)    
    num = int(num // 2)
    print(last)
'''
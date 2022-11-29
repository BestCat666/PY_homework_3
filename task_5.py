#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, , 0, 1, 1, 2, 3, 5, 8, 13, 21] 

fib1 = 1
fib2 = -1
n = 9
lst_1 = []
while n > 0:
  for e in range(0, n):
    fib1, fib2 = fib2, fib1 - fib2
    lst_1.append(fib2)
    n = n - 1
lst_1 = [1, 1, 0, -1] + lst_1
new_lst = lst_1[::-1]
print(new_lst)                                   
    
    
fib1 = fib2 = 1
n = 10
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    new_lst.append(fib2)
    n = n - 1
print(new_lst)  


'''
def fib(n):
 if n in [1, 2]:
   return -1
 else:  
   return fib(n + 2) - fib(n + 1)
list = []
for e in range(1, -30):
  list.append(fib(e))
print(list) 
'''

'''
def fib(n):
 if n in [1, 2]:
   return -1
 else:  
   return (-1)**(n+1) * fib(n)
list = []
for e in range(0, -20):
  list.append(fib(e))
print(list) 



def fib(n):
 if n in [1, 2]:
   return 1
 else:
   return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
  list.append(fib(e))
print(list)

'''
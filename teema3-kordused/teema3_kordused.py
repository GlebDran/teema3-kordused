print("\n--- ulesanne 2 ---\n")

while True: #цикл - пока не введешь цифру, программа будет работать
      try:
        a = int(input("Sisesta A: "))
        break 
      except ValueError:
            print ("On vaja naturaalne arv")
summa = 0
if  a >0:
    for i in range(1, a+1, 1):
        summa+=i            #summa=summa+i
        print(f"{i}. samm summa={summa}")
print(f"Vastus {summa}")

print("\n--- ulesanne 3 ---\n")

p = 1
for i in range (8):
       while True: #цикл - пока не введешь цифру, программа будет работать
          try:
           arv = float(input(f"sisesta {i+1} arv: "))
           break 
          except ValueError:
            print ("On vaja arv")
       if arv>0: p*=arv
       else:
           print ("Korrutame arvud rohkem kui 0")
       print (f"{i}. samm korrutis= {p}")
print (f"lõpptulemus on {p}")

print("\n--- ulesanne 4 ---\n")

for i in range (10, 21, 1):
    print(i**2, end=";")

print("\n--- ulesanne 16 ---\n")

for j in range(1, 10): #строка
    for i in range(1,10): #столбец
        if i==j:
            print(j, end=" ")
        else:
            print(0, end=" ")
    print()

print("\n--- ulesanne 15 ---\n")

for read in range (10):
    for rida in range (10):
        print(rida, end=" ")
    else:
        print()
print()

print("\n--- ulesanne 8 ---\n") # 8. Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм = 2,5 см) для значений длин от 1 до 20 дюймов.

# Таблица перевода расстояний из дюймов в сантиметры
print("Дюймы\Сантиметры")
for inches in range(1, 21):  # От 1 до 20 включительно
    cm = inches * 2.5
    print(f"{inches}\{cm:.2f}")
    

print("\n--- ulesanne 28 ---\n")

import random  #модуль random для генерации случайных чисел

secret_number = random.randint(1, 10) # Компьютер загадывает случайное число от 1 до 10
print("Я задумал число от 1 до 10. Попробуй угадать его!")
schetchik = 0 # счетчик попыток
while True: # бесконечный цикл
    user_guess = int(input("Введи своё предположение: "))  # Пользователь вводит число
    schetchik += 1  # Увеличиваем счетчик попыток
    if user_guess < secret_number: # Проверяем, угадал ли пользователь число
        print("Моё число больше.")
    elif user_guess > secret_number:
        print("Моё число меньше.")
    else:
        print(f"Поздравляю! Ты угадал число {secret_number} за {schetchik} попыток.") #выходим из цикла
        break
print("\n--- ulesanne 17 ---\n")

number = 2

for i in range(1, 10):  #Цикл от 1 до 9
    print(f"{number}*{i}={number * i}")

print("\n--- ulesanne 18 ---\n")

for number in range(20, 51): #перебираем числа от 20 до 50 включительно
    if number % 3 == 0 and number % 5 !=0: #проверяем условия делимости 
        print(number)
#число делится на 3 (number % 3 == 0).
#число не делится на 5 (number % 5 != 0).
#оператор % (ПРОЦЕНТ) в Python (и во многих других языках программирования) называется оператором остатка от деления. 
#Он используется для вычисления остатка при делении одного числа на другое.
# Оператор != в Python означает "не равно". Он используется для сравнения двух значений и возвращает:
# True, если значения не равны.
# False, если значения равны.

print("\n--- ulesanne 9 ---\n")

summa = float(input("Введите сумму вклада: "))
god = int(input("Введите кол-во лет: "))
stavka = 0.03
itog = summa * (1 + stavka) ** god
print (f"через {god} лет, сумма вклада будет {itog:.2f} евро") #2.f выводим 2 знака после запятой
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
       print (f"{i}. samm korrutis= {p}")
print (f"lõpptulemus on {p}")
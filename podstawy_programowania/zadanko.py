import random

x1 = eval(input("Podaj poczatek przedzialu: "))
x2 = eval(input("Podaj koniec przedzialu: "))
x=0
for i in range(5):
    liczba = random.randint(x1,x2)
    x= x+1
    print("Liczba nr ",x, ": ",liczba)
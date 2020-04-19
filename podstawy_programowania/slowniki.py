#slownik = {'key1':'value1', 'key2':'value2'}

'''
Utwórz słownik o nazwie pracownik zawierający klucze:
imie, nazwisko, miastko, wiek, imionadzieci, imionarodzicow.
'''

pracownik = {
    'imie':'Jarek',
    'nazwisko':'Odarek',
    'miasto':'Pacanów',
    'wiek':'47',
    'imionadzieci':['Marek', 'Janek'],
    'imionarodzicow':['Józio', 'Basia']
}
pracownik['wzrost'] = 185
pracownik['waga'] = 85

pracownik1 = {
    'imie' : 'Anna',
    'nazwisko' : 'Kowalska',
    'city' : 'Poznań',
    'age' : 24
}

'''key = 'age'
if key in pracownik1:
    del pracownik1[key]
    print(f'Klucz {key} został usunięty.')
else:
    print(f'Klucz {key} nie został usunięty')
'''

#print(pracownik1.keys())
#print(pracownik1.values())
#print(list(pracownik1.values()))
#print(pracownik1.items())
'''
for value in pracownik1.values():
    print(value, end=", ")

print()
for key, value in pracownik1.items():
    print(f'{key}: {value}')

'''
'''
    Utwórz słownik, który zawiera dane podane przez użytkownika z klawiatury:
    imię, nazwisko, wiek. Przypisz do słownika dane pobrane od dwóch użytkowników.
    Wyświetl dane w formacie
    user1: {imie} {nazwisko} wiek: {wiek}
    user2: {imie} {nazwisko} wiek: {wiek}
    Średni wiek użytkowników wynosi: {średnia} lat
'''

print("Podaj dane pierwszego usera")
name1 =  input("Podaj imie: ")
surname1 =  input("Podaj nazwisko: ")
age1 =  eval(input("Podaj wiek: "))

print("Podaj dane drugiego usera")
name2 =  input("Podaj imie: ")
surname2 =  input("Podaj nazwisko: ")
age2 =  eval(input("Podaj wiek: "))

user1 = {
    'imie' : name1,
    'nazwisko' : surname1,
    'wiek' : age1
}
user2 = {
    'imie' : name2,
    'nazwisko' : surname2,
    'wiek' : age2
}

print("user1: ",user1['imie']," ",user1['nazwisko'], " wiek: ",user1['wiek'])
print("user2: ",user2['imie']," ",user2['nazwisko'], " wiek: ",user2['wiek'])

srednia = (user1['wiek']+user2['wiek'])/2

print(f"Średni wiek użytkowników wynosi: {srednia} lat")




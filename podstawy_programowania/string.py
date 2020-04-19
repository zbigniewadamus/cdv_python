text = "Anna, paweł, TomEK"

tab = text.split(", ")

print(text)
print(tab)
print(type(tab))
name1 = tab[0]
print("Twoje imie: " + name1)

nameUpper = name1.upper()
print(nameUpper)

nameLower = name1.lower()
print(nameLower)

#sprawdzenie zawartości
surname = input("Podaj imionko: ")
content = surname.isalpha()
print(content)


name="Katarzyna"
print("\nDane użytkownika\nMasz na imie:", name)
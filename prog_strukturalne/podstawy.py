print("cdv")
print(2)
print('test')

#potęga
pow=2**10
print(pow)

text="CDV"
print(text * 2)

#pobieranie danych z klawiatury
name=input()
print("Twoje imię: "+name)
surname=input("Podaj swoje nazwisko: ")
print("Twoje nazwisko: "+surname)

print("Imie: "+ name + ", nazwisko: "+ surname)

surnameLength=len(surname)
print(type(surname))
print(type(surnameLength))
surnameLength = str(surnameLength)
print("Dlugosc nazwiska: " + surnameLength)

#zadanie
imie =input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")
wiek=input("Podaj wiek: ")
print("Imie i nazwisko: "+imie, nazwisko+", wiek: "+wiek)

firstLetter=surname[0]
lastLetter=surname[-1]
print("Pierwsza Litera "+firstLetter)
print("Ostatnia Litera "+lastLetter)

#konwersja

x="5"
print(type(x))
x=int(x)
print(type(x))
a = 1

print(type(a))

a = "sample text"
print(type(a))

a = 1.0
print(type(a))

pi = 3.14
print(type(pi))

myChar = 'a'
print(type(myChar))

imie = "Anna"

adres_zamieszkania = "Nieznana 20"

adreszamieszkania = "Nieznana 20"
drugie_imię = "Beata"
#3ulubionePotrawy = „x, y, z”
#and = 51
and_Dana = 1023
And = "hello"
#twoje zainteresowania = „nurkowanie”
twoje2samochody = "v, m"
śćółżęąćł = " :-) "
twojaSzczesliwaLiczbaKtoraWylosowanoSpecjalnieDlaCiebie = 5

""""
sadsad
wewewe
"""

numer = 45
print(numer)

zajęcie = "Szkolenia"
print(zajęcie)

ilość = 23.5
print(ilość)

obiekt = "Test"
print(obiekt)

przyszłość = '?'
print(przyszłość)

print(obiekt, przyszłość)

przyszłość = '!'
print(przyszłość)

#########################
# Syntax
#########################



#########################
# Tuple
#########################

a = (1,2,3)
print(type(a))

print (a[0])
print (a[1])
print (a[2])

a = (1,2,3,'s','a','m','n')
print(type(a))

print(a[4])

#one element tuple
a = (1,)
print(type(a))

#tuple is immutable
#a[0] = 4

a = 1,2,3,4,5,'a','b','c'
print(type(a))

a = tuple((1,2,3))
print(type(a))

#########################
# List
#########################

a = [1,2,3,4,'a','b']
print(type(a))


print(a[2])

#podmiana wartości pod indeksem drugim
a[2] = 'nowa'
print(a)

#dodawanie nowej wartosci na koncu listy
a.append('nowa2')
print(a)

#dodawanie wartosci na wybranej pozycji
a.insert(2,'nowa3')
print(a)

#usuwanie

del a[0]

print(a)

#
print(len(a))

a_tuple = tuple(a)
print(type(a_tuple))

###################

a = 1
b = 2
c = a

a = b
b = c

a = 1
b = 2

a,b = b,a

print (a)
print (b)

#petla for each
a = [1,2,3,4,'a','b']
for ad in a:
    print (ad)

a = list(range(1,5,1))
print(a)

for elem in a:
    print(elem)

my_list = [1,2,'log',4,'a','b']
counter = 0
for elem in a:
    print (my_list[counter])
    counter +=1 # counter = counter +1

my_tuple = ('a','b','c')
for elem in my_tuple:
    print(elem)

a = list(range(0,3,1))
print (a)
counter = 0
for elem in a:
    print(my_tuple[counter])
    counter +=1

for elem in a:
    print(my_tuple[elem])


a = [1,2,3,4,5]

for elem in a:
    print(elem * 2)

a = ['a','b',3,4,5]

for elem in a:
    print(elem * 2)


a = [1,2,3,4,5,6,7]
a = (list(range(1,11,1)))

new_list = []
for elem in a:
    if elem > 3:
        new_list.append(elem)

print(new_list)

new_list3  = []
a = [1,2,3,4,5,6,7]
for elem in a:
    if elem % 2 == 0:
        new_list3.append(elem)
print(new_list3)

a ="sample text"

for letter in a:
    print(letter)


counter = 0
while counter < 3:
    print(counter)
    counter +=1



"""
while 1==1:
    counter = 4
    if counter > 0:
        break
    counter =- 1
"""





###################################
# SET
###################################

a = [1,11,2,3,4,5]

b = "sample text"

c = (1,2,1,2,3)

a_set = set(a)
print (type(a_set))
b_set = set(b)
print (type(b_set))
c_set = set(c)
print (type(c_set))

print(a_set)
print(b_set)
print(c_set)


for elem in a_set:
    if elem ==1:
        print("ok istnieje")

print(1 in a)

#zbiór {}

a = {1,1,2,3}
print(a)

a.remove(1) #usuwa wartosc, nie indeks


a = [1,2,3]

#frozenset is immutable

a_set = frozenset(a)

print(a)

#Dictionary

numbers = {
    'a': 2,
    'b': 3,
    'c': 4
}
print(numbers)
print(type(numbers))
print(numbers['b'])

print(numbers.keys())
print(numbers.values())
print(numbers.items())

items = numbers.items()

for item in items:
    print(item)
    print(item[0])
    print(item[1])

#slices
a = [1,2,3,4,5,6,7]

print(a[0:3:1])

#last element
print(a[len(a) - 1])
print(a[-1:-4:-1])
print(a[::])
print(a[::-1])

text = "sample text"
textList = text.split(" ")
print(textList)
print(" ".join(textList))

a = "sample text"
print(a[:: -1])

zmienna_1 = "Ciekawe"
zmienna_2 = "Programowanie"
zmienna_3 = "Jest"
zmienna_4 = "Wciągające"
zmienna_5 = "I"

print(zmienna_1 + ' ' + zmienna_2 + ' ' + zmienna_5 + ' ' + zmienna_3 + ' ' + zmienna_4)

"""
czas = 45

#kolorowa
print (2*45)/5

#czarno
print(45*8)/2

"""

#P10

kwota = 1000


print(round(kwota * 0.97, 2))


#P11

Chleb = 1.99
chs = 2
Mleko = 2.50
ms = 0.5
Cukierki = 12.99
cs = 0.3

print(Chleb * chs + Mleko * ms + Cukierki * cs)



print(a)
a= 0o27
print(a)

print(bool(7))

imie = 'Adam'
nazwisko = 'Kowalski'
wiek = 35
pensja = 6000
stanowisko = "młodszy inżynier procesu"


print (10 * ('Pan ' + imie + ' ' + nazwisko + '(' + ' wiek ' + str(wiek) + 'lat' + ')' + ' pracuje na stanowisku ' + stanowisko + ' (pensja:' + str(pensja) + 'brutto.'))

dochod = 700
koszt = 500
wiekszy_dochod = 1.5
dochod2 = dochod - koszt * wiekszy_dochod
dochod3 = dochod2 * wiekszy_dochod

print(dochod - koszt + dochod2 + dochod3)




stawka = 5500
czas = 168

"""
a*h/2

"""

print(stawka/czas)
print(stawka/czas * 1.23)

a = (bool(0))
b = (bool(0))
c = (bool(1))

W1 = (not a) and (not b) and (not c)
W2 = (not a) and (not b) and (c)
W3 = (not a) and (b) and (not c)
W4 = (a) and (not b) and (not c)

print(W1 or W2 or W3 or W4)

"""

imie = input("wczyta napis")
print(30 * (imie + "\n"))

"""
"""
b = int(input('bok'))
w = int(input('wysokosc'))
"""
#print(b * w / 2)

a = 'aaaabbbbbbbcccccc'
dictionary = dict()
for letter in a:
    if letter in dictionary:
        dictionary[letter] =+ 1

    else:
        dictionary[letter] = 1
print(dictionary)


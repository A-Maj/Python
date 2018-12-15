
st = [eval(input('1')), eval(input('2')), eval(input('3')), eval(input('4')), eval(input('5'))]

list = []

for elem in st:
    if type(elem) is str:
        list.append(elem)

print(list)


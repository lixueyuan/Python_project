a = 1
array = []
while a < 6:
    b = int(input('输入第位数'))
    array.append(b)
    a = a +1

min = array[0]
max = array[1]
for s in array:
    if s > min:
        max = s
    if s < max:
        min = s

print (max,min)



list = ['hello', 'this', 'is', 'kaushal']
dict = {}
for item in list:
    dict[item] = 4
print dict

for item in dict:
    if item is 'hello':
        dict[item] += 1
print dict


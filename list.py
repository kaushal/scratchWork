# Scrip to take an input list and generate two lists that sum to the same value
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a.sort()

l1 = []
l2 = []
last = 0
seocond = 0
for item in a:
    if last is 0:
        l1.append(item)
        last = 1
    elif last is 1:
        l2.append(item)
        last = 0
s1 = sum(l1)
s2 = sum(l2)

while not s1 == s2:
    if(s1 > s2):
        l2.append(l1[0])
        l1.pop(0)
        l2.sort()
    if(s2 > s1):
        l1.append(l2[0])
        l2.pop(0)
        l1.sort()
    s1 = sum(l1)
    s2 = sum(l2)

print l1
print s1

print l2
print s2


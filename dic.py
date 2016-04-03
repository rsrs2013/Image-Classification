d = {}
mylist = ['a','b','c','b','c','b','d','e']
distinctSet = set(mylist)
count = 5
defaultWeight = 1
hislist = [defaultWeight]*count
for x in mylist:
    d[x] = 1
mylist = list(d.keys())
print mylist
print hislist
print len(mylist)
distinctList = list(distinctSet)
print distinctList
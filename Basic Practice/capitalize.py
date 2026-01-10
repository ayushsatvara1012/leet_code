name = str(input())
newname = []
listname = name.split(' ')

for i in listname:
    nm = i.capitalize()
    newname.append(nm)

for i in newname:
    print(i,end=' ')

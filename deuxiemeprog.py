import copy 
liste=[1,2,3]
print(liste)
liste[2]=5
print(liste)
liste.append(4)
print(liste)
del liste[0]
print(liste)
liste.remove(2)
print(liste)
liste.reverse()
print(liste)
print(len(liste))
liste.append(2)
liste.append(1)
liste.append(5)
liste.append(3)
print(liste)
print(liste.count(5))
print(liste.count(8))
print(liste.index(2))
print(liste[-1])
print(liste[:])
print(liste[-4:])
print(liste[:2])
print(liste[2:3])
for i in liste:
    print i
for i in enumerate(liste):
    print i
x=[1,2,3]
y=x[:]
y[1]=0
print(x)
print(y)
y=copy.deepcopy(x)
y[0]=20
print(y)
chaine="olivier:engel:stasbourg"
print(chaine.split(":"))
liste=['olivier','engel','strabourg']
print(':'.join(liste))
for i in range(10):
    print i
print(range(10))
x=[1,2,3,4]
y=[4,5,6,7]
x.extend(y)
print x























def somme(a,b,c,d,e):
    return a+b+c+d+e
print(somme(2,3,1,4,6))
def addition(*syl):
    return syl[0]+syl[1]+syl[2]+syl[3]
print(addition(2,6,3,5,7,7))
#exercice4
def somme(*elvi):
    som=0
    for i in elvi:
        som+=i
    return som
print(somme(1,2,34,4,5,67,8))
def maximum(a,b,c):
    return max(a,b,c)
print(maximum(1,2,3))


#EXERCICE SUR LES FONCTIONS
#exercice1
#la difference est que la fonction a une valeur de retour alors que la procedure n'en a pas
#il n'y a pas de difference entre l'appel d'une fonction et celle d'une procedure
def fusion(liste1,liste2):
    return liste1+liste2
print(fusion([1,2,3],[4,5,6]))

#exercice2
def inverse(liste):
    return list(reversed(liste))
print(inverse(['bonjour','monsieur','le','ministre']))

def table_multiplication(mul,borninf,bornsup):
    for i in range(borninf,bornsup+1):
        print i,"*",mul,"=",i*mul
print(table_multiplication(2,1,12))

#exercice3
def position(a,liste):
    return liste.index(a)
print(position(2,[6,2,9]))

#exercice4
def somme(*elvi):
    som=0
    for i in elvi:
        som+=i
    return som
print(somme(1,2,34,4,5,67,8))

def maximum(a,b,c):
    return max(a,b,c)
print(maximum(1,2,3))

#exercice5
def pair(a):
    if a%2==0:
        return True
    else:
        return False
def impair(a):
    if a%2!=0:
        return True
    else:
        return False
val=input('entrez une valeur:')
print(pair(val))
print(impair(val))




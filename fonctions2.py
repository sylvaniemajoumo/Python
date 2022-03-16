'''#exo1
def table_multiplication(mul,borninf,bornsup):
    for i in range(borninf,bornsup+1):
        print i,"*",mul,"=",i*mul
#programme principal
table_multiplication(mul=input("entrer le multiplicateur:"),borninf=input("entrer la borne inferieure:"),bornsup=input("entrer la borne superieure:"))
#exo2
from math import pi
def cube(a):
    return a**3
print(cube(3))
def volumesphere(r):
    return (4*pi*cube(r))/3
#programme principal
r=int(input("entrer le rayon:"))
print(volumesphere(r))
#exo3
def triangle(n):
    nbretoile=1
    nbrespace=n-1
    for i in range(1,n+1):
        print(nbrespace*" "+nbretoile*"*")
        nbretoile+=2
        nbrespace-=1        
#programme principal
triangle(input("saisir le nombres de lignes:"))
#exo4
def maximum(a,b,c):
    return max(a,b,c)
#programme principal
print(maximum(a=input("saisir la valeur de a:"),b=input("saisir la valeur de b:"),c=input("saisir la valeur de c:")))
#exo5
def trianglechiffre(n):
    nbrechiffre=2
    nbrespace=n-1
    a=1
    for i in range(1,n+1):
        print(nbrespace*" "+nbrechiffre*str(a))
        nbrechiffre+=2
        nbrespace-=1
        a+=1
#programme principal
trianglechiffre(input("saisir le nombre de ligne:"))
#exo6
def chiffreportebonheur(nb):
    nbre=nb
    while nb>10 and nb!=1:
        somme=0
        chaine=str(nb)
        taille=len(chaine)
        for i in range(0,taille):
            entier=int(chaine[i])
            somme+=entier**2  
        nb=somme
        print nb
    if nb==1:
        print "le chiffre:",nbre,"est porte bonheur"
    else:
        print"le chiffre:",nbre,"nest pas porte bonheur"
#programme principal
chiffreportebonheur(input("saisir un chiffre:"))
#exo7
def comptemots(phrase):
    nbremot=1
    nbrespace=0
    taille=len(phrase)
    for i in range(0,taille):
        if phrase[i]==" ":
            nbremot+=1
    print nbremot
#programme principal
comptemots(input("saisir votre phrase:"))
#exo8
def comptemots(phrase):
    return len(phrase.split(" "))
phrase=input("entrez votre phrase:")
print(comptemots(phrase))
#exo9
def update_score(current,value):
    current=+current+value
    return current
current=int(input("entrer le score:"))
value=int(input("entrer la valeur a ajouter:"))
print(update_score(current,value))
#exo 10
def get_name():
    name=input("quel est votre nom?")
    return name
def calc_calories(miles,calories_per_mile):
    calories=miles*calories_per_mile
    return calories
distance=int(input("combien de miles avez-vous fait cette semaine?"))
burn_rate=50
biker=get_name()
calories_burned=calc_calories(distance,burn_rate)
print biker,",vous avez brule a propos",calories_burned,"calories."'''
#exo11



    



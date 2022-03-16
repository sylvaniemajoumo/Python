'''#import monmodule
#from monmodule import somme
#from mondule import *

nombre1=int(input('saisir le premier nombre:'))
nombre2=int(input('saisir le second nombre"'))

#print(monmodule.somme(nombre1,nombre2))'''

#les fichiers

fichier=open('monfichier.txt','a')
fichier.write('bonjour le monde')
fichier.close()

fichier=open('monfichier.txt','a')
nbre1=input("entrez le premier nombre:\n")
nbre2=input("entrez le second nombre:\n")

fichier.write("\nle premier nombre est:"+str(nbre1))
fichier.write("\nle second nombre est:"+str(nbre2))

somme=int(nbre1)+int(nbre2)
print "la somme des deux nombres est:",somme

fichier.write("\nla somme des deux nombres est:"+str(somme))
fichier.close()


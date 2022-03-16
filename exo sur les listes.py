#exercie 5
liste=[0,1,2,3,4,1,4,3,0,1]
print(len(liste))
print(liste.count(0))
print(liste.count(1))
print(liste.count(2))
print(liste.count(3))
print(liste.count(4))
print(liste.index(3))
print(sorted(liste))
#sorted() renvoi une liste triee par ordre croissant alors que sort()ne renvoi rien mais la liste devient maintenant ordonee.
#exercice 6
liste=['a','hello',1,2,3,4,'t',10,20,'oui','moi','toi','bonjour monsieur']
for i in liste:
    print i
#exercice 8
'''
[1,2,3,4,4,5,1,0]
[1,2,3,4,4,5,1,0]
le programme ci dessous multipli une liste par 5.le resultat du programme est[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
'''
#exercice9
'''
[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
5
1
2
4
2
2
3
4
'''
#exercie 7
val=2
liste=[]
liste.append(val)
for i in range(4):
    val=val*val
    liste.append(val)
print(liste)



#exo sur les dictinnaires
import random
dico={}
dico["comment tu t'appelles?"]="sylvanie"
dico["quel age as-tu?"]="19ans"
dico["tu es de quel pays?"]="le cameroun"
dico["ta nourriture preferee?"]="eru"
dico["ton passe temps favori?"]="dormir"
print(dico)
points=0
nbreqstrep=0
for i in range(len(dico)):
    cleliste= random.sample(dico.keys(),1)
    cle=cleliste[0]
    print(cle)
    nbreqstrep+=1 
    valeur=input('entrez la reponse:')
    print(valeur)
    if valeur==dico[cle]:
        points+=1
        print('bonne reponse')
    else:
        print('mauvaise reponse')
    del dico[cle]
    print(dico)
    question='voulez-vous continuez?'
    print(question)
    if dico=={}:
        break
    reponse=input('tapez "o" pour oui et "n" pour non:')
    if reponse=="o":
        continue
    else:
        break
print 'ton score est',points,'sur', nbreqstrep











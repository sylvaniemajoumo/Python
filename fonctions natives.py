import random
print abs(-2)
liste=[1,1,0]
print all(liste)
print any(liste)
print bin(2)
print "madame".capitalize()
print random.choice(liste)
print "madame".count("a")
s="sylvanie"
print s.endswith("e")
print s.endswith("er")
e=24
print eval('e*3')
print "elvira".find("r")
print help(str)
print hex(32)
print "23f".isalnum()
print "+".isalnum()
print "data".isalpha()
print "12".isdigit()
print "Danyie".islower()
print " ".isspace()
print callable(any)
print "Titre".istitle()
print "LoVE".isupper()
print "+".join(["claude","elvi"])
print len((1,2,3))
print locals()
print "LONgue".lower()
def add_one(x):
    return x/2
print map(add_one,[3,4,5])
print max(1,23,4,5)
print min(3,4,5)
print random.randint(2,22)
print random.random()
print "ines".replace("i","a")
X=[1,2,3]
X.reverse()
print X
print list(reversed([1,2,3]))
print round(1.5)
y=[1,2,3,4]
random.shuffle(y)
print y
print "berone".startswith(("be","syl"))
T=[99,4,7,0,1]
T.sort()
print T
print sorted(T)
print "sylvira+clauvira".split("+")
print "olivier\n\n\engel\n\ndeveloppeur".splitlines()
print sum([2,3,6])
print "maman part au stade".title()
print "delano".upper()
a=[1,2,3]
b=["maman","baby","papa"]
print zip(a,b)
try:
  a=4
  b=0
  print(a/b)
except ZeroDivisionError:
    print("Erreur")
except TypeError:
    print("Erreur")
except:
    pass
finally:
    print('Execution')

print ("la suite du progamme")





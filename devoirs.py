'''#exercice
#1-
largeur=20
hauteur=5*9.3
print (largeur*hauteur)
#2-
a=3
b=5
c=7
print(a-b//c)
#3-
r,pi=12,3.14159
s=pi*r**2
print(s)
print(type(r),type(pi),type(s))
#page 31
#4-
for i in range (0,20):
    p=7*i
    print i,'*','7','=',p

def table_multiplication(mul,a,b):
    for i in range (a,b+1):
        a=i
        b=i*mul
        print a,'*',mul,'=',b
print table_multiplication(7,1,20)
#5-
for i in range (1,10):
    s=i*1.65
    print i,'euro','=',s,'dollar(s)'
def conversion(a,b):
    for i in range (a,b+1):
        a=i
        b=i*1.65
        print a,'euro=',b,'dollar(s)'
print conversion(1,10)
#6-
a=1
for i in range (1,13):
    print a
    a=a*3
#page 35
#7-
pro= input('entrez la profondeur:')
la=input('entrez la largeur:')
hau=input('entrezla hauteur:')
print 'le volume est:',pro*la*hau
#page 36
#8-
t=input('entrer le nombre de secondes')
j=t//86400
h=(t%86400)//3600
m=((t%86400)%3600)//60
s=((t%86400)%3600)%60
print 'ce nombre de seconde correspond a:',j,'jour(s)',h,'heure(s)',m,'minute(s)',s,'seconde(s)'
#9-
def table_multiplication(mul,a,b):
    for i in range (a,b+1):
        a=i
        b=i*mul
        if b%3==0:
           print b,'*'
        else:
            print b
print table_multiplication(7,1,20)
#10-
def table_multiplication(mul,a,b):
    for i in range (a,b+1):
        a=i
        b=i*mul
        if b%7==0:
           print b
print table_multiplication(13,1,50)
#11-
print '*'
print '**'
print '***'
print '****'
print '******'
print '*******'
print '********'
#page40
#12-
a=input('entrez la valeur en degre:')
b=a*(3.14159/180)
print a,'degre=',b,'radian(s)'
#13-trivial
#14-
a=input('entrez la valeur en degre:')
b=a*1.8+32
print a,'degres celcius=',b,'fahrenheit'
#15-
u=100
for i in range (1, 21):
    u=u*0.043+u
print'la somme des interets est:',u'''
#16-
nc=1
ng=1
while nc<65:
    print(nc,ng)
    nc,ng=nc+1,ng*2
#17-


    


class personne:
    
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
        self.age=18
    
    def getnom(self):
        return self.nom
    def getage(self):
        return self.age
    def getprenom(self):
        return self.prenom
pers=personne("alex","jules")
print pers.getnom()
print pers.getage()
print pers.getprenom()









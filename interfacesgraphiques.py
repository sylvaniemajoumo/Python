#interfaces graphiques
from Tkinter import *
fenetre = Tk()
fenetre.title('ma fenetre')
#fenetre.geometry('400*300')
#les labels
label=Label(fenetre,text="hello world", bg="blue")
label.pack()
#les boutons
bouton=Button(fenetre,text="fermer",command=fenetre.quit)
bouton.pack()
#input/entree
value=StringVar()
value.set("texte par defaut")
entree=Entry(fenetre, textvariable="string",width="30")
entree.pack()
#case a cocher
bouton= Checkbutton(fenetre,text="gentil?")
bouton.pack()
#boutons radios
value=StringVar()
bouton1=Radiobutton(fenetre, text="oui", variable=value,value=1)
bouton2=Radiobutton(fenetre, text="non", variable=value,value=2)
bouton3=Radiobutton(fenetre, text="peut-etre", variable=value,value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
#les listes
liste=Listbox(fenetre)
liste.insert(1,"python")
liste.insert(2,"PHP")
liste.insert(3,"jQuery")
liste.insert(4,"CSS")
liste.insert(5,"javascript")
liste.pack()
#canvas


fenetre.mainloop()


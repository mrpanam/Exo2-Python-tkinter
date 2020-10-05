from fr.data.niv1 import Film
from tkinter import *

fenetre = Tk()
fenetre.title("Seance de Cinema - Logiciel de gestion")
fenetre.geometry("400x300")

print("Bienvenue au cinema, voici les films à l'affiche")

films = ["Gladiator", "The revenant", "The Lion king"]

for i in enumerate(films):
    print(i)

f1 = Film("Gladiator", "17h30", 80)
f2 = Film("The Revenant", "14h10", 120)
f3 = Film("The Lion king", "11h00", 50)
f4 = Film("Pulp Fiction", "15h30", 80)

films = [f1, f2, f3, f4]


def click_btn(film_id):
    print("vous avez reserver 1 place pour ",film_id)
    if film_id.places > 1:
        film_id.places -= 1
        #print(f"vos {nbplace} places sont réservées")
        print(f"il reste {film_id.places} places pour ce film ")
    else:
        print("il ne reste plus de places")


for i in films:
    print(i)

    places_var=StringVar()
    places_var.set(i.places)

    titre_label = Label(fenetre, text= i , textvariable=places_var,bg="#FFE4B5")
    titre_label.grid(row=i.nb,column=0)

    bouton = Button(fenetre,text="reserver",command=lambda num = i: click_btn(num))
    bouton.grid(row=i.nb,column=1)


#film_id = int(input("Choisir un film \n"))
#nbplace = int(input("nombre de place désirées?\n"))


fenetre.mainloop()

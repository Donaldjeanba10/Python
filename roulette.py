from random import randrange 


nombre_ordi = randrange(1,500)
chance = 5
 
print ("Choisir un nombre compris entre 1 et 500")
 
 while chance >=1 :
     nombre_choix = int(input("Choisir un nombre :"))
     if nombre_choix=nombre_ordi :
         print("Vous avez trouve le bon nombre.")
         break
     else: 
         if nombre_choix<nombre_ordi :
             print("Votre nombre est plus petit")
         else:
             print("Votre nombre est plus fort")
    chance -= 1
             print("Il vous reste:",chance,"essaie(s)")
             
print("le nombre choisi par l'ordinateur etait :",nombre_ordi)             

     

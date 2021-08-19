import random
import colored 
from colored import stylize 


# Begrüsung
print(stylize("herzlich willkomen zu schre stein papier!", colored.fg(4)))

spilen = "JA"
while spilen == "JA":

 # spiller wällen lassen
    spielerwarl = input("welle einen gegenstand: ")

    # computer wählt
    computerwal = random.choice(["schere", "stein", "patpier"])

  # wer hat gewonnen ?
     # if spielerwarl == "schre" and computerwal == "schre":
    if spielerwarl == "schere" and computerwal == "schere":
        print(stylize("Es ist Unenschiden", colored.fg(45)))
        print("Aufwiedersehen") 
    if spielerwarl == "stein" and computerwal == "stein":
        print(stylize("es ist Unenschiden", colored.fg(45)))
        print("Aufwiedersehen") 
    if spielerwarl == "papier" and computerwal == "papier":
        print(stylize("es ist Unenschiden", colored.fg(45)))
        print("Aufwiedersehen") 
    if spielerwarl == "stein" and computerwal == "schere":
        print(stylize("Du hast Gewonnen", colored.fg(221)))
        print("Aufwiedersehen") 
    if spielerwarl == "schere" and computerwal == "stein":
        print(stylize("Du hast Ferloren", colored.fg(9)))
        print("Aufwiedersehen") 
    if spielerwarl == "papier" and computerwal == "schere":
        print(stylize("Du hast Ferloren", colored.fg(9)))
        print("Aufwiedersehen") 
    if spielerwarl == "stein" and computerwal == "papier":
        print(stylize("Du hast Ferloren", colored.fg(9)))
        print("Aufwiedersehen") 
    if spielerwarl == "schere" and computerwal == "papier":
        print(stylize("Du hast Gewonnen", colored.fg(221)))
        print("Aufwiedersehen") 
    if spielerwarl == "papier" and computerwal == "stein":
        print(stylize("Du hast Ferloren", colored.fg(9)))
        print("Aufwiedersehen") 
      
        


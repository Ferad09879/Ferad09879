
import colored 
from colored import stylize 
from colored import fg
# begrüsung 
print(stylize("Hezlich willkommen zum Taschenrechner",fg(221)))

#frage den bunutzer nach einer zahl

Zahl1_string = input("Was ist die erste zahl :")
Zahl1 = int (Zahl1_string)
# frage den benutzer nach dem rechen zah und zweite zahl

rz = input("Was ist dein rechen zeichen :")

zahl2_string = input("Was ist die zweite zahl :")
zahl2 = int(zahl2_string)

if rz == "+":
    print(Zahl1 + zahl2)

if rz == "-":
    print(Zahl1 - zahl2)

if rz == "*":
    print(Zahl1 * zahl2)

if rz == "/" or rz == ":":
    print(Zahl1 / zahl2)


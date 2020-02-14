from random import random, randint

print("wikommen zum spiel schere stein papier \n 1=schere \n 2=stein \n 3=papier \n 4=brunnen ")
print("wähle deinen zug:")
zp = 0
zc = 0
while True:
    spieler = int(input())
    if spieler == "x":
        exit(0)
    computer = randint(1, 4)
    if spieler == computer:
        print("unentschieden")
    elif (spieler == 1 & computer == 3) | (spieler == 2 & computer == 1) | (
            spieler == 3 & computer == 2 | computer == 4) | (spieler == 4 & computer == 1 | computer == 2):
        print("glückwunsch du hast gewonnen")
        zp = zp + 1
    else:
        print("du hast leider verloren versuche es beim nächsten mal nochmal")
        zc = zc + 1
    print("Computer: " + computer + "\n Spieler: " + spieler)


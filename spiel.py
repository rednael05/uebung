from random import random, randint


def translate(zahl):
    if zahl == 1:
        return "Schere: "+str(zahl)
    elif zahl == 2:
        return "Stein: "+str(zahl)
    elif zahl == 3:
        return "Papier: "+str(zahl)
    elif zahl == 4:
        return "Brunnen: "+str(zahl)


if __name__ == '__main__':
    print("wikommen zum spiel schere stein papier \n 1=schere \n 2=stein \n 3=papier \n 4=brunnen ")
    print("wähle deinen zug:")
    zp = 0
    zc = 0
    while True:
        i = input()
        if i == "x":
            exit(0)
        spieler = int(i)
        if spieler < 1 or spieler > 4:
            print("ungültige eingabe")
            continue
        computer = randint(1, 4)

        if spieler == computer:
            print("unentschieden")
        elif (spieler == 1 and computer == 3) or \
                (spieler == 2 and computer == 1) or\
                (spieler == 3 and (computer == 2 or computer == 4)) or\
                (spieler == 4 and (computer == 1 or computer == 2)):
            print("glückwunsch du hast gewonnen: "+str(spieler)+":"+str(computer))
            zp = zp + 1
        else:
            print("du hast leider verloren versuche es beim nächsten mal nochmal")
            zc = zc + 1
        print("Computer: " + translate(computer) + "\n Spieler: " + translate(spieler))
        print("deine punkte " + str(zp) + " die punkte vom computer " + str(zc))

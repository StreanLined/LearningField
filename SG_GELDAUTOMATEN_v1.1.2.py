from math import trunc


inputpin = ()
pin = int(1234)
trypin = 3
kontostand = float(1000)
username = ()
aktion = ()
nachricht = (0)
auszahlung = int()
######################################################################################################
#Get name
def benutzer():
    global username
    print("\nBenutzername: ")
    if username == username:
        username = input(str())
        print("\nGuten Tag " + username + ", sie haben " + str(nachricht) + " Nachrichten")
    else:
        pass

#Ungültige aktion
def valid():
    global aktion
    print("\nBitte wählen sie eine aktion")
    aktion = input("Kontostand[1]    Geld abheben[2]     \n")
    if aktion == str(1):
        pass
    elif aktion == str(2):
        pass
    else:
        print("Ungültige aktion eingabe, versuchen sie es bitte erneut")
        valid()


#Aktion auswahl
def aktion_auswahl():
    global kontostand
    global auszahlung
    if aktion == str(1):
        print("Ihr Konto enthält: " + str(trunc(kontostand)) + "€")
    elif aktion == str(2):
        user_auszahlung()
        if kontostand == (0):
            print("You broke son...")
        else:
            pass
    else:
        print("Ungültige aktion eingabe, loggen sie sich bitte nochmal ein")

#Auszahlung
def user_auszahlung():
    global kontostand
    global auszahlung
    auszahlung = int(input("Wie viel würden sie gerne ausgezahlt haben?\n"))
    if auszahlung > kontostand:
        print("Es konnte nicht " + str(auszahlung) + "€ " + "ausgezahlt werden da ihr Konto einen Wert von "+ str(trunc(kontostand)) + "€ enthält" )
        print("Versuchen sie es bitte erneut")
        user_auszahlung()
    else:
        kontostand -= auszahlung
        print("Ausgezahlt: " + str(auszahlung) + "€")
        print("Ihr Konto enthält jetzt: " + str(trunc(kontostand)) + "€")

#Pin abfrage
def pin_abfrage():
    global trypin
    try:
        user_input = int(input("\nBitte geben sie ihre PIN ein: "))
    finally:
        if user_input != pin:
            trypin -= 1
            print("\nDie falsche PIN wurde eingegeben")
            print("Sie haben noch " + str(trypin) + " PIN versuche übrig")
        else:
            print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
            aktion_auswahl()
            quit()
####################################################################################################
#Main
benutzer()
valid()

while trypin >= 1:
    pin_abfrage()

while trypin == 0:
    print("\nKarte einbehalten & gesperrt. Wenden sie an ihrem Ansprechpartner um die Karte zurück zu enthalten.")
    quit()

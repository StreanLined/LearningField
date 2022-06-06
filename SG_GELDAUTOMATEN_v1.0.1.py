#Database
pin = int(1234)
puk = int(4321)
trypin = int(4)
trypuk = int(4)
user_input = int(0000)
kontostand = int(1001)
username = ()
Logged_in = False
a1 = 1
a2 = ()
nachricht = (0)

#Aktion auswahl
def aktion_auswahl():
    global kontostand
    if a2 == str(1):
        print("Ihr Konto enthält: " + str(kontostand) + "€")
    elif a2 == str(2):
        kontostand -= 1000
        print("Ausgezahlt: 1000€")
        print("Ihr Konto enthält jetzt: " + str(kontostand) + "€")
        if kontostand == (0):
            print("You broke son...")
        else:
            pass
    else:
        print("Ungültige aktion eingabe, loggen sie sich bitte nochmal ein")
    

#MotD
print("\n \n \n \n \n \n \n \n")
print("Wilkommen")

#Main
while Logged_in == False:
    if a1 == 1:
        #Get - Name
        print("\nBenutzername: ")
        if username == username:
            username = input(str())
            print("\nGuten Tag " + username + " sie haben " + str(nachricht) + " Nachrichten")
        else:
            pass
        
        trypin -= 1
        trypuk -= 1

        print("\nBitte wählen sie eine aktion")
        a2 = input("Kontostand[1]    Geld abheben[2] \n")

        #trypipn 3
        while trypin == 3:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuche übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    a1 -= 1
                    aktion_auswahl()
                    quit()
        #trypin 2   
        while trypin == 2:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuch übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    a1 -= 1
                    aktion_auswahl()
                    quit()
        #trypin 1
        while trypin == 1:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuche übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    a1 -= 1
                    aktion_auswahl()
                    quit()
        #trypin 0
        while trypin == 0:
                input("\nKarte einbehalten & gesperrt. Wenden sie an ihrem Ansprechpartner um die Karte zurück zu enthalten.")
                #nachricht = ("Ihre PIN wurde zu oft faslch eingegeben. Die Karte ist gesperrt")
                quit()
    else:
        Logged_in = True
quit()
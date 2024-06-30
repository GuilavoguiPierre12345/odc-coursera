#*Ecrire un script python permettant de tester les connaissances de bases des
#*opération mathématique élémentaires à l’aide des opérations suivantes :
#*X+4 =3 ;  X + 2= 2X -4 ;  y-3=4Y+4

import pyttsx3
engine = pyttsx3.init()
engine.say('Greetings!')
engine.say('How are you today?')
engine.runAndWait()


def tester_equation1():
    engine.say('Equation 1 : X + 4 = 3')
    engine.runAndWait()
    print("Equation 1 : X + 4 = 3")
    solution = -1  # Solution de l'équation X + 4 = 3
    while True:
        try:
            engine.say('Entrez la valeur de x')
            engine.runAndWait()
            reponse = float(input("Entrez la valeur de X : "))
            
            
            if reponse == solution:
                engine.say('Bonne reponse')
                engine.runAndWait()
                print("Bonne réponse!")
                break
            else:
                engine.say('Mauvaise reponse. Reessayez')
                engine.runAndWait()
                print("Mauvaise réponse. Réessayez.")
        except ValueError:
            engine.say('Veuillez entrer un nombre valide')
            engine.runAndWait()
            print("Veuillez entrer un nombre valide.")


def tester_equation2():
    engine.say('Equation 2 : X + 2 = 2X - 4')
    engine.runAndWait()
    print("Equation 2 : X + 2 = 2X - 4")
    solution = 6  # Solution de l'équation X + 2 = 2X - 4
    while True:
        try:
            engine.say('Entrez la valeur de X :')
            engine.runAndWait()
            reponse = float(input("Entrez la valeur de X : "))
            if reponse == solution:
                engine.say('Bonne reponse')
                engine.runAndWait()
                print("Bonne réponse!")
                break
            else:
                engine.say('Mauvaise réponse. Réessayez.')
                engine.runAndWait()
                print("Mauvaise réponse. Réessayez.")
        except ValueError:
            engine.say('Veuillez entrer un nombre valide.')
            engine.runAndWait()
            print("Veuillez entrer un nombre valide.")


def tester_equation3():
    engine.say('Equation 3 : Y - 3 = 4Y + 4')
    engine.runAndWait()
    print("Equation 3 : Y - 3 = 4Y + 4")
    solution = -7/3  # Solution de l'équation Y - 3 = 4Y + 4
    while True:
        try:
            engine.say('Entrez la valeur de Y :')
            engine.runAndWait()
            reponse = float(input("Entrez la valeur de Y : "))
            if reponse == solution:
                engine.say('Bonne reponse')
                engine.runAndWait()
                print("Bonne réponse!")
                break
            else:
                engine.say('Mauvaise réponse. Réessayez.')
                engine.runAndWait()
                print("Mauvaise réponse. Réessayez.")
        except ValueError:
            engine.say('Veuillez entrer un nombre valide.')
            engine.runAndWait()
            print("Veuillez entrer un nombre valide.")

# Test des équations
tester_equation1()
tester_equation2()
# tester_equation3()
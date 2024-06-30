import sys
# La gestion des erreurs 
''' 
    Cette partie nous aides a gerer les differents types d'erreur 
    par exemple si l'on demande a un utilisateur de mettre sont nom, lui il met sa
    date de naissance ou autres chose
'''
try: # essayer d'executer le code sans ce soucir de la sortie
    getfile = open("myfile", 'r')
    getfile.write("je suis guilavogui")
except IOError: # precision du type d'exception a capturer
    print("Input Output error: ")
except : # gestion globale des exceptions
    print("Une autre erreur")
else : # cette partie s'execute s'il n'y a pas eut d'exception
    print("Program finished successfully")
finally : # cette partie s'execute peut importe le resultat 
    # getfile.close()
    print("File is now closed")
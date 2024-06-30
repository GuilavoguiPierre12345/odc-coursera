# La manipulation des fichiers en python
# LECTURE DE FICHIER AVEC OPEN
'''
La fonction open() : pour ouvrir un fichier
    param1 : le chemin du fichier
    param2 : le mode d'ouverture du fichier
    file.name : afficher le nom du fichier
    file.mode : afficher le mode d'ouverture du fichier
    
    file.read(), file.write(value) : respectivement lire un fichier et ecrire dans un fichier
    file.readline() : pour une ligne dans le fichier
    file.readlines() : pour toutes les lignes du fichier
    lire tout le contenu du fichier en integralie
'''
file1 = open('file1.txt', 'r')
file1.close()

# La meilleur maniere d'ouvrir un fichier ce fait avec with
with open('file1.txt', 'r') as file_c :
    file_content = file_c.readline(4)
    print(file_content)
print(file_c.closed)
# print(file_content)

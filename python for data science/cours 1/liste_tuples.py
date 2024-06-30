# Tuples 
# my_tuple = 3,5,2,1,4.5,1.004
# my_tuple_1 = ('peter', 'yaboigui', 3,-3.4)
# print(my_tuple)

# Extraction (Slicing)
# extract_value = my_tuple[1:-1:1]
# print(extract_value)

# new_tuple = my_tuple
# print(sorted(new_tuple))

# Liste 
my_list = [ 1,3,'yaboigui', -3.4]
my_list_ext = [3,1,0]
my_list.extend(my_list_ext)
print("YABOIGUI".split('i'))
print(my_list)

# passage par references
# list_1 = [1,2,5]
# list_2 = list_1
# list_2[1]= 10
# print(list_1)

# copy d'une liste
list_a = [3,1,2.5]
list_a_cpy = list_a.copy() # out list_a[:]
print(list_a_cpy,end='\n')
print(list_a_cpy)
del list_a[0]
print(list_a,end='\n')

# quelques methodes des listes : 
list_a.append(1)  # ajoute une valeur a la fin de la liste
list_a.copy() # copie les elements de la liste dans une nouvelle liste
list_a.count(9) # compte le nombre d'occurence d'une valeur dans la liste
del list_a[0] # supprime l'element de la liste a l'index donne et  affiche le reste
list_a.extend(list_a_cpy) # extend utiliser pour ajouter plusieurs element a la liste
list_a.insert(2,'guilavogui') # insert, pour inserer une nouvelle valeur a l'indice precis
list_a.pop() # supprime le dernier element de la liste et affiche le reste
list_a.sort() # ordonner la  liste 

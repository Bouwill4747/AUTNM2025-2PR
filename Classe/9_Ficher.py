#Fichier 1

#CSV : comma sperated values
#CSV : compatible avec excel

# Ouverture de fichier en mode écriture
f = open("Data/data.csv", "w") # w = écrase
f.write("M, William, 1999 \n")

# Ouverture de fichier en mode appennd
f = open("Data/data.csv", "a") # a = ajoute la fin de ce qui existe
f.write("M, William, 1999 \n")

f.close()


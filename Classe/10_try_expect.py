# Les exceptionn : erreurs lors de l'execution du code

try:
    x= int(input("svp entrez un nombre : "))
    print(10/ x)

except ZeroDivisionError:
    print("Division par zero :: ")

except ValueError:
    print("Valeur invalide")

except Exception:
    print("Autre exception")
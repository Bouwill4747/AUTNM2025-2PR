# Les exceptionn : erreurs lors de l'execution du code

class AgeException(Exception):
    pass

def input_age():
    age = int(input("Age : "))
    if age < 0:
        raise ValueError("Age cannot be negative") # provoquer une exception volontaire ...
    return age

try:
    age = input_age()
except Exception as e:
    print("exceptoin...", e)

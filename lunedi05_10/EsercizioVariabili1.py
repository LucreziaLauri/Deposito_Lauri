nome = input("Inserisci il tuo nome: ")
numero= int(input("Inserisci un numero: "))
lettera = input("Inserisci un carattere: ")
numeroVirgola = float(input("Inserisci un numero con la virgola: "))
isTrue = bool(input("Inserisci valore: "))

print(nome, numero , lettera, numeroVirgola, isTrue)

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

print (num1 >= num2 or num1 != num2)
print (num1 == num2 and num1 >= num2)
print (not(num1>num2))
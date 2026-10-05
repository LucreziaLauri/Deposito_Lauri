# print variabili

nome="Lucrezia"
etá= 25
citta= "Roma"
print("Ciao, il mio nome è", nome, ", ho", etá, "anni", "e abito a", citta)

# Input da parte dell'utente

nome= input("Inserisci il tuo nome: ")
eta= int(input("Inserisci la tua età: ")) # int serve perche' input prende sempre stringhe, quindi se voglio fare operazioni matematiche devo convertire in int
print("Ciao, " + nome + "! benvenuta in python!")

#print operazioni

print(1+5)  # addizione
print(6-1)  # sottrazione
print(2*3)  # moltiplicazione
print(10/2) # divisione
print(3**2) # 3 alla seconda/ potenze

#print somma

x = int(input("Inserisci un numero: "))
y = int(input("Inserisci un altro numero: "))
print("la somma dei due numeri e'=", x + y)  
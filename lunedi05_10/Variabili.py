# Variabili e tipi in Python

s = "Lucrezia"
print(s[3]) #gli indici iniziano da 0, quindi s[3] è la quarta lettera della stringa
print(s[5]) 

saluto = "Ciao"
nomeCorso = "Python!"
messaggio = saluto + " " + nomeCorso # le virgolette servono per mettere uno spazio tra le due stringhe
print(messaggio)

#funzioni non integrate

s = "Lucrezia , ho 25 anni e abito a Roma"
print(s.upper()) #metodo upper() per trasformare la stringa in maiuscolo
print(s.lower()) #metodo lower() per trasformare la stringa in minuscolo
print(s.split(",")) #metodo split() per dividere la stringa in una lista di parole, in questo caso divido la stringa in base allo spazio"))
print(s.replace("Lucrezia", "Luca")) #metodo replace() per sostituire una parte della stringa con un'altra

#le funzioni integrate non hanno il punto
print(len(s)) #funzione len() per calcolare la lunghezza della stringa

# variabili booleane operatori di confronto

x = 77
y = 105

print(x > y) #False 
print(x < y) #True
print(x == y) #False 77 uguale a 105
print(x != y) #True 77 diverso da 105
print(x >= y) #False
print(x <= y) #True

#operatori logici
x = 90
y= 100
z= 60
print(y> x and x >z) #true tutte e due sono veri
print(y> x or z> x)# true almeno una delle due è vera
print (not(y>x)) # false perché y è maggiore di x, quindi not(y>x) è falso


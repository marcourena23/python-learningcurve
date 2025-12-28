import string

n = 0
# Para letras minúsculas
lista_minusculas = " " + string.punctuation  + string.digits + string.ascii_letters
lista_minusculas = list(lista_minusculas)

message = list(input("Enter a message to encrypt: "))

# check my message
for letter in message:
    print(letter, end="")
print()

# add character in list
for letter in message:
    lm = lista_minusculas.index(letter) + 1
    message[n] = lista_minusculas[lm]
    newMessage = message[n]
    n += 1
    print(newMessage, end="")
print()

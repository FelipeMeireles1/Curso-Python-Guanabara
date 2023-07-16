from random import randint
computador = randint(0, 10)
jogador = int(input("Qual número o computador está pensando?"))

while jogador != 5:
    print ("Você errou... Tente denovo!")
    jogador = int(input("Qual número o computador está pensando?"))
if jogador == 5:
    print("Você acerou!")
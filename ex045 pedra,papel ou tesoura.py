from random import randint

itens = ("pedra","papel","tesoura")

computador = randint (0, 2)

print ("Jogo do pedra,papel ou tesoura:")
print ("Escolha a sua opção:")
print ("[0] Pedra")
print ("[1] Papel")
print ("[2] Tesoura")
jogador = int(input("Qual é a sua jogada?"))

print ("-=" * 11)
print ("O computador jogou {}".format(itens[computador]))
print ("O Jogador jogou {}".format(itens[jogador]))
print ("-=" * 11)

if computador == 0: #pedra
    if jogador == 0:
        print ("Empatou!")
    elif jogador == 1:
        print ("Jogador Venceu")
    elif jogador == 2:
        print ("Computador Venceu!")
    else:
        print ("Jogada inválida!")
if computador == 1: #Papel
    if jogador == 1:
        print ("Empatou!")
    elif jogador == 2:
        print ("Jogador Venceu")
    elif jogador == 0:
        print ("Computador Venceu!")
    else:
        print ("Jogada inválida!")
if computador == 2: #Tesoura 
    if jogador == 2:
        print ("Empatou!")
    elif jogador == 0:
        print ("Jogador Venceu")
    elif jogador == 1:
        print ("Computador Venceu!")
    else:
        print ("Jogada inválida!")
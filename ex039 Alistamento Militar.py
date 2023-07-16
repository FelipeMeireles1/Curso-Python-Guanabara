nascimento = int(input("Digite o seu ano de nascimento:"))
idade = 2023 - nascimento

if idade < 18:
    print("Você ainda vai se alistar")
if idade == 18:
    print("É hora de se alistar!")
if idade > 18: 
    print("Passou do tempo de se alistar")
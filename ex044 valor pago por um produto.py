print ("Loja do Meireles")

preço = float(input("Digite o valor do produto:R$"))

print("Escolha a forma de pagamento:")
print("[1] Dinheiro/Cheque")
print("[2] 1x no Cartão")
print("[3] 2x no Cartão")
print("[4] 3x ou mais no cartão")

opção = int(input())

if opção == 1:
    print("Você recebeu um desconto de 10% no valor pago a vista:")
    print("O novo preço do produto é")
    print("R${:.0f}".format(preço-(preço*10/100)))
elif opção == 2:
    print("Você recebeu um desconto de 5% no valor pago no cartão:")
    print("O novo preço do produto é:")
    print("R${:.0f}".format(preço-(preço*5/100)))
elif opção == 3:
    print("Você não receberá desconto no valor pago em 2x no cartão:")
    print("O preço do produto vai ser o mesmo:")
    print("R${:.0f}".format(preço))
elif opção == 4:
    print("Você recebeu um acréscimo de 20% juros no cartão:")
    print("O novo preço do produto é:")
    print("R${:.0f}".format(preço+(preço*20/100)))
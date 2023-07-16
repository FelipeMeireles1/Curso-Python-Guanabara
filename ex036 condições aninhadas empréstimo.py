valor = float(input("Digite o valor da casa:"))
salario = float(input("Digite o seu salário:R$"))
anos = int(input("Em quantos anos você irá pagar:"))
mensal = anos * 12
prestação = valor / mensal

if prestação < (salario * 30 / 100):
    print("Empréstimo Aprovado!")
else:
    print("Empréstimo Negado!")
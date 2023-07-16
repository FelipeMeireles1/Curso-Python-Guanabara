num = str(input("Digite um número de 0 a 9999:"))
print("""
unidade:{}
dezena:{}
centena:{}
milhar:{}
""".format(num[3:4],num[2:3],num[1:2],num[0:1]))
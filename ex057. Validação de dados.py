sexo = str(input("Digite o seu sexo [M] ou [F]"))

while sexo not in "MmFf":
    print ("Você é burro? é M ou F!!!")
    sexo = str(input("Digite seu sexo:"))
print("Sexo {} registrado com sucesso!".format(sexo))

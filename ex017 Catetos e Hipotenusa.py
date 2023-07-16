import math

catetooposto = float(input("Digite o cateto oposto:"))
catetoadjacente = float(input("Digite o cateto adjacente:"))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print("A hipotenusa vai medir:{}".format(hipotenusa))


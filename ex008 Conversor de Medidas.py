metros = float(input("Digite a distância em metros:"))
print("Essa medida corresponde a:")
print("{:.0f}cm".format(metros*100))
print("{}km".format(metros/1000))
print("{}mm".format(metros*1000))
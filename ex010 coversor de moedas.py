real = float(input("Digite o valor em R$:"))
dolar = real * 4.80
euro = real * 5.38
libra = real * 6.29
print("Com R${:.0f} você pode comprar U${}".format(real, dolar))
print("Com R${:.0f} você pode comprar {} Euros".format(real, euro))
print("Com R${:.0f} você pode comprar {} Libras".format(real, libra))

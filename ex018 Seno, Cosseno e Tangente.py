import math

ang = int(input("Digite o ângulo:"))
radiano = math.radians(ang)
seno = math.sin(radiano) 
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print ("O seno desse ângulo é:{:.2f}".format(seno))
print ("O cosseno desse ângulo é:{:.2f}".format(cosseno))
print ("O tangente desse ângulo é:{:.2f}".format(tangente))
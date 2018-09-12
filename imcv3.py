from statistics import mode, mean, median, stdev, pstdev
peso=[57.7,73.4,67.8,72.2,72.8,76.8,75.5,80.3,82.5,84.1,90.4,84.5,82.9,85.0,84.9,83.1,82.5,81.6,77.8,74.2,71.8,67.6,65.4,76.0,62,63.5,63.2,77.2,66.7,78.7,66.7,79.1,81.6,82.5,92.8,90.7]
altura=[1.57,1.72,1.69,1.71,1.71,1.73,1.73,1.76,1.76,1.78,1.80,1.78,1.77,1.50,1.80,1.78,1.76,1.76,1.74,1.73,1.69,1.68,1.65,1.73,1.59,1.65,1.62,1.73,1.68,1.75,1.68,1.75,1.76,1.76,1.85,1.82]

pacientes2 = {}
for x in range(0, 36):
    pacientes2[x+1] = (peso[x], altura[x])

print(pacientes2)
imc = {}
for x in range(0, 36):
    imc[x+1] = peso[x]/(altura[x]*altura[x])

print("imc= ", imc)
freq_abs = [0 for i in range(7)]
for x in range(0, 36):
    if 0 <= imc[x+1] < 18.5:
        freq_abs[1] += 1
    if 18.5 <= imc[x+1] < 25.0:
        freq_abs[2] += 1
    if 25.0 <= imc[x+1] < 30.0:
        freq_abs[3] += 1
    if 30.0 <= imc[x+1] < 35.0:
        freq_abs[4] += 1
    if 35.0 <= imc[x+1] < 40.0:
        freq_abs[5] += 1
    if 40.0 <= imc[x+1] < 50.0:
        freq_abs[6] += 1

print("FREQ ABSOLUTA")
print('0<=18.5 - ', freq_abs[1])
print('18.5<=25.0 - ', freq_abs[2])
print('25.0<=30.0 - ', freq_abs[3])
print('30.0<=35.0 - ', freq_abs[4])
print('35.0<=40.0 - ', freq_abs[5])
print('40.0<=50.0 - ', freq_abs[6])
for x in range(1, len(freq_abs)):

    print(x+1, " ", freq_abs[x])

print("FREQ RELATIVA")
for x in range(1, len(freq_abs)):

    print(x, " ", freq_abs[x]/len(imc))

print("FREQ ACUMULADA")
total = 0
for x in range(1, len(freq_abs)):
    total += freq_abs[x]
    print(x, " ", total)

print("FREQ ACUMULADA")
total = 0
for x in range(0, len(freq_abs)):
    total += freq_abs[x]
    print(x, " ", (total/36)*100)

print('SEGUNDA QUESTAO')
print()
print('Altura: ', altura)
print('MEDIA DE ALTURA = ', mean(altura))
print("MEDIANA DE ALTURA = ", median(altura))
print("MODA DE ALTURA = ", mode(altura))
print('DESVIO PADRAO DE ALTURA = ', stdev(altura))
print("COEFICIENTE DE VARIACAO DE ALTURA = ", stdev(altura)/mean(altura))
print()
print('Peso: ', peso)
print('MEDIA DE PESO = ', mean(peso))
print("MEDIANA DE PESO = ", median(peso))
print("MODA DE PESO = ", mode(peso))
print('DESVIO PADRAO DE PESO = ', stdev(peso))
print("COEFICIENTE DE VARIACAO DE PESO = ", stdev(peso)/mean(peso))
print()
imc = list(imc.values())
print('Imc: ', imc)
print('MEDIA DE IMC = ', mean(imc))
print("MEDIANA DE IMC = ", median(imc))
print("MODA DE IMC = ", mode(imc))
print('DESVIO PADRAO DE IMC = ', stdev(imc))
print("COEFICIENTE DE VARIACAO DE IMC = ", stdev(imc)/mean(imc))
print()
print()
print('TERCEIRA QUESTAO')
print()
media_intervalos = [0 for i in range(7)]
media_intervalos[1] = 18.5/2
media_intervalos[2] = (18.5+25.0)/2
media_intervalos[3] = (25.0+30.0)/2
media_intervalos[4] = (30.0+35.0)/2
media_intervalos[5] = (35.0+40.0)/2
media_intervalos[6] = (40.0+50.0)/2
total = 0
total_freq = 0
for x in range(1, len(freq_abs)):
    total_freq += freq_abs[x]
    total += freq_abs[x]*media_intervalos[x]

print("MEDIA DO IMC AGRUPADO = ", total/total_freq)
# Grupo da mediana = 25-30
# Equação da mediana = L + (((n/2)-B)G)*w
# L = limite min do grupo da mediana = 25
# n é o total dos valores = 36
# B frequencia acumulada dos grupos de antes do grupo da mediana = 13
# G é a frequencia do grupo da mediana = 22
# w é o tamanho do grupo = 5
print('MEDIANA DO IMC AGRUPADO = ', (25+(((18-13)/22)*5)))
# Grupo modal = 25-30
# Equação da moda estimada = L + (F(m)-F(m-1))/(F(m)-F(m-1)+F(m)-F(m+1))
# L é o limite minimo do grupos
# F(m-1) é a frequencia do grupo antes do modal
# F(m) é a frequencia do grupo modal
# F(m+1) é a frequencia do grupo depois do modal
# w é o tamanho do grupo
print("MODA DO IMC AGRUPADO = ", 25+((22-13)/((22-13)+(22-0)))*5)
imc_agrupado = [0 for x in range(0, 6)]
for x in range(1, len(freq_abs)):
    imc_agrupado[x-1] = freq_abs[x]
print('DESVIO PADRAO DE IMC = ', pstdev(imc_agrupado), "   NAO SEI VER SE ISSO TA CERTO DA UMA CONFERIDA")
print("COEFICIENTE DE VARIACAO DE IMC = ", pstdev(imc_agrupado)/(total/total_freq), "   NAO SEI VER SE ISSO TA CERTO DA UMA CONFERIDA")

# CRIAR CONDIÇÕES DE VALORES
# USAR IF, ELIF E ELSE
valorp = float(input('Digite um valor:'))
valors = float(input('Digite um valor:'))

if valorp > valors:
    print(valorp,'é maior que',valors)

elif valorp == valors:
    print(valorp,'é igual a',valors)

else:
    print(valors,'é maior que',valorp)

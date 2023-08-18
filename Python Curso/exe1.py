"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
     numero = int(numero)
     if numero % 2 == 0:
       print(numero,'é par')
     else:
       print(numero,'é impar')
else:
    print(numero,'não é um número inteiro')

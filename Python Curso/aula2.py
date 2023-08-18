# CALCULANDO IMC, EXERCÍCIO CURSO PYTHON
nome = input('Qual é o seu nome?')
peso = float(input('Qual o seu peso em kg?'))
altura = float(input('Qual a sua altura em metros?'))
imc = peso / (altura*altura)
print('Oi',nome,'baseado em seu peso',peso,'e na sua altura de,',altura,'seu indíce de massa corporal é:',imc)
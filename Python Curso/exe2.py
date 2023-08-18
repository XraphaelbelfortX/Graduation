"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
horario = int(input('Que horas são? '))

if horario in range(0,12):
    print('Bom dia!')
elif horario in range(12,18):
    print('Boa Tarde')
if horario in range(18,24):
    print('Boa Noite')
    

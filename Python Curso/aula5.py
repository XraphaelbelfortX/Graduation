# AND, OR E NOT

entrada = input('[E]ntrar [S]air: ')
senha = input('Digite a senha: ') or 'Você não digitou a senha'
asenha = '123456'

if entrada == 'E' or entrada == 'e' and senha == asenha:
    print('Entrou')

elif entrada == 'S' or entrada == 's':
    print('Você foi desconectado')

else:
    print('Você foi desconectado')
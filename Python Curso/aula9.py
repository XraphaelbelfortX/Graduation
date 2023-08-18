"""
COSTANTE = variavel que não se altera de forma alguma
OBS: Muitas condições no if é considerado ruim
Quanto mais simples o código melhor e mais fácil de ser lido
"""

velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_radar = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade > RADAR_1:
    print('O carro passou da velocidade permitida')

if vel_carro_radar and carro_multado:
    print('Carro multado em radar 1')

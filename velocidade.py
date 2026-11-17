velocidade=float(input('digite a velocidade do veiculo'))
if velocidade < 80:
     print(f'O veículo passou a {velocidade} km/h, voce nao foi multado')
else:
    print(f'O veículo foi multado por excesso de velocidade: {velocidade} km/h')
print('Preço da maçã por unidade --> R$ 1,30')
print('Preço da maçã - caixa com 12 und --> R$ 1,00')
maca=int(input('Digite quantas maçãs você deseja:'))
if maca <=11:
    valor1=maca*1.30
    print('Suas compras custaram:',valor1)
else:
    valor2=maca*1
    print('Suas compras custaram:', valor2)
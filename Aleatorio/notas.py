n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
tp = float(input('Digite a nota do teste de progresso '))
r = (n1*4)/10 + (n2*4)/10 + (tp*2)/10
if r >= 7:
    print('Sua média foi {}, aprovado.'.format(r))
if r >= 3.5 and r <= 7:
    print('Sua média foi {}, reprovado com recupreção.'.format(r))
else:
    print('Sua média foi {}, reprovdo sem recupreção.'.format(r))
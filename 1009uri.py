nome = (input())
salario_fixo = float(input())
total_vendas = float(input())

porcentagem = float(total_vendas * (15/100))
salariobruto = salario_fixo + porcentagem

print('TOTAL = R$ %.2f'%salariobruto)

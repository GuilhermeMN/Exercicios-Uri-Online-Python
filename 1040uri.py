notas = input().split(" ")

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = float((n1*2 + n2*3 + n3*4 + n4*1) / 10)

if (media >= 7.0):
    print('Media: %.1f'%media)
    print('Aluno aprovado.')
elif (media < 5.0):
    print('Media: %.1f' % media)
    print('Aluno reprovado.')
elif (media >= 5.0 and media <= 6.9):
    print('Media: %.1f' % media)
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: %.1f'%exame)
    media_final = (media + exame)/2
    if (media_final >= 5.0):
        print('Aluno aprovado.')
        print('Media final: %.1f'%media_final)
    elif (media_final <= 4.9):
        print('Aluno reprovado.')
        print('Media final: %.1f'%media_final)

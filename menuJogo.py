def menu():
    print('+------------------------+')
    print('|  Jogo Da Advinhação    |')
    print('+------------------------+')
    print('\n'*2)
    print('+-------------------------+')
    print('|      a)fácil            |')
    print('|      b)médio            |')
    print('|      c)difícil          |')
    print('+-------------------------|')
    nivel = input('informe a letra do nivel desejado ----> ')
    print('\n'*1)
    print("Você Tem Apenas 3 Chances ")
    print('\n'*1)
    if nivel=='a':
        import facil
    elif nivel=='b':
        import medio
    else:
        import dificil
menu()        

import random
jogar_novamente = 'sim'
while jogar_novamente=='sim':
    pergunta = int(random.randint(1,50))
    print('Informe o Numero Mistérioso (entre 1 e 50)')
    for vezes in range(0,3):
        resposta = int(input('a resposta é -----> '))
        if (resposta == pergunta) :  
            print('PARABÈNS!!!, você Acertou !!! ')
            print('''
                    ☆┌─┐　 ─┐☆
                    　│▒│ /▒/
                    　│▒│/▒/
                    　│▒/▒/─┬─┐
                    　│▒│▒|▒│▒│
                    ┌┴─┴─┐-┘─┘
                    │▒┌──┘▒▒▒│
                    └┐▒▒▒▒▒▒┌┘
                    　└┐▒▒▒▒┌
             ''')
            break
        elif pergunta > resposta and vezes<2:
            print('O Numero Mistérioso é Maior Que Esse')
        elif pergunta < resposta and vezes<2:
            print("O Número Misterioso é Menor que Esse")

        elif  pergunta != resposta and vezes==2:
            print('Infelizmente você perdeu')
            print('o numero correto era', pergunta)
    jogar_novamente = input('deseja jogar novamente: SIM ou NÃO \n')
if jogar_novamente== 'nao':
    import menuJogo
    menuJogo.menu()
    print('\n'*2)
        


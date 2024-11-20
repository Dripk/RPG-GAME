print('Bem vindo ao jogo!')

inventario = []

while True:

    print('\n1. Ir para a cabana')
    print('2. Ir para a floresta')
    print('3. Sair do jogo')
    print('4. Ver inventário')
    
    escolha = int(input('\n Qual é sua escolha: '))

    if escolha == 1: #bloco de código *CABANA*
        print('\nA cabana tem uma espada')
        print('1. Pegar espada')
        print('2. Ignorar espada')
        print('3. Voltar para a floresta')
        
        espada = int(input('O que você faz? '))
        
        if espada == 1:
            inventario.append('Espada')
            print('O jogador conseguiu uma espada!')
        elif espada == 2:
            print('Seu inventário está vazio!')
        elif espada == 3:
            print('Você voltou para a floresta!')
        else:
            print('Número inválido!') #Fim do codígo *CABANA*

    elif escolha == 2:
        print('Você está na floresta escura!')
        print('\n A floresta tem um kit médico')
        print('1. Pegar o kit médico')
        print('2. Ignorar o kit médico')
        print('3. Voltar para a cabana')
        
        kit_medico = int(input('O que você faz? '))
        
        if kit_medico == 1:
            inventario.append('Kit médico')
            print('O jogador conseguiu um kit médico!')
        elif kit_medico == 2:
            print('Você ignorou o Kit médico!')
        elif kit_medico == 3:
            print('Você voltou para a cabana!')
        else:
            print('Número inválido!')
                   
    elif escolha == 3:
        print('Você saiu do jogo!')
        break
    
    elif escolha == 4:
        print('Seu inventário: ')
        for item in inventario:
            print(f'{item}')
       
    else:
        print('Número inválido!')
feitos = []
desfeitos = []
lista_tarefas = []


def adiciona():
    tarefa = input('Qual o nome da tarefa ? ')
    lista_tarefas.append(tarefa)
    feitos.append(tarefa)
    print(f"A tarefa: {tarefa}, foi adicionada com sucesso")


def lista():
    if lista_tarefas == []:
        return print('A sua lista está vazia')
    else:
        return print(lista_tarefas)


def apaga():
    if lista_tarefas == []:
        return print('Não há tarefas para serem apagadas')
    else:
        removido = lista_tarefas.pop()
        desfeitos.append(removido)
        return print(f'Você removeu com sucesso a tarefa {removido}')


def desfazer():
    if desfeitos == []:
        return print('Não há comandos para desfazer')
    else:
        refazer = desfeitos.pop()
        lista_tarefas.append(refazer)
        feitos.append(refazer)
        return print(f'Você acabou de desfazer a ulima tarefa {refazer}')


def lista_tudo():
    if lista_tarefas == [] and feitos == [] and feitos == []:
        return print('Não há nada nas suas listas.')
    else:
        return print(
            f'Sua lista de tarefas contém: {lista_tarefas}\n Sua lista de comandos feitos contém: {feitos} Sua lista de comandos desfeitos contém: {desfeitos}')


def menu():
    menu = True
    while menu:
        print(""""
        Escolha uma tarefa:\n
        1- Adicionar tarefa
        2- listar tarefa(s)
        3- Apagar a ultima tarefa
        4- Desfazer
        5- Listar tudo
        6- Sair
        """)
        print('-' * 50)
        try:
            menu = input("Escolha uma opção: ")
            if menu == '1':
                adiciona()
            elif menu == '2':
                lista()
            elif menu == '3':
                apaga()
            elif menu == '4':
                desfazer()
            elif menu == '5':
                lista_tudo()
            elif menu == '6':
                print("Tchau")
                menu = False
            elif menu != '':
                print('Algo deu errado, escolha outra opção ou aperte 5 para sair')
        except Exception:
            print("Algo deu errado")
            menu = False


menu()

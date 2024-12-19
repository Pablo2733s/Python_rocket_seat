def adicionar_tarefa(tarefas, nome_tarfera):
    # tarefa: nome da tarefa
    # completada: indica se a chave foi completada ou não

    tarefa = {"tarefa": nome_tarfera, "completada": False,}
    tarefas.append(tarefa)
    print(f'A tarefa {nome_tarfera} foi adiciona com sucesso')
    return 

def ver_tarefas(tarefas):
     print('\n Lista de tarefas:')
     for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa["completada"] else ""
        nome_tarefa = tarefa["tarefa"]
        print(f'{indice}. [{status}] {nome_tarefa}')
        

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa ):
     indice_tarefa_ajustado = int(indice_tarefa) -1

     if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas): 
        tarefas[indice_tarefa_ajustado] ["tarefa"] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa}, atualizada para {novo_nome_tarefa}')  
     else:
          print('Indice de tarefa inválido')
     return

def completar_tarefa(tarefas, indice_tarefa):
     indice_tarefa_ajustado = int(indice_tarefa) -1
     tarefas[indice_tarefa_ajustado] ["completada"] = True
     print(f'Tarefa {indice_tarefa} marcada como completada')
     return

def deletar_tarefas_completadas(tarefas):     
     for tarefa in tarefas:
          if tarefa["completada"]:
            tarefas.remove(tarefa)
     print('Tarefas completadas foram deletadas.')
     return

tarefas = []
while True:
    print('\n Menu de Gerenciador de lista de tarefas')
    print('1. Adicionar tarefa')
    print('2. Ver tarefa')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar tarefa')
    print('6. Sair')

    escolha = int(input('Digite a sua escolha '))
    if (escolha == 1):
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
        print(f'Tarefa {nome_tarefa} foi adicionada com sucesso')
        ver_tarefas(tarefas)
    
    elif (escolha == 2):
        ver_tarefas(tarefas)
    
    elif (escolha == 3):
         ver_tarefas(tarefas)
         indice_tarefa = int(input('Digite o numero da tarefa que deseja atualizar: '))
         novo_nome = input('Digite o novo nome da tarefa: ')
         atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif (escolha == 4):
         ver_tarefas(tarefas)
         indice_tarefa = int(input('Digite o numero da tarefa que deseja completar: '))
         completar_tarefa(tarefas, indice_tarefa)
    elif (escolha == 5):
         deletar_tarefas_completadas(tarefas)
         ver_tarefas(tarefas)

    elif (escolha == "6"):
            break    
    
    else: 
         print('Você digitou um numero que não está na lista deseja retornar?')
         print('\n Se sim clique 1 se não clique 2')
         cliqueUsuario = int(input(''))
         if (cliqueUsuario == 1):
              continue
         else: 
              print(f'Você fechou o programa de lista de tarefas')
              break




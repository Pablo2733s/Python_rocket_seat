# Python_rocket_seat 🚀

# Gerenciador de Tarefas 📝

Este é um gerenciador de tarefas simples implementado em Python. O programa permite que você adicione, veja, atualize, complete e delete tarefas de uma lista. Ele foi projetado para ser fácil de usar e pode ser expandido conforme necessário.

![image](https://github.com/user-attachments/assets/18732a55-7276-4a70-9170-f3d3915c5cd1)



## Funcionalidades ⚙️

- **Adicionar Tarefa**: Permite adicionar uma nova tarefa à lista.
- **Ver Tarefas**: Exibe a lista de tarefas com informações sobre sua conclusão.
- **Atualizar Tarefa**: Permite alterar o nome de uma tarefa existente.
- **Completar Tarefa**: Marca uma tarefa como concluída.
- **Deletar Tarefas Completadas**: Deleta todas as tarefas que estão marcadas como concluídas.
- **Menu de Opções**: O usuário pode navegar pelo menu de opções, escolher o que deseja fazer e realizar as ações com facilidade.

## Como usar 💻

1. Clone o repositório:

   ```bash
   [git clone https://github.com/Pablo2733s/Python_rocket_seat.git](https://github.com/Pablo2733s/Python_rocket_seat.git)
Navegue até o diretório do projeto:

bash
Copiar código
cd nome-do-diretorio
Execute o script Python:

bash
Copiar código
python index.py
No menu, você verá as seguintes opções:

1: Adicionar tarefa
2: Ver tarefas
3: Atualizar tarefa
4: Completar tarefa
5: Deletar tarefa completada
6: Sair do programa
Exemplos de Uso
1. Adicionar Tarefa
Ao escolher a opção 1, o programa pedirá que você insira o nome da tarefa. A tarefa será adicionada à lista.

bash
Copiar código
Digite o nome da tarefa que deseja adicionar: Jogar bola
A tarefa Jogar bola foi adicionada com sucesso
2. Ver Tarefas
Ao escolher a opção 2, o programa exibirá todas as tarefas com seu status (completa ou não).

bash
Copiar código
Lista de tarefas:
1. [ ] Jogar Bola
3. Atualizar Tarefa
Escolha a opção 3, digite o número da tarefa e o novo nome para atualizar.

bash
Copiar código
Digite o numero da tarefa que deseja atualizar: 1
Digite o novo nome da tarefa: Comprar pão
Tarefa 1, atualizada para Comprar pão
4. Completar Tarefa
Escolha a opção 4 para marcar uma tarefa como completa.

bash
Copiar código
Digite o numero da tarefa que deseja completar: 1
Tarefa 1 marcada como completada
5. Deletar Tarefas Completadas
Escolha a opção 5 para excluir as tarefas que foram marcadas como concluídas.

bash
Copiar código
Tarefas completadas foram deletadas.
Como o código funciona
Funções:
adicionar_tarefa(tarefas, nome_tarfera):

Adiciona uma nova tarefa ao tarefas como um dicionário com duas chaves: "tarefa" e "completada". O valor da chave "completada" é False por padrão.
ver_tarefas(tarefas):

Exibe todas as tarefas na lista com seu número, nome e status (se foi completada ou não).
atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):

Atualiza o nome de uma tarefa existente, dado o índice da tarefa e o novo nome.
completar_tarefa(tarefas, indice_tarefa):

Marca a tarefa indicada como completada, alterando o valor de "completada" para True.
deletar_tarefas_completadas(tarefas):

Remove todas as tarefas que estão marcadas como completadas da lista.
Contribuição
Sinta-se à vontade para fazer um fork deste projeto, enviar pull requests ou abrir problemas para melhorias e correções de bugs.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

### Explicação do README:

1. **Título e descrição**: Um título para o projeto e uma breve explicação do que ele faz.
2. **Funcionalidades**: Descrição das funcionalidades do programa.
3. **Como usar**: Passos simples de como clonar e rodar o programa.
4. **Exemplos de uso**: Exemplos do que acontece quando o usuário escolhe cada opção do menu.
5. **Como o código funciona**: Explicação das principais funções no código.
6. **Contribuição**: Incentivo à contribuição de outros desenvolvedores.
7. **Licença**: Licença do código, geralmente a MIT, mas pode ser alterada conforme a sua escolha.

# Trilha-Python-IA-Backend-Dev
Aqui está um resumo detalhado do que cada parte do código faz:

Funções de Operações Bancárias:
  sacar: Realiza a operação de saque verificando se o valor não excede o saldo, o limite diário ou o número de saques permitidos.
  depositar: Realiza a operação de depósito adicionando o valor ao saldo e registrando no extrato.
  visualizar_extrato: Exibe todas as operações realizadas e o saldo atual.
  
Funções de Gerenciamento de Clientes e Contas:
  criar_cliente: Cria um novo cliente com nome, data de nascimento, CPF e endereço, garantindo que o CPF seja único.
  criar_conta_corrente: Cria uma nova conta corrente para um cliente existente, vinculando-a ao cliente e atribuindo um número de conta sequencial.
  listar_usuarios_e_contas: Lista todos os clientes cadastrados juntamente com as informações de suas contas correntes.
  
Sistema Bancário:
  Estruturas de Dados:
    clientes: Um dicionário para armazenar informações dos clientes, usando o CPF como chave.
    contas: Uma lista para armazenar as contas correntes.
    numero_conta: Um contador para atribuir números sequenciais às contas.
    
  Variáveis de Controle:
    saldo, limite, extrato, numero_saques, LIMITE_SAQUES: Controlam as operações bancárias como saldo disponível, limite diário de saque, histórico de operações e limites de saque diário.
    
  Menu Interativo:
    Um menu de texto permite ao usuário selecionar as operações desejadas. As opções incluem criar cliente, criar conta corrente, depositar, sacar, visualizar extrato, listar usuários e contas, e sair do sistema.

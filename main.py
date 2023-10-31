#Laboratório de Programação
#Projeto - Ecoenergy

limite_minimo = {
    'gasolina': 100,
    'alcool': 50,
    'diesel': 100,
    'energia solar': 20
}

estoque = {
    'gasolina': 1000,
    'alcool': 800,
    'diesel': 1200,
    'energia solar': 500
}

estoque02 = {
    'gasolina': {'quantidade': 1000, 'preco': 3.50},
    'alcool': {'quantidade': 800, 'preco': 2.00},
    'diesel': {'quantidade': 1200, 'preco': 2.80},
    'energia solar': {'quantidade': 500, 'preco': 1500.00}
}

vendas = {}
alertas = []
energia_solar_gerada = 0


#1º Módulo - Controle de Estoque de Produtos
def ControleDeEstoqueDeProdutos():

    while True:

        print('\nNíveis de Estoque em Tempo Real:\n')

        for produto, nivel in estoque.items():
            print(f"{produto}: {nivel}")

        print('\nControle de Estoque De Produtos:\n')

        print('1. Abastecimento de Produtos')
        print('2. Venda de Produtos')
        print('3. Nível de Estoque de Produtos')
        print('4. Voltar')

        opcao = int(input('\n-> Escolha a opção desejada: '))

        if opcao == 1:
            produto = str(input('\nDigite o produto recebido: ')).lower()
            quantidade = int(input('Digite a quantidade recebida: '))

            estoque[produto] += quantidade

            print(f'\n{quantidade} unidades de {produto} recebidas com sucesso!')

        elif opcao == 2:
            produto = str(input('\nDigite o produto a ser vendido: ')).lower()
            quantidade = int(input('Digite a quantidade a ser vendido: '))

            if estoque[produto] >= quantidade:

                estoque[produto] -= quantidade

                print(f'\n{quantidade} unidades de {produto} vendidos com sucesso!')

            else:
                print(f'\nQuantidade insuficiente de {produto} em estoque!')

        elif opcao == 3:

            print()

            for produto, nivel in estoque.items():

                if nivel <= limite_minimo[produto]:
                    print(f'ALERTA: Nível de {produto} atingiu o limite mínimo!')

                else:
                  print(f'ALERTA: {produto} em estoque!')

        elif opcao == 4:
            print()
            break

        else:
            print('\n-> Opção inválida! Tente novamente.')


#2º Módulo - Gerenciamento de Serviços Automotivos
def GerenciamentoDeServiçosAutomotivos():

    agendamento = []
    historico = {}

    while True:

        print('\nGerenciamento de Serviços Automotivos:\n')
        print('1. Agendar Serviço')
        print('2. Registrar Detalhes de Serviço')
        print('3. Acessar Histórico de Serviços')
        print('4. Voltar')

        opcao = int(input('\n-> Escolha a opção desejada: '))

        if opcao == 1:

            veiculo = input('\nDigite a placa do veículo: ')
            data = input('Digite a data e horário para o serviço (ex: 01/01/2023 12:00): ')
            mecanico = str(input('Digite o nome do mecânico: ')).strip().capitalize()

            agendamento.append({'veiculo': veiculo, 'data': data, 'mecanico': mecanico})

            print('\nServiço agendado com sucesso!')

        elif opcao == 2:

            veiculo = input('\nDigite a placa do veículo: ')
            data = input('Digite a data e horário do serviço (ex: 01/01/2023 12:00): ')
            servico_realizado = str(input('Descreva o serviço realizado: '))
            pecas_utilizadas = input('Liste as peças utilizadas: ')


            if veiculo in historico:
                historico[veiculo].append({'data': data, 'servico': servico_realizado, 'pecas': pecas_utilizadas})

            else:
                historico[veiculo] = [{'data': data, 'servico': servico_realizado, 'pecas': pecas_utilizadas}]

            print('\nDetalhes do serviço registrados com sucesso!')

        elif opcao == 3:

            veiculo = input('\nDigite a placa do veículo para acessar o histórico de serviços: ')

            if veiculo in historico:

                print('\nHistórico de Serviços para o veículo', veiculo)

                for servico in historico[veiculo]:
                    print(f"Data: {servico['data']}")
                    print(f"Serviço Realizado: {servico['servico']}")
                    print(f"Peças Utilizadas: {servico['pecas']}")

            else:
                print('\nNenhum serviço registrado para este veículo.')

        elif opcao == 4:
            print()
            break

        else:
            print('\nOpção inválida! Tente novamente.')


#3º Módulo - Gestão de Mercearia
def criar_produto():

    nome = str(input('\nDigite o nome do novo produto: ')).strip().lower()
    quantidade = int(input('Digite a quantidade inicial: '))
    preco = float(input('Digite o preço por unidade: '))

    if nome not in estoque02:
        estoque02[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f'\n-> Produto {nome} criado com sucesso!')

    else:
        print(f'\n-> Produto {nome} já existe no estoque.')


def registrar_venda(produto, quantidade):

    if produto in estoque02 and estoque02[produto]['quantidade'] >= quantidade:

        if produto in vendas:
            vendas[produto]['quantidade'] += quantidade

        else:
            vendas[produto] = {'quantidade': quantidade, 'receita': 0}

        estoque02[produto]['quantidade'] -= quantidade
        vendas[produto]['receita'] += quantidade * estoque02[produto]['preco']

        print(f'\n-> {quantidade} unidades de {produto} vendidas com sucesso!')

    else:
        print(f'\n-> Quantidade insuficiente de {produto} em estoque ou o produto não existe.')


def analisar_desempenho_produto(produto):

    if produto in vendas:
        quantidade_vendida = vendas[produto]['quantidade']
        receita_total = vendas[produto]['receita']
        print(f'\nAnálise de desempenho para {produto}:')
        print(f'Quantidade Vendida: {quantidade_vendida} unidades')
        print(f'Receita Total: R${receita_total:.2f}')

    else:
        print(f'\nProduto {produto} não possui vendas registradas.')


def alerta_reposicao():

    for produto, info in estoque02.items():
        quantidade = info['quantidade']

        if quantidade <= limite_minimo.get(produto, 0):
            print(f'ALERTA: Nível de {produto} atingiu o limite mínimo, precisamos repor!. Estoque atual: {quantidade}')


def ControleDeEstoqueDeProdutos02():

    while True:

        print('\nNíveis de Estoque em Tempo Real:\n')

        for produto, info in estoque02.items():
            print(f"{produto}: {info['quantidade']} unidades - Preço: R${info['preco']:.2f}")

        print('\nGestão de Mercearia:\n')
        print('1. Criar Novo Produto')
        print('2. Abastecimento de Produto')
        print('3. Venda de Produto')
        print('4. Análise de Produto')
        print('5. Inspeção de Estoque')
        print('6. Voltar')

        acao = int(input('\nSelecione a opção que você deseja: '))

        if acao == 1:
            criar_produto()

        elif acao == 2:
            produto = input('\nDigite o produto recebido: ').strip().lower()
            quantidade = int(input('Digite a quantidade recebida: '))

            if produto in estoque02:
                estoque02[produto]['quantidade'] += quantidade
                print(f'\n-> {quantidade} unidades de {produto} recebidas with success.')

            else:
                print(f'\n-> Produto {produto} não encontrado no estoque.')

        elif acao == 3:
            produto = input('\nDigite o produto a ser vendido: ').strip().lower()
            quantidade = int(input('Digite a quantidade a ser vendida: '))
            registrar_venda(produto, quantidade)

        elif acao == 4:
            produto = input('\nDigite o produto a ser analisado: ').strip().lower()
            analisar_desempenho_produto(produto)

        elif acao == 5:
            alerta_reposicao()

        elif acao == 6:
            print()
            break

        else:
            print('\Opção inválida. Tente novamente.\n')


#4º Módulo - Monitoramento Energético
def MonitoramentoEnergetico():

  alertas = []

  def adicionar_energia_solar(quantidade_energia):

      nonlocal alertas

      alertas = []

      global energia_solar_gerada
      energia_solar_gerada += quantidade_energia

  def analisar_desempenho_energia_solar():

      if energia_solar_gerada > 0:
          eficiencia = energia_solar_gerada / 1000
          economia = eficiencia * 0.75

          return f'Energia solar gerada: {energia_solar_gerada} kWh\nEficiência: {eficiencia:.2f} kW\nEconomia estimada: R$ {economia:.2f}'

      else:
          return 'Nenhuma energia solar gerada.'

  def alerta_baixa_geracao_solar():

      nonlocal alertas

      if energia_solar_gerada < 500:
          alertas.append('\nBaixa geração de energia solar')

      return alertas

  while True:

      print('\nMonitoramento Energético:\n')
      print('1. Adicionar energia solar gerada')
      print('2. Análise de desempenho da energia solar')
      print('3. Alertas de baixa geração de energia solar')
      print('4. Voltar')

      opcao = int(input('\n-> Escolha a opção desejada: '))

      if opcao == 1:
          quantidade_energia = float(input('\nDigite a quantidade de energia solar gerada (em kWh): '))
          adicionar_energia_solar(quantidade_energia)

          print(f'\n{quantidade_energia} kWh de energia solar adicionados com sucesso!')

      elif opcao == 2:
          resultado_analise = analisar_desempenho_energia_solar()

          print()
          print(resultado_analise)

      elif opcao == 3:
          alertas = alerta_baixa_geracao_solar()

          if alertas:

              for alerta in alertas:
                  print(alerta)

          else:
              print('\nNenhum alerta de baixa geração de energia solar.')

      elif opcao == 4:
          print()
          break

      else:
          print('\nOpção inválida! Tente novamente.\n')


#Módulo 05 - Relatórios e Análises
def relatorios_analises():

  vendas_diarias = {}
  vendas_mensais = {}
  servicos_automotivos = {}
  energia_solar = {
      "energia_gerada": 0,
      "gasto_estimado": 0,
      "economia_estimada": 0,
  }

  while True:

      print("\nRelatórios e Análises:\n")
      print("1. Registrar Venda")
      print("2. Registrar Serviço Automotivo")
      print("3. Adicionar Energia Solar")
      print("4. Analisar Desempenho Energético")
      print("5. Sair")

      opcao = input("\nEscolha a opção desejada: ")

      if opcao == "1":
          produto_servico = str(input("\nNome do Produto/Serviço: "))
          valor = float(input("Valor da Venda: "))
          data = input("Data da Venda (AAAA-MM-DD): ")

          if data not in vendas_diarias:
              vendas_diarias[data] = 0
              vendas_diarias[data] += valor

          mes = data[:7]

          if mes not in vendas_mensais:
              vendas_mensais[mes] = 0
              vendas_mensais[mes] += valor

              print("\nVenda registrada com sucesso!")

      elif opcao == "2":
          tipo_servico = str(input("\nTipo de Serviço Automotivo: "))
          tempo_execucao = float(input("Tempo de Execução (minutos): "))
          satisfacao_cliente = float(input("Satisfação do Cliente (1-5): "))

          if tipo_servico not in servicos_automotivos:
              servicos_automotivos[tipo_servico] = {
                  "total_tempo_execucao": 0,
                  "total_clientes": 0,
              }

          servicos_automotivos[tipo_servico]["total_tempo_execucao"] += tempo_execucao
          servicos_automotivos[tipo_servico]["total_clientes"] += 1

          print("\nServiço automotivo registrado com sucesso!")

      elif opcao == "3":
          quantidade_energia = float(input("\nQuantidade de Energia Solar Gerada (kWh): "))
        
          economia_estimada = quantidade_energia * 0.25
          gasto = quantidade_energia * 0.75
          energia_solar["energia_gerada"] += quantidade_energia
          energia_solar["gasto_estimado"] += gasto
          energia_solar["economia_estimada"] += economia_estimada

          print("\nEnergia solar adicionada com sucesso!")

      elif opcao == "4":

          if energia_solar["energia_gerada"] > 0:
              eficiencia = energia_solar["energia_gerada"] / 1000
              gasto = energia_solar["gasto_estimado"]
              economia = energia_solar["economia_estimada"]

              print(f'\nEnergia solar gerada: {energia_solar["energia_gerada"]} kWh\nEficiência: {eficiencia:.2f} kWh\nGasto estimado: R$ {gasto:.2f}\nEconomia estimada: R$ {economia:.2f}')

          else:
              print('\nNenhuma energia solar gerada.')

      elif opcao == "5":
          print()
          break

      else:
          print("\nOpção inválida! Tente novamente.")


#Função principal
while True:

  print('=' * 22)
  print('Bem-Vindos a EcoEnergy')
  print('=' * 22)

  print('1. Controle de Estoque de Produtos')
  print('2. Gerenciamento de Serviços Automotivos')
  print('3. Gestão de Mercearia')
  print('4. Monitoramento Energético')
  print('5. Relatórios/Análises')
  print('6. Sair')

  try:
      opcao = int(input('\n-> Selecione a opção que você deseja: '))
  except ValueError:
      print('\nOpção inválida! Por favor, digite apenas números entre 1 e 6.\n')
      continue

  if opcao == 1:
    ControleDeEstoqueDeProdutos()

  elif opcao == 2:
    GerenciamentoDeServiçosAutomotivos()

  elif opcao == 3:
    ControleDeEstoqueDeProdutos02()

  elif opcao == 4:
      MonitoramentoEnergetico()

  elif opcao == 5:
      relatorios_analises()

  elif opcao == 6:
    print('\nA EcoEnergy agradece a preferência, volte sempre!\n')
    break

  else:
    print('\nOpção inválida! Tente novamente.\n')

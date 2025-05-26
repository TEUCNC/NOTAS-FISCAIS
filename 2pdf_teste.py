import os
import platform
from fpdf import FPDF
from time import sleep
from datetime import datetime
from colorama import Fore, Style, init

init()
# Inicializa o colorama

# Definindo as cores
fvermelha = Fore.RED
fverde = Fore.GREEN
famarela = Fore.YELLOW
fazul = Fore.BLUE
fpreto = Fore.BLACK
fmagenta = Fore.MAGENTA
fciano = Fore.CYAN
fbranco = Fore.WHITE

# Cores claras
fvermelhaclaro = Fore.LIGHTRED_EX
fverdeclaro = Fore.LIGHTGREEN_EX
famarelaclaro = Fore.LIGHTYELLOW_EX
fazulclaro = Fore.LIGHTBLUE_EX
fpretoclaro = Fore.LIGHTBLACK_EX
fmagentaclaro = Fore.LIGHTMAGENTA_EX
fcianoclaro = Fore.LIGHTCYAN_EX
fbrancoclaro = Fore.LIGHTWHITE_EX

# Estilos adicionais
negrito = Style.BRIGHT
apagado = Style.DIM
normal = Style.NORMAL
reste = Style.RESET_ALL

# lista onde os dados dos produtos vendidos são armazenado
itens = []

# VARIAVEL PARA SOMAR TODAS AS COMPRAS
soma_precos = 0

# Lista onde os dados de cliente fisico são armazenados
pessoa_dados = []

# Lista onde os dados da empresa são armazenados
empresa_dados = []

# Lista que armazena qual foi a modalidade de entrega
modalidade_entrega = []

"""# Fonte da venda
modalidade_venda = []"""

# Lista que armazena qual foi a modalidade de venda
modalidade_venda = []

# Lista que armazena qual foi a observação adicionada
observacao = []


# Def para limpar tela
def limpartela():
    sistema = platform.system()

    # Verificar qual sistema operacional está sendo executado
    if sistema == "Windows":
        # Comando para limpa o terminal no Windows
        comando = "cls"
    elif sistema == "Darwin":
        # Comando para limpa o terminal no macOS
        comando = "clear"
    elif sistema == "Linux":
        # Comando para limpa o terminal no Linux
        comando = "sudo apt-get autoclean"
    else:
        # Caso o sistema operacional não seja reconhecido
        comando = None

        # Executar o comando, se definido
    if comando:
        os.system(comando)
    print(f"{famarela}Software desenvolvido por: TEUCNC's Technology Solutions{negrito}{reste}")

# Serve para não permitir que a variavel seja vaiza
def naovazia(prompt):
    while True:
        entrada = input(prompt).strip()
        # Remove espaços em branco ao redor
        if entrada:
            return entrada
        print("Este campo é obrigatório!! Tente novamente.\n \n")
        sleep(1)


# Serve para verificar se o valor digitado for um número inteiro
def verif_num(prompt):
    while True:
        try:
            entrada_num = int(input(prompt))  # Tenta converter a entrada para número inteiro
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número inteiro válido.\n \n")  # Mostra mensagem de erro para entrada inválida
            sleep(1)


# Serve para verificar se o valor digitado for um número inteiro ou vazio
def verif_num_pode_vazio(prompt):
    while True:
        entrada = input(prompt).strip()  # Remove espaços em branco no início e fim
        if entrada == "":  # Permite o campo vazio
            return " -- "  # Retorna None se o campo for deixado em branco
        try:
            entrada_num = int(entrada)  # Tenta converter a entrada para número inteiro
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número inteiro válido ou deixe em branco.\n")


# Serve para verificar se o valor digitado é número com virgula
def verif_num_virgula(prompt):
    while True:
        try:
            entrada_num = float(input(prompt))  # Tenta converter a entrada para número inteiro
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número válido.\n \n")  # Mostra mensagem de erro para entrada inválida
            sleep(1)


# Serve para verificar se o valor digitado é número com virgula
def verif_num_virgula_pode_vazio(prompt):
    while True:
        entrada = input(prompt).strip()  # Remove espaços em branco no início e fim
        if entrada == "":  # Permite o campo vazio
            return " -- "  # Retorna None se o campo for deixado em branco
        try:
            entrada_num = float(input(prompt))
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número válido ou deixe em branco.\n")


# Serve para verificar se a resposta é sim ou não
def verif_resposta(prompt):
    while True:
        entrada = input(prompt).strip().upper()  # Remove espaços e transforma em maiúsculas
        if entrada in ["S", "N", "SIM", "NAO", "NÃO"]:  # Verifica se a entrada está na lista
            return entrada  # Retorna a entrada válida
        else:
            print("Por favor, insira uma resposta válida: 'S', 'N', 'SIM', 'NÃO', ou 'NAO'.\n")
            sleep(1)




# Bloco para coletar as informações de cada produto do pedido
def pedido():
    global item_class, valor_total, soma_precos
    for ii in range(itens_venvidos):
        item_ordem = 1 + ii
        item_class_cit = verif_num(f"Qual é a classificação do {item_ordem}º produto? \n"
                                   f"1) Notebook\n"
                                   f"2) Monitor\n"
                                   f"3) Escritório\n"
                                   f"4) Produtos Domésticos\n"
                                   f"5) Cabo\n"
                                   f"6) Fonte\n"
                                   f"7) Perífericos\n"
                                   f"8) Outros\n")
        while item_class_cit not in (1, 2, 3, 4, 5, 6, 7, 8):
            print("Opção inválida!!")
            limpartela()
            item_class_cit = verif_num(f"Qual é a classificação do {item_ordem}º produto? \n"
                                       f"1) Notebook\n"
                                       f"2) Monitor\n"
                                       f"3) Escritório\n"
                                       f"4) Produtos Domésticos\n"
                                       f"5) Cabo\n"
                                       f"6) Fonte\n"
                                       f"7) Perífericos\n"
                                       f"8) Outros\n")

        print("\n \n")
        if item_class_cit == 1:
            print("Escolheu uma das melhores lojas para comprar!!")
            sleep(1)
            item_class = "Notebook"

        if item_class_cit == 2:
            print("Será que ele vai jogar Minecraft??")
            sleep(1)
            item_class = "Monitor"

        if item_class_cit == 3:
            print("Esse cliente vai ser um grande empresário!!")
            sleep(1)
            item_class = "Escritório"

        if item_class_cit == 4:
            print("Uma ótima escolha para cuidar da casa!!")
            sleep(1)
            item_class = "Produtos Domésticos"

        if item_class_cit == 5:
            print("Escolheu a melhor loja pra isso!!")
            sleep(1)
            item_class = "Cabo"

        if item_class_cit == 6:
            print("Aqui o produto é de confiança!!")
            sleep(1)
            item_class = "Fonte"

        if item_class_cit == 7:
            print("Será que tem LED??")
            sleep(1)
            item_class = "Perífericos"

        if item_class_cit == 8:
            print("Independepentende da escolha, o cliente não vai se arrepender, afinal essa é a melhor loja!!")
            sleep(2.7)
            item_class_outros = "Outros"
            item_class2 = naovazia("Qual seria o produto? \n")
            item_class = f"Outros - {item_class2}"

        item_descricione = naovazia("Qual é a descrição do produto?\n")
        item_preco2 = verif_num("Qual é o preço do produto descrito acima? ")

        # Acumulando o valor do preço
        soma_precos += item_preco2

        item_preco = str(item_preco2)
        itens.append(item_class + " - " + item_descricione + " - R$ " + item_preco)


# Bloco para pedir os dados pessoais de pessoa fisica:
def pessoa_fisica():
    global endere_cliente_complemento
    cpf = "CPF"
    nome_cliente = naovazia("Nome: ")
    cpf_cliente2 = verif_num_pode_vazio("Digite o CPF do cliente: ")
    cpf_cliente = str(cpf_cliente2)

    tele_cleinte2 = verif_num_pode_vazio("Digite o número de contato do cliente: ")
    tele_cleinte = str(tele_cleinte2)

    tele_verifciacione = verif_resposta("O telefone de contato acima tem Whatsapp? (SIM ou NÃO) ")
    endere_cliente_rua = input("Qual é o endereço da rua onde o cliente mora? ")
    endere_cliente_num2 = verif_num_pode_vazio("Qual é o número da casa do cliente? ")
    endere_cliente_num = str(endere_cliente_num2)

    endere_cliente_complemento_exist = verif_resposta(
        "O endereço acima possuí complemento? (SIM ou NÃO) ").strip().upper()

    # Estrutura de verificação da resposta
    if endere_cliente_complemento_exist in ("S", "SIM"):
        endere_cliente_complemento = input("Qual é o complemento do endereço? ")
    else:
        pass

    endere_cliente_bairro = input("Qual bairro o cliente mora? ")
    endere_cliente_cep2 = verif_num_pode_vazio("Qual é o CEP da casa do cliente? (DIGITE APENAS NÚMEROS) ")
    endere_cliente_cep = str(endere_cliente_cep2)

    # Bloco para combinar e armazenar os dados do cliente:
    pessoa_dados.append("Nome: " + nome_cliente)
    pessoa_dados.append("CPF: " + cpf_cliente)
    pessoa_dados.append("Telefone: " + tele_cleinte)
    pessoa_dados.append("Whatsapp: " + tele_verifciacione)
    if endere_cliente_complemento_exist in ("S", "SIM"):
        pessoa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + " " + endere_cliente_complemento + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)

    else:
        pessoa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)


# Bloco para pedir os dados pessoais de pessoa fisica:
def empresa_cnpj():
    global endere_cliente_complemento, insc_estadual
    cnpj = "CNPJ"
    razion_social_empresa = naovazia("Razão Social: ")
    cnpj_cliente2 = verif_num_pode_vazio("Digite o CNPJ da empresa: ")
    cnpj_cliente = str(cnpj_cliente2)

    insc_estadual_exist = verif_resposta("A empresa possuí Inscrição Estadual? (SIM ou NÃO) ").strip().upper()

    # Estrutura de verificação da resposta
    if insc_estadual_exist in ("S", "SIM"):
        insc_estadual2 = verif_num_pode_vazio("Qual é a Inscrição Estadual da empresa? ")
        insc_estadual = str(insc_estadual2)
    else:
        pass

    tele_cleinte2 = verif_num_pode_vazio("Digite o número de contato da empresa: ")
    tele_cleinte = str(tele_cleinte2)

    tele_verifciacione = verif_resposta("O telefone de contato acima tem Whatsapp? (SIM ou NÃO) ")
    endere_cliente_rua = input("Qual é o endereço da rua onde o cliente mora? ")
    endere_cliente_num2 = verif_num_pode_vazio("Qual é o número da empresa cliente? ")
    endere_cliente_num = str(endere_cliente_num2)

    endere_cliente_complemento_exist = verif_resposta(
        "O endereço acima possuí complemento? (SIM ou NÃO) ").strip().upper()

    # Estrutura de verificação da resposta
    if endere_cliente_complemento_exist in ("S", "SIM"):
        endere_cliente_complemento = input("Qual é o complemento do endereço? ")
    else:
        pass

    endere_cliente_bairro = input("Qual bairro a empresa se encontra? ")
    endere_cliente_cep2 = verif_num_pode_vazio("Qual é o CEP da empresa cliente? (DIGITE APENAS NÚMEROS) ")
    endere_cliente_cep = str(endere_cliente_cep2)

    # Bloco para combinar e armazenar os dados do cliente:
    empresa_dados.append("Razão social: " + razion_social_empresa)
    empresa_dados.append("CNPJ: " + cnpj_cliente)

    if insc_estadual_exist in ("S", "SIM"):
        empresa_dados.append("Inscrição Estadual: " + insc_estadual)
    else:
        empresa_dados.append("Inscrição Estadual: " + insc_estadual_exist)

    empresa_dados.append("Telefone: " + tele_cleinte)

    if tele_verifciacione in ("S", "SIM"):
        empresa_dados.append("Whatsapp: SIM")

    else:
        empresa_dados.append("Whatsapp: NÃO")

    if endere_cliente_complemento_exist in ("S", "SIM"):
        empresa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + " " + endere_cliente_complemento + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)
    else:
        empresa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)


print("")
# Colocar o script do login


print(f"{famarela}Agora vamos coletar os dados do cliente{reste}")
sleep(1.5)

limpartela()

# Opções de clientes (CPF, CNPJ)
tipo_cliente = input(f"{fbranco}Qual das opções a seguir corresponde ao seu cliente?\n{reste}"
                     f"{fazul}1) Pessoa Fisica (CPF)\n{reste}"
                     f"{negrito}2) Pessoa Juridica (CNPJ)\n{reste}")

# Verifica o valor inserido acima como str
while tipo_cliente not in ("1", "2"):
    limpartela()
    tipo_cliente = input(f"{fbranco}Qual das opções a seguir corresponde ao seu cliente?\n{reste}"
                         f"{fazul}1) Pessoa Fisica (CPF)\n{reste}"
                         f"{negrito}2) Pessoa Juridica (CNPJ)\n{reste}")

# Coletando info de cliente
if tipo_cliente in ("1", "CPF", "cpf", "Pessoa Fisica"):
    pessoa_fisica()
    limpartela()
    print("Verifique os dados do cliente: ")
    sleep(1)
    for dados in pessoa_dados:
        print(dados)

    # Bloco para verificar se os dados estão corretos
    item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
    if item_verificacione in ("S", "SIM"):
        pass
        limpartela()
    if item_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
        verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
        if verif_pedido_recomeco in ("S", "SIM"):
            pessoa_dados.clear()
            limpartela()
            pessoa_fisica()
            limpartela()

    # Bloco enquanto o pedido for errado (o vendedor quiser editar ele entra em loop limpando a lista)
    while item_verificacione not in ("S", "SIM"):
        for dados in pessoa_dados:
            print(dados)

        # Bloco para verificar se o pedido está correto
        item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
        if item_verificacione in ("S", "SIM"):
            pass
            limpartela()

        if item_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
            verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
            if verif_pedido_recomeco in ("S", "SIM"):
                pessoa_dados.clear()
                limpartela()
                pessoa_fisica()
                limpartela()

    juros = verif_num_pode_vazio("Qual é o juros da compra: ")
    soma_precos += juros

# coleta dos dados de cliente ok

# Coletando info de empresa
if tipo_cliente in ("2", "CNPJ", "cnpj", "Pessoa Juridica"):
    empresa_cnpj()
    limpartela()
    print("Verifique os dados do cliente: ")
    sleep(1)
    for dados in empresa_dados:
        print(dados)

    # Bloco para verificar se os dados estão corretos
    item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
    if item_verificacione in ("S", "SIM"):
        pass
        limpartela()
    if item_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
        verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
        if verif_pedido_recomeco in ("S", "SIM"):
            empresa_dados.clear()
            limpartela()
            empresa_cnpj()
            limpartela()

    # Bloco enquanto o pedido for errado (o vendedor quiser editar ele entra em loop limpando a lista)
    while item_verificacione not in ("S", "SIM"):
        for dados in empresa_dados:
            print(dados)

        # Bloco para verificar se o pedido está correto
        item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
        if item_verificacione in ("S", "SIM"):
            pass
            limpartela()

        if item_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
            verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
            if verif_pedido_recomeco in ("S", "SIM"):
                empresa_dados.clear()
                limpartela()
                empresa_cnpj()
                limpartela()

limpartela()

# Bloco responsável pela coleta das infos sobre cada item vendido
itens_venvidos = verif_num("Foram vendidos quantos itens para o cliente? ")

pedido()

limpartela()
print("Verifique os itens do pedido:\n")
sleep(1.78)

# Exibe a lista completa do pedido
for i, item in enumerate(itens, start=1):
    print(f"{i}. {item}")

# Bloco para verificar se o pedido está correto
item_verificacione = verif_resposta("\n Os itens acima estão corretos?(SIM ou NÃO) ").strip().upper()
if item_verificacione in ("S", "SIM"):
    pass
    limpartela()
if item_verificacione in ("N", "NÃO", "NAO"):
    # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
    verif_pedido_recomeco = verif_resposta("Deseja recomeçar o pedido?(SIM ou NÃO)").strip().upper()
    if verif_pedido_recomeco in ("S", "SIM"):
        itens.clear()
        limpartela()
        pedido()
        limpartela()

# Bloco enquanto o pedido for errado (o vendedor quiser editar ele entra em loop limpando a lista)
while item_verificacione not in ("S", "SIM"):
    for i, item in enumerate(itens, start=1):
        print(f"{i}. {item}")

    # Bloco para verificar se o pedido está correto
    item_verificacione = verif_resposta("\n Os itens acima estão corretos?(SIM ou NÃO) ").strip().upper()
    if item_verificacione in ("S", "SIM"):
        pass
        limpartela()

    if item_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
        verif_pedido_recomeco = verif_resposta("Deseja recomeçar o pedido?(SIM ou NÃO)").strip().upper()
        if verif_pedido_recomeco in ("S", "SIM"):
            itens.clear()
            limpartela()
            pedido()
            limpartela()


# Modalidade de venda
modalidade_de_entrega = verif_num("Qual é a modalidade de entrega?\n"
                                  "1) Retirada na loja\n"
                                  "2) Por conta do cliente Uber\n"
                                  "3) Por conta do cliente 99\n"
                                  "4) Por conta do cliente Lalamoove\n"
                                  "5) OLX Correios\n"
                                  "6) OLX Transportadora\n"
                                  "7) Mercado Livre Correios\n"
                                  "8) Mercado Envios\n"
                                  "9) Correios\n")
if modalidade_de_entrega == 1:
    a = "RETIRAR NA LOJA"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 2:
    a = "POR CONTA DO CLIENTE UBER"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 3:
    a = "POR CONTA DO CLIENTE 99"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 4:
    a = "POR CONTA DO CLIENTE LALAMOOVE"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 5:
    a = "OLX CORREIOS"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 6:
    a = "OLX TRANSPORTADORA"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 7:
    a = "MERCADO LIVRE CORREIOS"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 8:
    a = "MERCADO LIVRE ENVIOS"
    modalidade_entrega.append(a)

if modalidade_de_entrega == 9:
    a = "CORREIOS"
    modalidade_entrega.append(a)

print("Modaldiade de entrega armazenada com sucesso...")
sleep(1)
limpartela()

# Modalidade de venda
modalidade_de_venda = verif_num("Qual é a modalidade de venda?\n"
                                "1) Pessoalmente\n"
                                "2) OLX\n"
                                "3) Mercado Livre\n"
                                "4) Whatsapp\n"
                                "5) Marktplace Facebook\n"
                                "6) Marktplace Instagram\n"
                                "7) Site Mercado Shops\n"
                                "8) Telefone\n")
if modalidade_de_venda == 1:
    b = "PESSOALMENTE"
    modalidade_venda.append(b)

if modalidade_de_venda == 2:
    b = "OLX"
    modalidade_venda.append(b)

if modalidade_de_venda == 3:
    b = "MERCADO LIVRE"
    modalidade_venda.append(b)

if modalidade_de_venda == 4:
    b = "WHATSAPP"
    modalidade_venda.append(b)

if modalidade_de_venda == 5:
    b = "MARKETPLACE FACEBOOK"
    modalidade_venda.append(b)

if modalidade_de_venda == 6:
    b = "MARKETPLACE INSTAGRAM"
    modalidade_venda.append(b)

if modalidade_de_venda == 7:
    b = "SITE MERCADO SHOPS"
    modalidade_venda.append(b)

if modalidade_de_venda == 8:
    b = "TELEFONE"
    modalidade_venda.append(b)

print("Modaldiade de venda armazenada com sucesso...")
sleep(1)
limpartela()

fonte_da_venda = verif_num("Qual é a fonte da venda?\n"
                           "1) Indicação\n"
                           "2) Google\n"
                           "3) Facebook\n"
                           "4) Instagram\n"
                           "5) Mercado Livre\n"
                           "6) OLX\n"
                           "7) Site\n")
if fonte_da_venda == 1:
    c = "INDICAÇÃO"
    modalidade_venda.append(c)

if fonte_da_venda == 2:
    c = "GOOGLE"
    modalidade_venda.append(c)

if fonte_da_venda == 3:
    c = "FACEBOOK"
    modalidade_venda.append(c)

if fonte_da_venda == 4:
    c = "INSTAGRAM"
    modalidade_venda.append(c)

if fonte_da_venda == 5:
    c = "MERCADO LIVRE"
    modalidade_venda.append(c)

if fonte_da_venda == 6:
    c = "OLX"
    modalidade_venda.append(c)

if fonte_da_venda == 7:
    c = "SITE"
    modalidade_venda.append(c)

# Recibo de venda
if tipo_cliente == "1":
    recibo_de_venda = f"Eu FÊNIX TESLA ELETRÔNICOS RECUPERÁVEIS LTDA inscrita sob o CNPJ de nº 47.103.686/0001-00, " \
                      f"recebi de {pessoa_dados[0]} inscrito(a) sob o CPF de nº {pessoa_dados[1]} a importância de: " \
                      f"R${soma_precos} referente a venda dos itens relacionados na tabela denominada ITENS VENDIDOS " \
                      f"neste documento."

if tipo_cliente == "2":
    recibo_de_venda = f"Eu FÊNIX TESLA ELETRÔNICOS RECUPERÁVEIS LTDA inscrita sob o CNPJ de nº 47.103.686/0001-00, " \
                      f"recebi de {empresa_dados[0]} inscrito(a) sob o CNPJ de nº {empresa_dados[1]} a importância de: " \
                      f"R${soma_precos} referente a venda dos itens relacionados na tabela denominada ITENS VENDIDOS " \
                      f"neste documento."

# Observações adicionais
obs = verif_resposta("Tem alguma observação?(SIM ou NÃO)").upper().strip()
if obs in ("SIM", "S"):
    observacione = input("Digite a sua observação:\n")
    observacao.append("Observações: " + observacione)

if obs in ("NÃO", "N", "NAO"):
    pass


# Função para gerar o próximo número sequencial baseado nos arquivos já existentes no diretório
def proximo_numero_arquivo(diretorio):
    # Lista os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtra os arquivos que seguem o padrão "numero.pdf"
    numeros = [int(f.split('.')[0]) for f in arquivos if f.endswith('.pdf') and f.split('.')[0].isdigit()]

    # Se existirem arquivos, retorna o próximo número, caso contrário, retorna 1
    if numeros:
        return max(numeros) + 1
    else:
        return 1


# Defina o diretório onde deseja salvar os arquivos
# Defina o caminho para a área de trabalho
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Caminho da nova pasta
folder_name = "Notas Fiscais"
folder_path = os.path.join(desktop_path, folder_name)
# Cria a pasta
os.makedirs(folder_path, exist_ok=True)
print(f"Pasta criada em: {folder_path}")


# Gera o próximo número sequencial
numero_sequencial = proximo_numero_arquivo(folder_path)

# Criação de um novo PDF
pdf = FPDF()

# Adiciona uma página
pdf.add_page()

# Defina as dimensões da imagem do carimbo
imagem_largura = 60  # Largura da imagem em mm
imagem_altura = 40  # Altura da imagem em mm
# Obtém as dimensões da página (210 x 297 para A4)
largura_pagina = pdf.w  # Largura da página A4
altura_pagina = pdf.h  # Altura da página A4
# Calcula as coordenadas x e y para posicionar a imagem no canto inferior direito
x_posicao = largura_pagina - imagem_largura - 5  # 10 mm de margem da borda direita
y_posicao = altura_pagina - imagem_altura - 10  # 10 mm de margem da borda inferior
# Adiciona a imagem no canto inferior direito
pdf.image("C:\\carimbo.png", x=x_posicao, y=y_posicao, w=imagem_largura, h=imagem_altura)

# Defina as dimensões da imagem da logo
imagem_largura = 40  # Largura da imagem em mm
imagem_altura = 40  # Altura da imagem em mm
# Obtém as dimensões da página (210 x 297 para A4)
largura_pagina = pdf.w  # Largura da página A4
altura_pagina = pdf.h  # Altura da página A4
# Calcula as coordenadas x e y para posicionar a imagem no canto inferior direito
x_posicao = largura_pagina - imagem_largura - 156  # 10 mm de margem da borda direita
y_posicao = altura_pagina - imagem_altura - 10  # 10 mm de margem da borda inferior
# logo no canto inferior esqeurdo
pdf.image("C:\\logo.png", x=x_posicao, y=y_posicao, w=imagem_largura, h=imagem_altura)

# BLOCO DE LINHAS PARA TÍTULOS
# linha titulo 01
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 14.55) até (200, 14.55)
pdf.line(10, 14.55, 200, 14.55)

# linha para título 02
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 51, 200, 51)

# linha para título 03
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 125, 200, 125)

# linha para título 04
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 140, 200, 140)

# linha para título 05
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 156, 200, 156)

# linha para título 05
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(6)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 176, 200, 176)

# BLOCO DE CÓDIGO PARA TÍTULOS
# Define a fonte: Arial, tamanho 16
# Define a formatação para o título
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 10, txt="DADOS DO CLIENTE", ln=True, align='C')
# Primeiro valor é a distancia da margem do lado direito
# Segundo valor é a distancia da margem superior da página

# ITENS VENDIDOS
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 62, txt="ITENS VENDIDOS", ln=True, align='C')

# FORMAS DE PAGAMENTO
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 86.30, txt="FORMAS DE PAGAMENTO", ln=True, align='C')

# MODALIDADE DE ENTREGA
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, -55.90, txt="MODALIDADE DE ENTREGA", ln=True, align='C')

# MODALIDADE DE VENDA
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 87.90, txt="MODALIDADE DE VENDA", ln=True, align='C')

# MODALIDADE DE VENDA
pdf.set_font("Arial", style='B', size=18)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, -47.95, txt="RECIBO DE VENDA", ln=True, align='C')

# linha do carimbo
# OK
# Define a cor da linha como preta (RGB: 0, 0, 0)
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0)
# Desenha uma linha preta de (10, 50) até (200, 50)
pdf.line(145, 286, 205.5, 286)

# linha do LOGO
# OK
# Define a cor da linha como preta (RGB: 0, 0, 0)
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0)
# Desenha uma linha preta de (10, 50) até (200, 50)
pdf.line(73, 286, 133.5, 286)

# BLOCO CONFIGURADO PARA LISTA DE DADOS DO CLIENTE
quantidade_dados_pessoa = len(pessoa_dados)
# OK
if tipo_cliente == "1":
    pdf.set_font("Arial", size=12)
    # Define a posição inicial
    x_inicial = 10
    y_inicial = 22
    # Define o espaço horizontal e vertical entre os itens
    espaco_entre_itens = 60  # Ajuste conforme necessário para a largura dos itens
    espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
    # Adiciona o dado na primeira linha
    pdf.set_text_color(0, 0, 0)  # Define a cor do texto como preto
    pdf.text(x_inicial, y_inicial, pessoa_dados[0])
    # Calcula a nova posição inicial para a segunda linha
    x = x_inicial
    y = y_inicial + espaco_entre_linhas
    # Adiciona três dados na segunda linha
    for i in range(1, 4):
        pdf.text(x, y, pessoa_dados[i])
        x += espaco_entre_itens
    # Calcula a nova posição inicial para a terceira linha
    x = x_inicial
    y = y + espaco_entre_linhas
    # Adiciona o dado na terceira linha
    pdf.text(x, y, pessoa_dados[4])

if tipo_cliente == "2":
    pdf.set_font("Arial", size=12)
    # Define a posição inicial
    x_inicial = 10
    y_inicial = 22
    # Define o espaço horizontal e vertical entre os itens
    espaco_entre_itens = 60  # Ajuste conforme necessário para a largura dos itens
    espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
    # Adiciona o dado na primeira linha
    pdf.set_text_color(0, 0, 0)  # Define a cor do texto como preto
    pdf.text(x_inicial, y_inicial, empresa_dados[0])
    # Calcula a nova posição inicial para a segunda linha
    x = x_inicial
    y = y_inicial + espaco_entre_linhas
    # Adiciona três dados na segunda linha
    for i in range(1, 4):
        pdf.text(x, y, empresa_dados[i])
        x += espaco_entre_itens
    # Calcula a nova posição inicial para a terceira linha
    x = x_inicial
    y = y + espaco_entre_linhas
    # Adiciona o dado na terceira linha
    pdf.text(x, y, empresa_dados[4])

# Para lista dos itens venvidos
# OK
# Define a posição inicial para o texto
x = 7.5
y = 60
# Adiciona cada item da lista ao PDF
for item in itens:
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.text(x, y, item)  # Adiciona o item na posição (x, y)
    y += 5  # Move para a próxima linha (ajuste o valor conforme necessário)


#TESTE

# Bloco caso o comprador quiser combinar métodos de compra
combinar_pagamento = verif_resposta("O comprador vai combinar formas de pagamento? (SIM ou NÃO) ").strip().upper()

if combinar_pagamento in ("S", "SIM"):
    limpartela()
    quant_pagamentos = verif_num("Serão quantas formas de pagamento? ")

    if quant_pagamentos == 1:
        print("uma vez")
        limpartela()
        print("1º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma1 = f"1º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma1 = f"1º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma1 = f"1º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma1 = f"1º Forma: Via Link"

        elif forma_pagamento == 5:
            forma1 = f"1º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()

        print("Verifique as formas de pagamento:")
        print(forma1)

        pagamento_verificacione = verif_resposta(
            "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
        if pagamento_verificacione in ("S", "SIM"):
            pass
        if pagamento_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
            verif_pagamento_recomeco = verif_resposta(
                "Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
            if verif_pagamento_recomeco in ("S", "SIM"):
                # forma 1
                limpartela()
                print("1º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma1 = f"1º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma1 = f"1º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma1 = f"1º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma1 = f"1º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma1 = f"1º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                limpartela()
                print("Verifique as formas de pagamento:")
                print(forma1)
                pagamento_verificacione = verif_resposta(
                    "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
                while pagamento_verificacione not in ("S", "SIM"):
                    # forma 1
                    limpartela()
                    print("1º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma1 = f"1º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma1 = f"1º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma1 = f"1º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma1 = f"1º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma1 = f"1º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                    limpartela()
                    print(forma1)

    if quant_pagamentos == 2:
        print("2 vezes")
        # forma 1
        limpartela()
        print("1º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma1 = f"1º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma1 = f"1º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma1 = f"1º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma1 = f"1º Forma: Via Link"

        elif forma_pagamento == 5:
            forma1 = f"1º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()

        # forma 2
        limpartela()
        print("2º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma2 = f"2º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma2 = f"2º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma2 = f"2º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma2 = f"2º Forma: Via Link"

        elif forma_pagamento == 5:
            forma2 = f"2º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()
        print("Verifique as formas de pagamento:")
        print(forma1)
        print(forma2)

        pagamento_verificacione = verif_resposta(
            "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
        if pagamento_verificacione in ("S", "SIM"):
            pass
        if pagamento_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
            verif_pagamento_recomeco = verif_resposta(
                "Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
            if verif_pagamento_recomeco in ("S", "SIM"):
                print("2 vezes")
                # forma 1
                limpartela()
                print("1º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma1 = f"1º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma1 = f"1º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma1 = f"1º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma1 = f"1º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma1 = f"1º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                limpartela()

                # forma 2
                limpartela()
                print("2º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma2 = f"2º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma2 = f"2º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma2 = f"2º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma2 = f"2º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma2 = f"2º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"
                limpartela()
                print("Verifique as formas de pagamento:")
                print(forma1)
                print(forma2)
                pagamento_verificacione = verif_resposta(
                    "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
                while pagamento_verificacione not in ("S", "SIM"):
                    # forma 1
                    limpartela()
                    print("1º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma1 = f"1º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma1 = f"1º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma1 = f"1º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma1 = f"1º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma1 = f"1º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                    limpartela()

                    # forma 2
                    limpartela()
                    print("2º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma2 = f"2º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma2 = f"2º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma2 = f"2º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma2 = f"2º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma2 = f"2º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"
                    limpartela()
                    print("Verifique as formas de pagamento:")
                    print(forma1)
                    print(forma2)
                    pagamento_verificacione = verif_resposta(
                        "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()

    if quant_pagamentos == 3:
        # forma 1
        limpartela()
        print("1º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma1 = f"1º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma1 = f"1º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma1 = f"1º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma1 = f"1º Forma: Via Link"

        elif forma_pagamento == 5:
            forma1 = f"1º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()

        # forma 2
        limpartela()
        print("2º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma2 = f"2º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma2 = f"2º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma2 = f"2º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma2 = f"2º Forma: Via Link"

        elif forma_pagamento == 5:
            forma2 = f"2º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()

        # forma 3
        limpartela()
        print("3º Forma:")  # Começa a contar a partir de 1
        forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                    "1) À Vista Débito\n"
                                    "2) Mercado Livre\n"
                                    "3) À Vista PIX\n"
                                    "4) Via Link\n"
                                    "5) OLX PAY\n"
                                    "6) Crédito\n"))

        if forma_pagamento == 1:
            forma3 = f"3º Forma: À Vista Débito"

        elif forma_pagamento == 2:
            forma3 = f"3º Forma: Mercado Livre"

        elif forma_pagamento == 3:
            forma3 = f"3º Forma: À Vista PIX"

        elif forma_pagamento == 4:
            forma3 = f"3º Forma: Via Link"

        elif forma_pagamento == 5:
            forma3 = f"3º Forma: OLX PAY"

        elif forma_pagamento == 6:
            pag_parcelas2 = verif_num("Serão quantas parcelas? ")
            pag_parcelas = str(pag_parcelas2)
            forma3 = f"3º Forma: Crédito Parcelado em {pag_parcelas}X"

        limpartela()

        print("Verifique as formas de pagamento:")
        print(forma1)
        print(forma2)
        print(forma3)

        pagamento_verificacione = verif_resposta(
            "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
        if pagamento_verificacione in ("S", "SIM"):
            pass
        if pagamento_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
            verif_pagamento_recomeco = verif_resposta(
                "Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
            if verif_pagamento_recomeco in ("S", "SIM"):
                # forma 1
                limpartela()
                print("1º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma1 = f"1º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma1 = f"1º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma1 = f"1º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma1 = f"1º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma1 = f"1º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                limpartela()

                # forma 2
                limpartela()
                print("2º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma2 = f"2º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma2 = f"2º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma2 = f"2º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma2 = f"2º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma2 = f"2º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"
                limpartela()

                limpartela()
                print("3º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma3 = f"3º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma3 = f"3º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma3 = f"3º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma3 = f"3º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma3 = f"3º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma3 = f"3º Forma: Crédito Parcelado em {pag_parcelas}X"

                limpartela()

                print("Verifique as formas de pagamento:")
                print(forma1)
                print(forma2)
                print(forma3)
                pagamento_verificacione = verif_resposta(
                    "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
                while pagamento_verificacione not in ("S", "SIM"):
                    # forma 1
                    limpartela()
                    print("1º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma1 = f"1º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma1 = f"1º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma1 = f"1º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma1 = f"1º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma1 = f"1º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                    limpartela()

                    # forma 2
                    limpartela()
                    print("1º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma2 = f"2º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma2 = f"2º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma2 = f"2º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma2 = f"2º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma2 = f"2º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma2 = f"2º Forma: Crédito Parcelado em {pag_parcelas}X"
                    limpartela()

                    print("3º Forma:")  # Começa a contar a partir de 1
                    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                                "1) À Vista Débito\n"
                                                "2) Mercado Livre\n"
                                                "3) À Vista PIX\n"
                                                "4) Via Link\n"
                                                "5) OLX PAY\n"
                                                "6) Crédito\n"))

                    if forma_pagamento == 1:
                        forma3 = f"3º Forma: À Vista Débito"

                    elif forma_pagamento == 2:
                        forma3 = f"3º Forma: Mercado Livre"

                    elif forma_pagamento == 3:
                        forma3 = f"3º Forma: À Vista PIX"

                    elif forma_pagamento == 4:
                        forma3 = f"3º Forma: Via Link"

                    elif forma_pagamento == 5:
                        forma3 = f"3º Forma: OLX PAY"

                    elif forma_pagamento == 6:
                        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                        pag_parcelas = str(pag_parcelas2)
                        forma3 = f"3º Forma: Crédito Parcelado em {pag_parcelas}X"

                    limpartela()

                    print("Verifique as formas de pagamento:")
                    print(forma1)
                    print(forma2)
                    print(forma3)
                    pagamento_verificacione = verif_resposta(
                        "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()

# Caso o usuário responda "NÃO" para combinar pagamentos
# OK
if combinar_pagamento in ("N", "NÃO", "NAO"):
    limpartela()
    print("1º Forma:")  # Começa a contar a partir de 1
    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                "1) À Vista Débito\n"
                                "2) Mercado Livre\n"
                                "3) À Vista PIX\n"
                                "4) Via Link\n"
                                "5) OLX PAY\n"
                                "6) Crédito\n"))

    if forma_pagamento == 1:
        forma1 = f"1º Forma: À Vista Débito"

    elif forma_pagamento == 2:
        forma1 = f"1º Forma: Mercado Livre"

    elif forma_pagamento == 3:
        forma1 = f"1º Forma: À Vista PIX"

    elif forma_pagamento == 4:
        forma1 = f"1º Forma: Via Link"

    elif forma_pagamento == 5:
        forma1 = f"1º Forma: OLX PAY"

    elif forma_pagamento == 6:
        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
        pag_parcelas = str(pag_parcelas2)
        forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"
    limpartela()

    print("Verifique as formas de pagamento:")
    print(forma1)

    pagamento_verificacione = verif_resposta(
        "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
    if pagamento_verificacione in ("S", "SIM"):
        pass
    if pagamento_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
        verif_pagamento_recomeco = verif_resposta(
            "Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
        if verif_pagamento_recomeco in ("S", "SIM"):
            # forma 1
            limpartela()
            print("1º Forma:")  # Começa a contar a partir de 1
            forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                        "1) À Vista Débito\n"
                                        "2) Mercado Livre\n"
                                        "3) À Vista PIX\n"
                                        "4) Via Link\n"
                                        "5) OLX PAY\n"
                                        "6) Crédito\n"))

            if forma_pagamento == 1:
                forma1 = f"1º Forma: À Vista Débito"

            elif forma_pagamento == 2:
                forma1 = f"1º Forma: Mercado Livre"

            elif forma_pagamento == 3:
                forma1 = f"1º Forma: À Vista PIX"

            elif forma_pagamento == 4:
                forma1 = f"1º Forma: Via Link"

            elif forma_pagamento == 5:
                forma1 = f"1º Forma: OLX PAY"

            elif forma_pagamento == 6:
                pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                pag_parcelas = str(pag_parcelas2)
                forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"
            limpartela()
            print("Verifique as formas de pagamento:")
            print(forma1)
            pagamento_verificacione = verif_resposta(
                "\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
            while pagamento_verificacione not in ("S", "SIM"):
                # forma 1
                limpartela()
                print("1º Forma:")  # Começa a contar a partir de 1
                forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                            "1) À Vista Débito\n"
                                            "2) Mercado Livre\n"
                                            "3) À Vista PIX\n"
                                            "4) Via Link\n"
                                            "5) OLX PAY\n"
                                            "6) Crédito\n"))

                if forma_pagamento == 1:
                    forma1 = f"1º Forma: À Vista Débito"

                elif forma_pagamento == 2:
                    forma1 = f"1º Forma: Mercado Livre"

                elif forma_pagamento == 3:
                    forma1 = f"1º Forma: À Vista PIX"

                elif forma_pagamento == 4:
                    forma1 = f"1º Forma: Via Link"

                elif forma_pagamento == 5:
                    forma1 = f"1º Forma: OLX PAY"

                elif forma_pagamento == 6:
                    pag_parcelas2 = verif_num("Serão quantas parcelas? ")
                    pag_parcelas = str(pag_parcelas2)
                    forma1 = f"1º Forma: Crédito Parcelado em {pag_parcelas}X"

                limpartela()


print("Salvando no sistema...")
sleep(1.76)
limpartela()

###Formatação no pdf

if forma_pagamento == 1:
    # MODALIDADE DE VENDA
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(200, -40.95, txt=forma1, ln=True, align='C')

if forma_pagamento == 2:
    # MODALIDADE DE VENDA 01
    pdf.set_font("Arial", style='B', size=18)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(80, -40.95, txt=forma1, ln=True, align='C')

    # MODALIDADE DE VENDA 02
    pdf.set_font("Arial", style='B', size=18)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(290, 40.95, txt=forma2, ln=True, align='C')

if forma_pagamento == 3:
    # MODALIDADE DE VENDA 01
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(80, -40.95, txt=forma1, ln=True, align='C')

    # MODALIDADE DE VENDA 02
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(200, 40.95, txt=forma2, ln=True, align='C')

    # MODALIDADE DE VENDA 03
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    # Adiciona um título
    pdf.cell(320, -40.95, txt=forma3, ln=True, align='C')










#TESTE




# BLOCO QUE DEFINE A MODALIDADE DA VENDA
#OK
pdf.set_font("Arial", size=12)
# Define a posição inicial
x_inicial = 40
y_inicial = 156
# Define o espaço horizontal e vertical entre os itens
espaco_entre_itens = 105  # Ajuste conforme necessário para a largura dos itens
espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
# Adiciona o dado na primeira linha
# Define a cor do texto como preto
pdf.set_text_color(0, 0, 0)
# Calcula a nova posição inicial para a segunda linha
x = x_inicial
y = y_inicial + espaco_entre_linhas
# Adiciona três dados na segunda linha
quantidade_de_elementos = len(modalidade_venda)
for i in range(quantidade_de_elementos):
    pdf.text(x, y, modalidade_venda[i])
    x += espaco_entre_itens

# BLOCO PARA CENTRALIZAR A MODALIDADE DE ENTREGA
# OK
# Define a fonte
pdf.set_font("Arial", size=16)
# Concatena os itens da lista em uma única string
texto = " ".join(modalidade_entrega)
# Calcula a posição X para centralizar o texto
page_width = pdf.w  # Largura total da página
text_width = pdf.get_string_width(texto)  # Largura do texto
x_position = (page_width - text_width) / 2  # Calcula a posição central
# Adiciona o texto centralizado na página
pdf.text(x_position, 150, texto)

# Textos fixos na parte de baixo
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
pdf.text(150, 290, "ASSINATURA DO VENDEDOR")

pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
pdf.text(80, 290, "ASSINATURA DO CLIENTE")

## TEXTO PARA RECIBO DE VENDAS
# ok
# Define a fonte e o estilo
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
# Texto do recibo
# Adiciona o texto com quebra automática
pdf.set_xy(7, 180)  # Define a posição inicial do texto
pdf.multi_cell(0, 5, recibo_de_venda)  # 0 significa que a largura será ajustada à página

# TEXTO PARA CONCEITIZAÇÃO
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
cientizacao = "Estou ciente e concordo com os termos e condições descritos no documento TERMOS E CONDIÇÕES DE COMPRA E VENDA DE PRODUTOS."
# Adiciona o texto com quebra automática
pdf.set_xy(7, 220)  # Define a posição inicial do texto
pdf.multi_cell(0, 5, cientizacao)  # 0 significa que a largura será ajustada à página

## CAMPO PARA COLOCAR OBSERVAÇÃO
# ok
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
# Adiciona o texto com quebra automática
pdf.set_xy(7, 200)  # Define a posição inicial do texto
texto_observacao = "\n".join(observacao)
pdf.multi_cell(0, 5, texto_observacao)  # 0 significa que a largura será ajustada à página

# Data de hoje
data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y ")
hora_formatada = data_atual.strftime("%H:%M:%S")
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
pdf.text(70, 255, f'São Paulo {data_formatada} {hora_formatada}')

# Define o nome do arquivo com base no número sequencial
nome_arquivo = f"{numero_sequencial}.pdf"

# Salva o arquivo em PDF no diretório especificado
pdf.output(os.path.join(folder_path, nome_arquivo))

print(f"Documento PDF '{nome_arquivo}' criado com sucesso!")

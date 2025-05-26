import os
import platform
import sys
from time import sleep
from colorama import Fore, Style, init
import getpass

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

# lista onde os dados dos produtos vendidos são armazenados
itens = []

# Lista onde os dados de cliente fisico são armazenados
pessoa_dados = []

# Lista onde os dados da empresa são armazenados
empresa_dados = []


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
            return None  # Retorna None se o campo for deixado em branco
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
            return None  # Retorna None se o campo for deixado em branco
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


# Formas de pagamento
def pagamentos_formas():
    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                "1) À Vista Débito\n"
                                "2) Mercado livre\n"
                                "3) À Vista PIX\n"
                                "4) Via Link\n"
                                "5) OLX PAY\n"
                                "6) Crédito\n"))

    if forma_pagamento == 1:
        debito = "À Vista Débito"

    if forma_pagamento == 2:
        mercado_livre = "Mercado Livre"

    if forma_pagamento == 3:
        pix = "À Vista PIX"

    if forma_pagamento == 4:
        via_link = "Via Link"

    if forma_pagamento == 5:
        olx = "OLX PAY"

    if forma_pagamento == 6:
        credito = "Crédito"
        parcelas = verif_num("Serão quantas parcelas? ")


# Bloco para coletar as informações de cada produto do pedido
def pedido():
    global item_class
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
            print("Esse cliente vai ser um grande emresário!!")
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
        item_preco = str(item_preco2)

        itens.append(item_class + " - " + item_descricione + " - " + item_preco)


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
    if endere_cliente_complemento_exist in ("S", "SIM"):
        pessoa_dados.append("Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + " " + endere_cliente_complemento + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)

    else:
        pessoa_dados.append("Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)


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
                emrpesa_dados.clear()
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

limpartela()
# Bloco caso o comprador quiser combinar métodos de compra
combinar_pagamento = verif_resposta("O comprador vai combinar formas de pagamento?(SIM ou NÃO) ").strip().upper()
if combinar_pagamento in ("S", "SIM"):
    limpartela()
    quant_pagamentos = verif_num("Serão quantas formas de pagamento? ")

else:
    pagamentos_formas()

# bloco de formas de pagamento colocado em um def encima

#formas de pagametno estão incompletas

# Forma de pagamento

# Exemplo de como adicionar cores a uma frase em Python
import os
import platform
import sys
from time import sleep
from colorama import Fore, Style, init
import getpass

init()
# Inicializa o colorama

fvermelha = Fore.RED
fverde = Fore.GREEN
famarela = Fore.YELLOW
fazul = Fore.BLUE
fpreto = Fore.BLACK
fmagenta = Fore.MAGENTA
fciano = Fore.CYAN
fbranco = Fore.WHITE
reste = Style.RESET_ALL

z = "_________________________________________________________________________________________________________"


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


# Especifique o caminho da pasta que você deseja criar
caminho_da_pasta = 'C:\\Usuarios'

# Use a função mkdir do módulo os para criar a pasta
try:
    os.mkdir(caminho_da_pasta)
    print(f"{famarela}Conectando com o servidor...{reste}")
    sleep(1)
    print("")
    print(f"{famarela}Conexão concedida!{reste}")
    sleep(1)
    print(f"{fazul}Redirecionando...{reste}")
    sleep(1.9)
except FileExistsError:
    print(f"{famarela}Conexão concedida!{reste}")
    sleep(1)
    print(f"{fazul}Redirecionando...{reste}")
    sleep(1.9)
except Exception as e:
    print(f"{famarela}Conectando com o servidor...{reste}")
    sleep(1)
    print("")
    print("NÃO FOI POSSÍVEL CONECTAR COM O SERVIDOR ERRO!")
    sleep(1)
    limpartela()
    print(f"{famarela}Erro: {e}{reste}")
    print(
        f"{famarela}Por favor entre em contato com o desenvolvedor do Software utilizando as informações abaixo:{reste}")
    print("O SOFTWARE FOI TOTALMENTE PENSADO E PROJETADO PELO ||| AHMAD ABOULEININ |||")
    print("Entre em contato com o desenvolvedor do Software por meio de suas redes sociais:")
    print("Instagram: @teucnc_oficial")
    print("Youtube: TEUCNC")
    print(z)
    print(z)
    print(z)
    input(f"{fazul}AO TERMINAR DE LER APERTE ENTER PARA PROSSEGUIR PARA SAIR DO SOFTWARE...{reste}\n")
    print(f"{fazul}Tchau!!!{reste}")
    sleep(1.9)
    sys.exit()


def erros():
    print(f"{famarela}Resposta inválida{reste}")
    sleep(1.75)
    print(f"{famarela}Digite a resposta novamente{reste}\n")
    sleep(1.76)
    limpartela()


# Função para verificar se o email é válido
def verificar_email(email):
    while "@" not in email:
        print(f"{fazul}Email inválido. Certifique-se de ter escrito o email corretamente.{reste}")
        email = input(f"{famarela}Digite o email novamente:\n{reste}").strip()
    return email


# Função para verificar se o arquivo existe
def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)


# Função para realizar o login
def realizar_login():
    print(f"{famarela}VAMOS REALIZAR O SEU LOGIN:\n {reste}")
    usuario_defenido = input(f"{famarela}Inseria o seu usuário para prosseguir:{reste}\n")
    nome_arquivo = fr"C:\\Usuarios\\{usuario_defenido}.txt"
    email = input(f"{famarela}Email: {reste}").strip()
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}").strip()

    if not arquivo_existe(nome_arquivo):
        print(f"{fvermelha}O login não foi encontrado. Redirecionando para o cadastro.{reste}")
        sleep(2)
        realizar_cadastro()
        return

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.read().split('\n')

        # Verifica se o email e a senha estão no arquivo
        if email in linhas and senha in linhas:
            limpartela()
            print(f"{fazul}Bem-vindo, {usuario_defenido}!{reste}")
        else:
            print(f"{fciano}Email ou senha incorretos. Tente novamente.{reste}")
            sleep(3)
            limpartela()
            realizar_login()

    except FileNotFoundError:
        print(f"{fvermelha}Informações não encontradas na base. Redirecionando para o cadastro.{reste}")
        realizar_cadastro()


# Função para realizar o cadastro
def realizar_cadastro():
    print(f"{famarela}VAMOS REALIZAR O SEU CADASTRO:\n {reste}")
    usuario_novo = input(f"{famarela}Inseria o seu usuário para prosseguir:{reste}\n")
    nome_arquivo = fr"C:\\Usuarios\\{usuario_novo}.txt"
    nome = input(f"{famarela}Nome: {reste}").strip()
    email = input(f"{famarela}Email: {reste}").strip()
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}").strip()

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.read().split('\n')

        # Verifica se o email já está cadastrado
        if email in linhas:
            print(f"{fazul}Este email já está cadastrado. Tente fazer login.{reste}")
            sleep(3)
            return

    except FileNotFoundError:
        pass

    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome}\n{email}\n{senha}\n\n")
    limpartela()
    print(f"{fazul}Cadastro realizado com sucesso!{reste}")
    sleep(2)


cadastro = input(f"{fazul}VOCÊ JÁ POSSUI UM CADASTRO NO NOSSO SISTEMA? (SIM ou NÃO): {reste}").upper().strip()

while (cadastro not in
       ["SIM", "S", "NÃO", "NAO", "N"]):
    erros()
    cadastro = input(f"{fazul}VOCÊ JÁ POSSUI UM CADASTRO NO NOSSO SISTEMA? (SIM ou NÃO): {reste}").upper().strip()

if cadastro in ["SIM", "S"]:
    print(f"{fciano}ENTÃO VAMOS NESSA!{reste}")
    sleep(1.9)
    limpartela()
    print(f"{famarela}VAMOS REALIZAR O SEU LOGIN:\n {reste}")
    usuario_defenido = input(f"{famarela}Inseria o seu usuário para prosseguir:{reste}\n")
    nome_arquivo = fr"C:\\Usuarios\\{usuario_defenido}.txt"
    email = input(f"{famarela}Email: {reste}").strip()
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}").strip()

    if not arquivo_existe(nome_arquivo):
        print(f"{fvermelha}O login não foi encontrado. Redirecionando para o cadastro.{reste}")
        sleep(2)
        realizar_cadastro()

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.read().split('\n')

        # Verifica se o email e a senha estão no arquivo
        if email in linhas and senha in linhas:
            limpartela()
            print(f"{fazul}Bem-vindo, {usuario_defenido}!{reste}")
        else:
            print(f"{fciano}Email ou senha incorretos. Tente novamente.{reste}")
            sleep(3)
            limpartela()
            realizar_login()

    except FileNotFoundError:
        print(f"{fvermelha}Informações não encontradas na base. Redirecionando para o cadastro.{reste}")
        realizar_cadastro()

elif cadastro in ["NÃO", "NAO", "N"]:
    realizar_cadastro()
    limpartela()
    print(f"{famarela}VAMOS REALIZAR O SEU LOGIN:\n {reste}")
    usuario_defenido = input(f"{famarela}Inseria o seu usuário para prosseguir:{reste}\n")
    nome_arquivo = fr"C:\\Usuarios\\{usuario_defenido}.txt"
    email = input(f"{famarela}Email: {reste}").strip()
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}").strip()

    if not arquivo_existe(nome_arquivo):
        print(f"{fvermelha}O login não foi encontrado. Redirecionando para o cadastro.{reste}")
        sleep(2)
        realizar_cadastro()

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.read().split('\n')

        # Verifica se o email e a senha estão no arquivo
        if email in linhas and senha in linhas:
            limpartela()
            print(f"{fazul}Bem-vindo, {usuario_defenido}!{reste}")
        else:
            print(f"{fciano}Email ou senha incorretos. Tente novamente.{reste}")
            sleep(3)
            limpartela()
            realizar_login()

    except FileNotFoundError:
        print(f"{fvermelha}Informações não encontradas na base. Redirecionando para o cadastro.{reste}")
        realizar_cadastro()

limpartela()


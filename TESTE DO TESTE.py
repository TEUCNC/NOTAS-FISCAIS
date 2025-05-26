import os
import platform
from time import sleep
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


# DEF PARA O WHILE
def erros():
    print(f"{famarela}Resposta inválida{reste}")
    sleep(1.75)
    print(f"{famarela}Digite a resposta novamente:{reste}")
    sleep(1.76)
    limpartela()


# DEF PARA CRÉDITOS E LIMPAR A TELA
def limpartela():
    sistema = platform.system()
    # Verificar qual sistema operacional está sendo executado
    if sistema == "Windows":
        # Comando para reiniciar no Windows
        comando = "cls"
    elif sistema == "Darwin":
        # Comando para reiniciar no macOS
        comando = "clear"
    elif sistema == "Linux":
        # Comando para reiniciar no Linux
        comando = "clear"
    else:
        # Caso o sistema operacional não seja reconhecido
        comando = None

    # Executar o comando, se definido
    if comando:
        os.system(comando)

    print("---------------------------------CRÉDITOS------------------------------------")
    print("O SOFTWARE FOI TOTALMENTE PENSADO E PROJETADO PELO ||| AHMAD ABOULEININ |||")
    print("Apoie o criador do projeto em suas redes sociais:")
    print("Instagram: @teucnc_oficial")
    print("Youtube: TEUCNC")
    print("---------------------------------CRÉDITOS------------------------------------\n \n")


# Função para verificar se o email é válido
def verificar_email(email):
    while "@" not in email:
        print(f"{fazul}Email inválido. Certifique-se de ter escrito o email corretamente.{reste}")
        email = input(f"{famarela}Digite o email novamente:\n{reste}")
    return email


# Função para verificar se o arquivo existe
def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)


# Função para realizar o login
def realizar_login():
    print(f"{famarela}VAMOS REALIZAR O SEU LOGIN:\n {reste}")
    nome_arquivo = r"C:\ProgramData\acessos.txt"
    email = input(f"{famarela}Email: {reste}")
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}")

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
            print(f"{fazul}Bem-vindo, {email}!{reste}")
        else:
            print(f"{fciano}Email ou senha incorretos. Tente novamente.{reste}")
            sleep(3)
            limpartela()
            realizar_login()

    except FileNotFoundError:
        print(f"{fvermelha}O arquivo '{nome_arquivo}' não foi encontrado. Redirecionando para o cadastro.{reste}")
        realizar_cadastro()


# Função para realizar o cadastro
def realizar_cadastro():
    print(f"{famarela}VAMOS REALIZAR O SEU CADASTRO:\n {reste}")
    nome_arquivo = r"C:\ProgramData\acessos.txt"
    nome = input(f"{famarela}Nome: {reste}")
    email = input(f"{famarela}Email: {reste}")
    email = verificar_email(email)
    senha = input(f"{famarela}Senha: {reste}")

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


# Verificar se o usuário já possui um cadastro
limpartela()
print(f"{fazul}SEJA BEM-VINDO(A)!{reste}")
sleep(1.7)

cadastro = input(f"{fazul}VOCÊ JÁ POSSUI UM CADASTRO NO NOSSO SISTEMA? (SIM ou NÃO): {reste}").upper().strip()
while cadastro not in ["SIM", "S", "NÃO", "NAO", "N"]:
    erros()
    cadastro = input(f"{fazul}VOCÊ JÁ POSSUI UM CADASTRO NO NOSSO SISTEMA? (SIM ou NÃO): {reste}").upper().strip()
if cadastro in ["SIM", "S"]:
    print(f"{fciano}ENTÃO VAMOS NESSA VIAGEM!{reste}")
    sleep(1.9)
    limpartela()
    realizar_login()

elif cadastro in ["NÃO", "NAO", "N"]:
    realizar_cadastro()
    limpartela()
    realizar_login()
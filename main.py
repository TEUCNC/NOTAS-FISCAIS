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

def naovazia(prompt):
    while True:
        entrada = input(prompt).strip()
        # Remove espaços em branco ao redor
        if entrada:
            return entrada
        print("Este campo é obrigatório!! Tente novamente.")

def verif_num(prompt):
    while True:
## Def de verificação se o valor inserido é numero

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

print("")
# Colocar o script do login


print(f"{famarela}Agora vamos coletar os dados do cliente{reste}")
sleep(1.5)

limpartela()

tipo_cliente = input(f"{fbranco}Qual das opções a seguir corresponde ao seu cliente?\n{reste}"
                     f"{fazul}1) Pessoa Fisica (CPF)\n{reste}"
                     f"{negrito}2) Pessoa Juridica (CNPJ)\n{reste}")

while tipo_cliente not in ("1", "2"):
    limpartela()
    tipo_cliente = input(f"{fbranco}Qual das opções a seguir corresponde ao seu cliente?\n{reste}"
                         f"{fazul}1) Pessoa Fisica (CPF)\n{reste}"
                         f"{negrito}2) Pessoa Juridica (CNPJ)\n{reste}")
if tipo_cliente in ("1", "CPF", "cpf", "Pessoa Fisica"):
    nome_cliente = naovazia("Nome: ")
    cpf_cliente =

if tipo_cliente in ("2", "CNPJ", "cnpj", "Pessoa Juridica"):
    print("")

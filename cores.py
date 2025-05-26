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
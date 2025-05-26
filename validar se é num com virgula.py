from time import sleep

def verif_num_virgula(prompt):
    while True:
        try:
            entrada_num = float(input(prompt))  # Tenta converter a entrada para número inteiro
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número válido.\n \n")  # Mostra mensagem de erro para entrada inválida
            sleep(1)


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


usuario = verif_num_virgula("Digite um número inteiro: ")
print(f"Você digitou o número: {usuario}")

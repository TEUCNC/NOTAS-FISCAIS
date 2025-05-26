def verif_num(prompt):
    while True:
        try:
            entrada_num = int(input(prompt))  # Tenta converter a entrada para número inteiro
            return entrada_num  # Retorna o valor se for válido
        except ValueError:
            print("Por favor, insira um número inteiro válido.")  # Mostra mensagem de erro para entrada inválida


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

usuario = verif_num("Digite um número inteiro: ")
print(f"Você digitou o número: {usuario}")

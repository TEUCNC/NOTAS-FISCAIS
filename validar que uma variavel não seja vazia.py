def obter_entrada_valida(prompt):
    while True:
        entrada = input(prompt).strip()  # Remove espaços em branco ao redor
        if entrada:
            return entrada
        print("A entrada não pode estar vazia. Tente novamente.")

# Exemplo de uso
usuario = obter_entrada_valida("Digite seu nome: ")


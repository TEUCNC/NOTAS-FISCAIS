def verif_resposta(prompt):
    while True:
        entrada = input(prompt).strip().upper()  # Remove espaços e transforma em maiúsculas
        if entrada in ["S", "N", "SIM", "NAO", "NÃO"]:  # Verifica se a entrada está na lista
            return entrada  # Retorna a entrada válida
        else:
            print("Por favor, insira uma resposta válida: 'S', 'N', 'SIM', 'NÃO', ou 'NAO'.\n")

resposta = verif_resposta("Digite 'S' para sim ou 'N' para não: ")
print(f"Você digitou: {resposta}")

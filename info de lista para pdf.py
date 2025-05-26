from fpdf import FPDF

# Exemplo de lista de informações
informacoes = [
    "Item 1: Informações sobre o primeiro item.",
    "Item 2: Detalhes do segundo item.",
    "Item 3: Explicações adicionais para o terceiro item.",
    "Item 4: Informações adicionais para o quarto item."
]

# Criação de um novo PDF
pdf = FPDF()

# Adiciona uma página
pdf.add_page()

# Define a fonte: Arial, tamanho 16 para o título
pdf.set_font("Arial", size=16)

# Adiciona um título
pdf.cell(200, 10, txt="Informações da Lista", ln=True, align='C')

# Define a fonte para o texto da lista
pdf.set_font("Arial", size=12)

# Adiciona os itens da lista ao PDF
for item in informacoes:
    pdf.multi_cell(0, 10, txt=item)

# Salva o arquivo PDF
pdf.output("informacoes_lista.pdf")

print("Documento PDF criado com sucesso!")

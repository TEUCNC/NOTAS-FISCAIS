from fpdf import FPDF

# Criação de um novo PDF
pdf = FPDF()

# Adiciona uma página
pdf.add_page()

# Define a fonte: Arial, tamanho 16
pdf.set_font("Arial", size=16)

# Adiciona um título
pdf.cell(200, 10, txt="Título do Documento", ln=True, align='C')

# Adiciona um parágrafo
pdf.set_font("Arial", size=12)
texto = "Este é um parágrafo de exemplo em um arquivo PDF gerado com Python."
pdf.multi_cell(0, 10, txt=texto)

# Salva o arquivo em PDF
pdf.output("exemplo_documento.pdf")

print("Documento PDF criado com sucesso!")

from fpdf import FPDF

# Criar uma classe PDF que herda de FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Relatório de Modalidades de Venda", 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, 'C')

# Instanciar o objeto PDF
pdf = PDF()
pdf.add_page()

# BLOCO DE LINHAS PARA TÍTULOS
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(1)

# Desenha linhas horizontais no PDF para os títulos
pdf.line(10, 30, 200, 30)  # Ajustado para evitar sobreposição
pdf.line(10, 60, 200, 60)  # Ajustado para evitar sobreposição
pdf.line(10, 90, 200, 90)  # Ajustado para evitar sobreposição
pdf.line(10, 120, 200, 120)  # Ajustado para evitar sobreposição
pdf.line(10, 150, 200, 150)  # Ajustado para evitar sobreposição
pdf.line(10, 180, 200, 180)  # Ajustado para evitar sobreposição

# BLOCO DE CÓDIGO PARA TÍTULOS
# Define a fonte: Arial, tamanho 16
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(0, 0, 0)

# Adiciona os títulos com posições ajustadas
pdf.set_xy(10, 25)
pdf.cell(200, 10, txt="DADOS DO CLIENTE", ln=True, align='C')

pdf.set_xy(10, 55)
pdf.cell(200, 10, txt="ITENS VENDIDOS", ln=True, align='C')

pdf.set_xy(10, 85)
pdf.cell(200, 10, txt="FORMAS DE PAGAMENTO", ln=True, align='C')

pdf.set_xy(10, 115)
pdf.cell(200, 10, txt="MODALIDADE DE ENTREGA", ln=True, align='C')

pdf.set_xy(10, 145)
pdf.cell(200, 10, txt="MODALIDADE DE VENDA", ln=True, align='C')

pdf.set_xy(10, 175)
pdf.cell(200, 10, txt="RECIBO DE VENDA", ln=True, align='C')

# MODALIDADE DE VENDA 01
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(10, 205)
pdf.cell(200, 10, txt="MODALIDADE DE VENDA 01", ln=True, align='C')

# Adiciona a forma1
forma1 = "Descrição da Modalidade 01"
pdf.set_xy(10, 215)
pdf.cell(200, 10, txt=forma1, ln=True, align='C')

# MODALIDADE DE VENDA 02
pdf.set_xy(10, 235)
pdf.cell(200, 10, txt="MODALIDADE DE VENDA 02", ln=True, align='C')

# Adiciona a forma2
forma2 = "Descrição da Modalidade 02"
pdf.set_xy(10, 245)
pdf.cell(200, 10, txt=forma2, ln=True, align='C')

# MODALIDADE DE VENDA 03
pdf.set_xy(10, 265)
pdf.cell(200, 10, txt="MODALIDADE DE VENDA 03", ln=True, align='C')

# Adiciona a forma3
forma3 = "Descrição da Modalidade 03"
pdf.set_xy(10, 275)
pdf.cell(200, 10, txt=forma3, ln=True, align='C')

# Salvar o PDF
pdf.output("modalidades_venda.pdf")

print("PDF gerado com sucesso!")

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Título do documento
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'DADOS DE VENDA - FORMULÁRIO', 0, 1, 'C')
        self.ln(10)

    def dados_cliente(self):
        # Seção de Dados do Cliente
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'DADOS DO CLIENTE', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Nome / Razão Social: ___________________________', 0, 1, 'L')
        self.cell(0, 10, 'CPF / CNPJ: ___________________________________', 0, 1, 'L')
        self.cell(0, 10, 'Endereço: _____________________________________', 0, 1, 'L')
        self.ln(10)

    def itens_vendidos(self):
        # Seção de Itens Vendidos
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ITENS VENDIDOS', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        for i in range(1, 9):  # Lista de itens
            self.cell(0, 10, f'ITEM {i}: ____________________________________', 0, 1, 'L')
        self.ln(10)

    def formas_pagamento(self):
        # Seção de Formas de Pagamento
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'FORMAS DE PAGAMENTO', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'À VISTA: [ ]   PIX: [X]   CARTÃO: [ ]', 0, 1, 'L')
        self.cell(0, 10, 'Bandeira: _____________________________________', 0, 1, 'L')
        self.cell(0, 10, 'Observações: __________________________________', 0, 1, 'L')
        self.ln(10)

    def termos_condicoes(self):
        # Seção de Termos e Condições
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'TERMOS E CONDIÇÕES DE COMPRA E VENDA', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, 'Eu, FÊNIX TESLA ELETRÔNICOS RECUPERÁVEIS LTDA inscrita sob o CNPJ '
                                'de nº 47.103.686/0001-00, recebi de ______________________, inscrito(a) sob '
                                'o CPF/CNPJ de nº ________________ a importância de R$ __________ referente à '
                                'venda dos itens relacionados acima.')
        self.ln(10)

    def assinatura(self):
        # Assinaturas
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'São Paulo, ____ de _______________ de 2024', 0, 1, 'L')
        self.ln(10)
        self.cell(0, 10, '_____________________________', 0, 1, 'L')
        self.cell(0, 10, 'ASSINATURA DO CLIENTE', 0, 1, 'L')
        self.ln(5)
        self.cell(0, 10, '_____________________________', 0, 1, 'L')
        self.cell(0, 10, 'ASSINATURA DO VENDEDOR', 0, 1, 'L')

# Criação do PDF
pdf = PDF()

# Adiciona página e conteúdo
pdf.add_page()
pdf.dados_cliente()
pdf.itens_vendidos()
pdf.formas_pagamento()
pdf.termos_condicoes()
pdf.assinatura()

# Gera o PDF
pdf_file = r"C:\Users\TEUCNC\Desktop\formulario_venda.pdf"
pdf.output(pdf_file)

print(f'Arquivo PDF criado com sucesso: {pdf_file}')

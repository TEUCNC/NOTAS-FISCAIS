from openpyxl import Workbook
from openpyxl.styles import Border, Side

# Criação do livro e da planilha
wb = Workbook()
sheet= wb.active

# bloco responsável pelas bordas
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)
# texto
sheet['L2'] = '=COUNTIF(I:I, "*indicação*")'
sheet['L2'].border = thin_border

sheet['L3'] = '=COUNTIF(I:I, "*google*")'
sheet['L3'].border = thin_border

sheet['L4'] = '=COUNTIF(I:I, "*facebook*")'
sheet['L4'].border = thin_border

sheet['L5'] = '=COUNTIF(I:I, "*instagram*")'
sheet['L5'].border = thin_border

sheet['L6'] = '=COUNTIF(I:I, "*mercado livre*")'
sheet['L6'].border = thin_border

sheet['L7'] = '=COUNTIF(I:I, "*OLX*")'
sheet['L7'].border = thin_border

sheet['L8'] = '=COUNTIF(I:I, "*site*")'
sheet['L8'].border = thin_border





sheet['K1'] = 'Modalidade de venda'
# config de borda
sheet['K1'].border = thin_border

sheet['K2'] = 'Indicação'
sheet['K2'].border = thin_border

sheet['K3'] = 'Google'
sheet['K3'].border = thin_border

sheet['K4'] = 'Facebook'
sheet['K4'].border = thin_border

sheet['K5'] = 'Instagram'
sheet['K5'].border = thin_border

sheet['K6'] = 'Mercado Livre'
sheet['K6'].border = thin_border

sheet['K7'] = 'OLX'
sheet['K7'].border = thin_border

sheet['K8'] = 'Site'
sheet['K8'].border = thin_border

sheet['L1'] = 'QUANT.'
sheet['L1'].border = thin_border

sheet['N1'] = 'Formas de pagamento'
sheet['O1'] = 'QUANT.'

sheet['Q1'] = 'Categoria'
sheet['R1'] = 'QUANT.'

# Salvando o arquivo
wb.save('seu_novo_arquivo.xlsx')
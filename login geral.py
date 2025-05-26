import openpyxl

# Exemplo de lista
itens = ["Item 1", "Item 2", "Item 3", "Item 4"]

# Função para colocar os itens de uma lista em uma célula
def adicionar_lista_na_celula_com_quebra(sheet, row, col, lista):
    # Une os itens da lista em uma única string com quebras de linha
    conteudo = "\n".join(lista)
    # Adiciona a string na célula
    cell = sheet.cell(row=row, column=col)
    cell.value = conteudo
    # Ativa a quebra de texto na célula
    cell.alignment = openpyxl.styles.Alignment(wrap_text=True)


# Carregar ou criar um workbook
workbook = openpyxl.Workbook()

# Seleciona a primeira aba
sheet = workbook.active

# Chama a função para adicionar a lista na célula A1
adicionar_lista_na_celula_com_quebra(sheet, 1, 1, itens)

# Salva o arquivo Excel
workbook.save("exemplo_lista_excel.xlsx")



quebra_itens(sheet, proxima_linha, 6, itens)
quebra_itens_class(sheet, proxima_linha, 7, itens)
quebra_modalidade_venda(sheet, proxima_linha, 9, itens)

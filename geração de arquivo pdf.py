import os
from fpdf import FPDF


# Função para gerar o próximo número sequencial baseado nos arquivos já existentes no diretório
def proximo_numero_arquivo(diretorio):
    # Lista os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtra os arquivos que seguem o padrão "numero.pdf"
    numeros = [int(f.split('.')[0]) for f in arquivos if f.endswith('.pdf') and f.split('.')[0].isdigit()]

    # Se existirem arquivos, retorna o próximo número, caso contrário, retorna 1
    if numeros:
        return max(numeros) + 1
    else:
        return 1

# Defina o diretório onde deseja salvar os arquivos
diretorio = "C:\\Users\\TEUCNC\\Desktop"

# Gera o próximo número sequencial
numero_sequencial = proximo_numero_arquivo(diretorio)

# Criação de um novo PDF
pdf = FPDF()

# Adiciona uma página
pdf.add_page()

# Defina as dimensões da imagem do carimbo
imagem_largura = 60  # Largura da imagem em mm
imagem_altura = 40    # Altura da imagem em mm
# Obtém as dimensões da página (210 x 297 para A4)
largura_pagina = pdf.w  # Largura da página A4
altura_pagina = pdf.h   # Altura da página A4
# Calcula as coordenadas x e y para posicionar a imagem no canto inferior direito
x_posicao = largura_pagina - imagem_largura - 5  # 10 mm de margem da borda direita
y_posicao = altura_pagina - imagem_altura - 10    # 10 mm de margem da borda inferior
# Adiciona a imagem no canto inferior direito
pdf.image("C:\\Users\\TEUCNC\\Desktop\\imagem.png", x=x_posicao, y=y_posicao, w=imagem_largura, h=imagem_altura)


# Defina as dimensões da imagem da logo
imagem_largura = 40  # Largura da imagem em mm
imagem_altura = 40    # Altura da imagem em mm
# Obtém as dimensões da página (210 x 297 para A4)
largura_pagina = pdf.w  # Largura da página A4
altura_pagina = pdf.h   # Altura da página A4
# Calcula as coordenadas x e y para posicionar a imagem no canto inferior direito
x_posicao = largura_pagina - imagem_largura - 156  # 10 mm de margem da borda direita
y_posicao = altura_pagina - imagem_altura - 10    # 10 mm de margem da borda inferior
# logo no canto inferior esqeurdo
pdf.image("C:\\Users\\TEUCNC\\Desktop\\logo.png", x=x_posicao, y=y_posicao, w=imagem_largura, h=imagem_altura)


# BLOCO DE LINHAS PARA TÍTULOS
#linha titulo 01
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 14.55) até (200, 14.55)
pdf.line(10, 14.55, 200, 14.55)


# linha para título 02
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 51, 200, 51)

# linha para título 03
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 125, 200, 125)

# linha para título 04
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 140, 200, 140)

# linha para título 05
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(5)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 156, 200, 156)

# linha para título 05
# Define a cor da linha como cinza escuro (RGB: 64, 64, 64)
pdf.set_draw_color(64, 64, 64)
pdf.set_line_width(6)
# Desenha uma linha preta de (10, 15) até (200, 15)
pdf.line(10, 176, 200, 176)




# BLOCO DE CÓDIGO PARA TÍTULOS
# Define a fonte: Arial, tamanho 16
# Define a formatação para o título
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 10, txt="DADOS DO CLIENTE", ln=True, align='C')
# Primeiro valor é a distancia da margem do lado direito
# Segundo valor é a distancia da margem superior da página

# ITENS VENDIDOS
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 62, txt="ITENS VENDIDOS", ln=True, align='C')

# FORMAS DE PAGAMENTO
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 86.30, txt="FORMAS DE PAGAMENTO", ln=True, align='C')

# MODALIDADE DE ENTREGA
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, -55.90, txt="MODALIDADE DE ENTREGA", ln=True, align='C')

# MODALIDADE DE VENDA
pdf.set_font("Arial", style='B', size=16)
pdf.set_text_color(255, 255, 255)
# Adiciona um título
pdf.cell(200, 87.90, txt="MODALIDADE DE VENDA", ln=True, align='C')

# MODALIDADE DE VENDA
pdf.set_font("Arial", style='B', size=18)
pdf.set_text_color(0, 0, 0)
# Adiciona um título
pdf.cell(200, -47.95, txt="RECIBO DE VENDA", ln=True, align='C')



#linha do carimbo
# OK
# Define a cor da linha como preta (RGB: 0, 0, 0)
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0)
# Desenha uma linha preta de (10, 50) até (200, 50)
pdf.line(145, 286, 205.5, 286)

#linha do LOGO
# OK
# Define a cor da linha como preta (RGB: 0, 0, 0)
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0)
# Desenha uma linha preta de (10, 50) até (200, 50)
pdf.line(73, 286, 133.5, 286)





# BLOCO CONFIGURADO PARA LISTA DE DADOS DO CLIENTE
lista = ["Dado 1", "Dado 2", "Dado 3", "Dado 4", "Dado 5"]

pdf.set_font("Arial", size=12)
# Define a posição inicial
x_inicial = 10
y_inicial = 22
# Define o espaço horizontal e vertical entre os itens
espaco_entre_itens = 60  # Ajuste conforme necessário para a largura dos itens
espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
# Adiciona o dado na primeira linha
pdf.set_text_color(0, 0, 0)  # Define a cor do texto como preto
pdf.text(x_inicial, y_inicial, lista[0])
# Calcula a nova posição inicial para a segunda linha
x = x_inicial
y = y_inicial + espaco_entre_linhas
# Adiciona três dados na segunda linha
for i in range(1, 4):
    pdf.text(x, y, lista[i])
    x += espaco_entre_itens
# Calcula a nova posição inicial para a terceira linha
x = x_inicial
y = y + espaco_entre_linhas
# Adiciona o dado na terceira linha
pdf.text(x, y, lista[4])

# Para listas comuns
"""
lista = ["Primeiro item", "Segundo item", "Terceiro item", "ausdjfosajdofjsaofd"]

# Define a posição inicial para o texto
x = 7.5
y = 60

# Adiciona cada item da lista ao PDF
for item in lista:
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.text(x, y, item)  # Adiciona o item na posição (x, y)
    y += 10  # Move para a próxima linha (ajuste o valor conforme necessário)"""


# Textos em geral
"""pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
texto = "Este é um parágrafo de exemplo em um arquivo PDF gerado com Python."
texto2 = "teste"
pdf.multi_cell(0, 10, txt=texto)
pdf.multi_cell(0, 3, txt=texto2)"""

# Para lista dos itens venvidos
lista = ["Primeiro item", "Segundo item", "Terceiro item", "ausdjfosajdofjsaofd"]

# Define a posição inicial para o texto
x = 7.5
y = 60
# Adiciona cada item da lista ao PDF
for item in lista:
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.text(x, y, item)  # Adiciona o item na posição (x, y)
    y += 5  # Move para a próxima linha (ajuste o valor conforme necessário)



# BLOCO QUE DEFINE A FORMA DE PAGAMENTO
lista = ["Dado 1", "Dado 2", "Dado 3"]

pdf.set_font("Arial", size=12)
# Define a posição inicial
x_inicial = 40
y_inicial = 124
# Define o espaço horizontal e vertical entre os itens
espaco_entre_itens = 60  # Ajuste conforme necessário para a largura dos itens
espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
# Adiciona o dado na primeira linha
# Define a cor do texto como preto
pdf.set_text_color(0, 0, 0)
# Calcula a nova posição inicial para a segunda linha
x = x_inicial
y = y_inicial + espaco_entre_linhas
# Adiciona três dados na segunda linha
for i in range(0, 3):
    pdf.text(x, y, lista[i])
    x += espaco_entre_itens



# BLOCO QUE DEFINE A MODALIDADE DA VENDA
lista = ["Dado 1", "Dado 2"]

pdf.set_font("Arial", size=12)
# Define a posição inicial
x_inicial = 40
y_inicial = 156
# Define o espaço horizontal e vertical entre os itens
espaco_entre_itens = 105  # Ajuste conforme necessário para a largura dos itens
espaco_entre_linhas = 10  # Ajuste conforme necessário para a altura dos itens
# Adiciona o dado na primeira linha
# Define a cor do texto como preto
pdf.set_text_color(0, 0, 0)
# Calcula a nova posição inicial para a segunda linha
x = x_inicial
y = y_inicial + espaco_entre_linhas
# Adiciona três dados na segunda linha
for i in range(0, 2):
    pdf.text(x, y, lista[i])
    x += espaco_entre_itens


# BLOCO PARA CENTRALIZAR A MODALIDADE DE ENTREGA
# SUBISTITUIR O TEXTO DENTRO DO BLOCO
# Define a fonte
pdf.set_font("Arial", size=16)
# Texto que será centralizado
texto = "Texto Centralizado"
# Calcula a posição X para centralizar o texto
page_width = pdf.w  # Largura total da página
text_width = pdf.get_string_width(texto)  # Largura do texto
x_position = (page_width - text_width) / 2  # Calcula a posição central
# Adiciona o texto centralizado na página
pdf.text(x_position, 150, texto)





# Textos fixos na parte de baixo
pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
pdf.text(150, 290, "ASSINATURA DO VENDEDOR")

pdf.set_font("Arial", style='B', size=10)
pdf.set_text_color(0, 0, 0)
pdf.text(80, 290, "ASSINATURA DO CLIENTE")

# Define o nome do arquivo com base no número sequencial
nome_arquivo = f"{numero_sequencial}.pdf"

# Salva o arquivo em PDF no diretório especificado
pdf.output(os.path.join(diretorio, nome_arquivo))

print(f"Documento PDF '{nome_arquivo}' criado com sucesso!")

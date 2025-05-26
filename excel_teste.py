from datetime import datetime
tipo_cliente = input("tipo 1 ou 2")
data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y ")
hora_formatada = data_atual.strftime("%H:%M:%S")
form1 = "teste1"
forma2 = "teste2"
forma3 = "teste3"
itens = ["1asdfasdfsdaf", "2sadfasdfsadfsfda", "3sfsafdsadfsadf"]
itens_class = ["notebook", "nobreak", "monitor"]
modalidade_venda = ["Facebook", "mercado pago"]
#DADOS PESSOAIS OU EMPRESARIAIS NA PLANILIA
if tipo_cliente in ("1", "CPF", "cpf", "Pessoa Fisica"):
    nome_cliente = "NOME"
    cpf_cliente = "CPF"
    tele_cleinte = "TELEFONE_PESSOA"
    sheet_atual[f'B{proxima_linha}'] = nome_cliente
    sheet_atual[f'C{proxima_linha}'] = cpf_cliente
    sheet_atual[f'D{proxima_linha}'] = tele_cleinte

elif tipo_cliente in ("1", "CPF", "cpf", "Pessoa Fisica"):
    razion_social_empresa = "NOME EMPRESA"
    cnpj_cliente = "CNPJ"
    tele_cleinte = "TELEFONE_EMPRESA"
    sheet_atual[f'B{proxima_linha}'] = razion_social_empresa
    sheet_atual[f'C{proxima_linha}'] = cnpj_cliente
    sheet_atual[f'D{proxima_linha}'] = tele_cleinte

sheet_atual[f'E{proxima_linha}'] = data_formatada, hora_formatada
sheet_atual[f'F{proxima_linha}'] = itens
sheet_atual[f'G{proxima_linha}'] = itens_class
#FORMA DE PAGAMENTO
if combinar_pagamento in ("S", "SIM"):
    if quant_pagamentos == 2:
        sheet_atual[f'H{proxima_linha}'] = forma1, forma2
    if quant_pagamentos == 3:
        sheet_atual[f'H{proxima_linha}'] = forma1, forma2, forma3

if combinar_pagamento in ("N", "NÃO", "NAO") or quant_pagamentos == 1:
    sheet_atual[f'H{proxima_linha}'] = forma1
    #EM CASO DE NEGAÇÃO

sheet_atual[f'I{proxima_linha}'] = modalidade_venda

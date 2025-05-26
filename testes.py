def empresa_cnpj():
    global endere_cliente_complemento
    cnpj = "CNPJ"
    razion_social_empresa = naovazia("Razão Social: ")
    cnpj_cliente2 = verif_num_pode_vazio("Digite o CNPJ da empresa: ")
    cnpj_cliente = str(cnpj_cliente2)

    insc_estadual_exist = verif_resposta("A empresa possuí Inscrição Estadual? (SIM ou NÃO) ").strip().upper()

    # Estrutura de verificação da resposta
    if insc_estadual_exist in ("S", "SIM"):
        insc_estadual2 = verif_num_pode_vazio("Qual é a Inscrição Estadual da empresa? ")
        insc_estadual = str(insc_estadual2)
    else:
        pass

    tele_cleinte2 = verif_num_pode_vazio("Digite o número de contato da empresa: ")
    tele_cleinte = str(tele_cleinte2)

    tele_verifciacione = verif_resposta("O telefone de contato acima tem Whatsapp? (SIM ou NÃO) ")
    endere_cliente_rua = input("Qual é o endereço da rua onde o cliente mora? ")
    endere_cliente_num = verif_num_pode_vazio("Qual é o número da empresa cliente? ")
    endere_cliente_complemento_exist = verif_resposta(
        "O endereço acima possuí complemento? (SIM ou NÃO) ").strip().upper()

    # Estrutura de verificação da resposta
    if endere_cliente_complemento_exist in ("S", "SIM"):
        endere_cliente_complemento = input("Qual é o complemento do endereço? ")
    else:
        pass

    endere_cliente_bairro = input("Qual bairro a empresa se encontra? ")
    endere_cliente_cep2 = verif_num_pode_vazio("Qual é o CEP da empresa cliente? (DIGITE APENAS NÚMEROS) ")
    endere_cliente_cep = (endere_cliente_cep2)


    # Bloco para combinar e armazenar os dados do cliente:
    empresa_dados.append("Razão social: " + nome_cliente)
    empresa_dados.append("CNPJ: " + cpf_cliente)

    if insc_estadual_exist in ("S", "SIM"):
        empresa_dados.append("Inscrição Estadual: " + insc_estadual)
    else:
        empresa_dados.append("Inscrição Estadual: "+insc_estadual_exist)

    empresa_dados.append("Telefone: " + tele_cleinte)

    if tele_verifciacione in ("S", "SIM"):
        empresa_dados.append("Whatsapp: SIM")

    else:
        empresa_dados.append("Whatsapp: NÃO")

    empresa_dados.append("Whatsapp")
    if endere_cliente_complemento_exist in ("S", "SIM"):
        empresa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + " " + endere_cliente_complemento + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)
    else:
        empresa_dados.append(
            "Endereço: " + endere_cliente_rua + ", " + endere_cliente_num + ", " + endere_cliente_bairro + ", " + endere_cliente_cep)



    empresa_cnpj()
    limpartela()
    print("Verifique os dados do cliente: ")
    sleep(1)
    for dados in empresa_dados:
        print(dados)


    # Bloco para verificar se os dados estão corretos
    item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
    if item_verificacione in ("S", "SIM"):
        pass
        limpartela()
    if item_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
        verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
        if verif_pedido_recomeco in ("S", "SIM"):
            empresa_dados.clear()
            limpartela()
            empresa_cnpj()
            limpartela()

    # Bloco enquanto o pedido for errado (o vendedor quiser editar ele entra em loop limpando a lista)
    while item_verificacione not in ("S", "SIM"):
        for dados in empresa_dados:
            print(dados)

        # Bloco para verificar se o pedido está correto
        item_verificacione = verif_resposta("\n Os dados acima estão corretos?(SIM ou NÃO) ").strip().upper()
        if item_verificacione in ("S", "SIM"):
            pass
            limpartela()

        if item_verificacione in ("N", "NÃO", "NAO"):
            # Bloco verifica se realmente o vendedor deseja recomeçar o pedido
            verif_pedido_recomeco = verif_resposta("Deseja recomeçar o cadastro dos dados?(SIM ou NÃO)").strip().upper()
            if verif_pedido_recomeco in ("S", "SIM"):
                emrpesa_dados.clear()
                limpartela()
                empresa_cnpj()
                limpartela()
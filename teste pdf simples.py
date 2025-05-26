def pagamentos_formas():
    global pag, pag_parcelas

    forma_pagamento = int(input("Escolha a forma de pagamento:\n"
                                "1) À Vista Débito\n"
                                "2) Mercado Livre\n"
                                "3) À Vista PIX\n"
                                "4) Via Link\n"
                                "5) OLX PAY\n"
                                "6) Crédito\n"))

    if forma_pagamento == 1:
        formas_de_pagamento.append("À Vista Débito")

    elif forma_pagamento == 2:
        formas_de_pagamento.append("Mercado Livre")

    elif forma_pagamento == 3:
        formas_de_pagamento.append("À Vista PIX")

    elif forma_pagamento == 4:
        formas_de_pagamento.append("Via Link")

    elif forma_pagamento == 5:
        formas_de_pagamento.append("OLX PAY")

    elif forma_pagamento == 6:
        credito = "Crédito"
        pag_parcelas2 = verif_num("Serão quantas parcelas? ")
        pag_parcelas = str(pag_parcelas2)
        formas_de_pagamento.append(credito + f" Parcelado em {pag_parcelas}X")
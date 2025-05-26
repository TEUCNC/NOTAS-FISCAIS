pagamento_verificacione = verif_resposta("\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
if pagamento_verificacione in ("S", "SIM"):
    pass
    limpartela()
if pagamento_verificacione in ("N", "NÃO", "NAO"):
    # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
    verif_pagamento_recomeco = verif_resposta("Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
    if verif_pagamento_recomeco in ("S", "SIM"):
        formas_de_pagamento.clear()
        limpartela()
        pagamentos_formas()
        limpartela()
while pagamento_verificacione not in ("S", "SIM"):
    for pagamentosformas, formas_de_pagamento in enumerate(formas_de_pagamento, start=1):
        print(f"{pagamentosformas}º Forma de pagamento: {formas_de_pagamento}")

    # Bloco para verificar se as formas de pagamento estão corretas
    pagamento_verificacione = verif_resposta("\n As formas de pagamento estão corretos?(SIM ou NÃO) ").strip().upper()
    if pagamento_verificacione in ("S", "SIM"):
        pass
        limpartela()

    if pagamento_verificacione in ("N", "NÃO", "NAO"):
        # Bloco verifica se realmente o vendedor deseja recomeçar as formas de pagamento
        verif_pagamento_recomeco = verif_resposta("Deseja recomeçar o cadastro das formas de pagamento?(SIM ou NÃO)").strip().upper()
        if verif_pagamento_recomeco in ("S", "SIM"):
            formas_de_pagamento.clear()
            limpartela()
            pagamentos_formas()
            limpartela()

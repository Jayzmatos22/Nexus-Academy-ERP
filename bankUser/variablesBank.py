
# Bancos disponíveis para seleção pelo usuário.
banks = {
    "1": "BANCO DO BRASIL",
    "2": "CAIXA ECONÔMICA FEDERAL",
    "3": "BNDES",
    "4": "BANRISUL",
    "5": "BANESTES",
    "6": "BANCO DA AMAZÔNIA",
    "7": "BANCO DO NORDESTE",
    "8": "ITAÚ UNIBANCO",
    "9": "BRADESCO",
    "10": "SANTANDER",
    "11": "BTG PACTUAL",
    "12": "SAFRA",
    "13": "SICREDI",
    "14": "SICOOB",
    "15": "NUBANK",
    "16": "BANCO INTER",
    "17": "C6 BANK",
    "18": "NEON",
    "19": "PAGBANK",
    "20": "MERCADO PAGO",
    "21": "WILL BANK",
    "22": "NEXT",
    "23": "BANCO ORIGINAL",
    "24": "BANCO PAN",
    "25": "BS2",
    "26": "AGIBANK",
    "27": "BMG",
    "28": "MODAL",
    "29": "UNICRED",
    "30": "CRESOL",
    "31": "AILOS",
    "32": "CITIBANK",
    "33": "JP MORGAN",
    "34": "HSBC",
    "35": "BNP PARIBAS",
    "36": "DEUTSCHE BANK"
}



# Códigos dos bancos.
banks_code = {
    "BANCO DO BRASIL": "001",
    "CAIXA ECONÔMICA FEDERAL": "104",
    "BNDES": "007",
    "BANRISUL": "041",
    "BANESTES": "021",
    "BANCO DA AMAZÔNIA": "003",
    "BANCO DO NORDESTE": "004",
    "ITAÚ UNIBANCO": "341",
    "BRADESCO": "237",
    "SANTANDER": "033",
    "BTG PACTUAL": "208",
    "SAFRA": "422",
    "SICREDI": "748",
    "SICOOB": "756",
    "NUBANK": "260",
    "BANCO INTER": "077",
    "C6 BANK": "336",
    "NEON": "735",
    "PAGBANK": "290",
    "MERCADO PAGO": "323",
    "WILL BANK": "280",
    "NEXT": "237",
    "BANCO ORIGINAL": "212",
    "BANCO PAN": "623",
    "BS2": "218",
    "AGIBANK": "121",
    "BMG": "318",
    "MODAL": "746",
    "UNICRED": "136",
    "CRESOL": "133",
    "AILOS": "085",
    "CITIBANK": "745",
    "JP MORGAN": "376",
    "HSBC": "399",
    "BNP PARIBAS": "752",
    "DEUTSCHE BANK": "487"
}


# MÁXIMO E MÍNIMO DEPÓSITO.
range_deposit_bank = (20, 100000.0)

# VALORES DE COMPRAS.
quantity_debts = []


# HISTÓRICO DE COMPRAS.
purchase_history = {}


# VARIÁVEIS DO DICIONÁRIO ANINHADO.
# F: evitar erros e automatizar.
name_of_purchase = 'nome compra'
unit_price = 'preço unitário'
quantity_of_items = 'quantidade item'
total_value = 'preço total'
description_purchase = 'descrição compra'
purchase_type = 'tipo de compra'
# Tipos de compras.
types_purchase = {
                1: 'cartão de crédito', 
                2: 'cartão de débito',
                3: 'dinheiro à vista', 
                4: 'pagamento boleto'}


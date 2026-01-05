from allFunctions.insertionTypes import insertion_void, space, insertion_float, insertion_int
from anscii_sistem.collors import text_collor, text_format, background_collors
from emojizeSistem.dict_emojize import utility_symbols1, utility_symbols2, techEmojis, workEmojis, financeEmojis, emojisAcademy2
from utils.utilsUx import ej
from bankUser.variablesBank import banks, banks_code, range_deposit_bank, quantity_debts, purchase_history, name_of_purchase, unit_price, quantity_of_items, total_value, description_purchase, purchase_type, types_purchase
from allFunctions.user_data_var import user_data_dictionary
import time
from datetime import datetime
import numpy as np
import pandas as pd

NOW = datetime.now().date()

# Dicionário sobre dados bancários do usuário.
bank_user_data = {}


def get_bank_code(bank_name):
    return banks_code.get(bank_name, None)


# FUNÇÃO DE CRIAÇÃO DE USUÁRIO BANCÁRIO.
def create_bank_user():
    while True:

        if bank_user_data:
            space()
            time.sleep(0.3)
            print(f'{text_collor["yellow"]} {ej(utility_symbols1["info"])}  Você já possui uma conta bancária criada no banco {bank_user_data["banco"]}.\033[m\n')
            break

        else:

            print(f'{text_format["highlighted"]}{background_collors["green"]} {ej(financeEmojis["banco"])}  CRIAÇÃO DE CONTA BANCÁRIA  {ej(financeEmojis["banco"])} \033[m\n')
            print(f'{text_format["highlighted"]}{text_collor["white"]} SELECIONE O BANCO ONDE DESEJA CRIAR SUA CONTA (1-{len(banks)}):\033[m\n')

            for code, name in banks.items():
                print(f'{text_format["highlighted"]}{background_collors["gray"]} {code} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{name}.\033[m')
            space()

            bank_user = insertion_void(f'{text_format["highlighted"]} INSTITUIÇÃO FINANCEIRA/BANCO:\033[m ').strip()
            get_bank = banks.get(bank_user, None)
            if get_bank is None:
                space()
                print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, opção inválida.{text_format["none"]}\n')
                continue

            else:
                # Verificação se já existe o campo 'valor conta' no dicionário.
                bank_user_data.setdefault('valor conta', 0.0)

                # Atribuição dos dados bancários ao dicionário.
                bank_code = get_bank_code(get_bank)
                cpf_user = user_data_dictionary.get('cpf', None)
                bank_user_data['banco'] = get_bank
                bank_user_data['código banco'] = bank_code
                bank_user_data['cpf titular'] = cpf_user
                space()
                print(f'{text_format["highlighted"]}{text_collor["green"]} {ej(financeEmojis["grafico_subindo"])}  Conta bancária criada com sucesso.\033[m\n')
                break


# FLOAT COM 2 CASAS DECIMAIS.
def valid_monetary_value(msg):
    while True:
        try:
            user_input_float = input(msg).strip()
            return round(float(user_input_float), 2)
        
        except ValueError:
            space()
            print(f'{text_collor["red"]}Erro, digite apenas numeros reais.{text_format["none"]}')
            space()

# FUNÇÃO DE DEPÓSITO BANCÁRIO.
def deposit_in_the_bank():
    while True:

        if not bank_user_data:
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, você ainda não possui uma conta bancária criada.\033[m\n')
            break

        # Valores mínimos e máximos para depósito.
        min_deposit = min(range_deposit_bank)
        max_deposit = max(range_deposit_bank)

        print(f'{text_format["highlighted"]}{background_collors["green"]} {ej(financeEmojis["saco_dinheiro"])} DEPÓSITO BANCÁRIO  {ej(financeEmojis["grafico_subindo"])} \033[m\n')
        print(f'{text_format["highlighted"]}{text_collor["white"]} INSIRA O VALOR DO DEPÓSITO (MÍNIMO R$ {min_deposit:.2f} E MÁXIMO R$ {max_deposit:.2f}):\033[m\n')

        deposit_amount = valid_monetary_value(f'{text_format["invert"]} VALOR DO DEPÓSITO (R$):\033[m ')
        if deposit_amount < min_deposit or deposit_amount > max_deposit:
            time.sleep(0.3)
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, valor inválido para depósito. mínimo: R$ {min_deposit:.2f} e máximo: R$ {max_deposit:.2f}.{text_format["none"]}\n')
            continue

        else:
            total = bank_user_data.get('valor conta', 0.0) + deposit_amount
            bank_user_data['valor conta'] = total
            space()
            print(f'{text_format["highlighted"]}{text_collor["green"]} {ej(financeEmojis["saco_dinheiro"])}  Depósito de R$ {deposit_amount} realizado com sucesso.\033[m\n')

        # Continuar realizando depósitos?
        while True:
            space()
            another_deposit = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA REALIZAR OUTRO DEPÓSITO? (1: SIM - 0: NÃO):\033[m ').strip()
            valid_response = ['1', '0']
            if another_deposit not in valid_response:
                time.sleep(0.3)
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                continue

            elif another_deposit == '1':
                space()
                break

            elif another_deposit == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                return
            
            
# FUNÇÃO DE SAQUE BANCÁRIO.
def withdraw_from_bank():
    while True:

        if not bank_user_data:
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, você ainda não possui uma conta bancária criada.\033[m\n')
            return
        
        if bank_user_data.get('valor conta', 0.0) <= 0.0:
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, saldo insuficiente para saque.\033[m\n')
            return

        print(f'{text_format["highlighted"]}{background_collors["green"]} {ej(financeEmojis["caixa_eletronico"])} SAQUE BANCÁRIO  \033[m\n')

        total_balance = bank_user_data.get('valor conta', 0.0)
        print(f'{text_format["highlighted"]}{text_collor["white"]} SEU SALDO ATUAL É DE R$ {total_balance:.2f}.\033[m\n')

        withdraw_amount = valid_monetary_value(f'{text_format["invert"]} VALOR DO SAQUE (R$):\033[m ')
        if withdraw_amount > total_balance:
            time.sleep(0.3)
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, saldo insuficiente para saque de R$ {withdraw_amount:.2f}. {text_format["none"]}\n')
            continue

        else:
            total_after_withdraw = total_balance - withdraw_amount # Desconto do valor sacado.
            bank_user_data['valor conta'] = total_after_withdraw # Atualização do saldo bancário.
            space()
            print(f'{text_format["highlighted"]}{text_collor["green"]} {ej(financeEmojis["dinheiro_voando"])}  Saque de R$ {withdraw_amount:.2f} realizado com sucesso.\033[m\n')

        # Continuar realizando saques?
        while True:
            space()
            another_withdraw = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA REALIZAR OUTRO SAQUE? (1: SIM - 0: NÃO):\033[m ').strip()
            valid_response = ['1', '0']
            if another_withdraw not in valid_response:
                time.sleep(0.3)
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                continue

            elif another_withdraw == '1':
                break

            else:
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                return  


# Quantidade mínima para compra.
def validation_quantity_purchase(qt):
    while True:
        min_quantity = 1
        quantity = insertion_int(qt)
        if quantity < min_quantity:
            space()
            print(f'Quantidade mínima = {min_quantity}\n')
            continue
        return quantity


# NOME DA COMPRA.
def validaton_name_purchase():  
    while True:

        min_name = 10
        max_name = 100
        name = insertion_void(f'{text_format['highlighted']}{ej(emojisAcademy2['caderno'])}  NOME DO LIVRO/CURSO OU MATERIAL A SE COMPRAR: {text_format['none']}')
        if len(name) < min_name or len(name) > max_name:
            space()
            print(f'{ej(utility_symbols2["erro"])}  Tamanho mínimo: {min_name}, máximo: {max_name}\n')
            continue

        return name


# ADICIONAR DÍVIDA
def add_debt(value: float):
    quantity_debts.append(value)


# SOMAR DÍVIDA.
def get_total_future_debt():
    return round(sum(quantity_debts), 2)


# DESCRIÇÃO DA COMPRA.
def validation_description_purchase():
    while True:
        min_description = 6
        max_description = 40
        description = insertion_void(f'{text_format['highlighted']}{ej(emojisAcademy2['documentos'])}  DESCRIÇÃO:\033[m ').lower().strip()
        if len(description) < min_description or len(description) > max_description:
            print(f'{ej(utility_symbols2['erro'])}  Descrição entre {min_description} e {max_description} caracteres.\n')
            continue
        return description


# Validar tipo de compra.
def valid_type_of_purchase():
    while True:
        types = types_purchase
        for number, type in types.items():
            print(f'{number}: {type}')
            time.sleep(0.2)
        space()

        user_type = insertion_int(f'{text_format['highlighted']}{ej(financeEmojis['cartao'])}  TIPO DE COMPRA 1-{len(types)}:\033[m ')
        get_type = types.get(user_type, None)

        if get_type is None:
            space()
            time.sleep(0.2)
            print(f'{ej(utility_symbols2['erro'])}  Selecione uma opção válida.\033[m\n')
            continue
            
        else:
            return get_type



# COMPRAS BANCÁRIAS VOLTADAS À ÁREA DE ESTUDO.
def bank_purchase_study_material():
    while True:

        if not bank_user_data:
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, você ainda não possui uma conta bancária criada.\033[m\n')
            return
        
        if bank_user_data.get('valor conta', 0.0) <= 0.0:
            space()
            print(f'{text_collor["red"]} {ej(utility_symbols2["erro"])}  Erro, saldo insuficiente para realizar compras.\033[m\n')
            return
        
        print(f'{text_format["highlighted"]}{text_collor["green"]}{"--" * 38}\033[m') 
        print(f'{text_format["highlighted"]}{text_collor["gray"]}Planeje suas futuras compras, tenha um balanço de suas compras e economize.{text_format["none"]}')
        print(f'{text_format["highlighted"]}{text_collor["green"]}{"--" * 38}\033[m\n')

        total_balance = bank_user_data.get('valor conta', 0.0)

        name_purchase = validaton_name_purchase()

        
        name_exists = False
        for name, details in purchase_history.items(): # Verificar se já tem compra com mesma chave.
            if name == name_purchase:
                time.sleep(0.3)
                space()
                print(f'{ej(utility_symbols2['erro'])}  Você já tem uma compra registrada com esse nome: "{name_purchase}", escolha outro.\n')
                name_exists = True
                break
        if name_exists:
            continue
        

        price = valid_monetary_value(f'{text_format['highlighted']}{ej(financeEmojis['nota_dolar'])}  PREÇO: {text_format['none']}')
        quantity = validation_quantity_purchase(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  QUANTIDADE: {text_format['none']}')
        description = validation_description_purchase()
        space()
        type_of_purchase_user = valid_type_of_purchase()

        total_price = round(price * quantity, 2) # Valor total.
        add_debt(total_price) # Valor da compra atribuída ao vetor de compras.
        total_purchases = get_total_future_debt() # Soma de todas as compras.

        if total_purchases > total_balance: # Comparação
            print(f'--> Sua dívida atual = \033[31mR$ {total_purchases}\033[m, data: {NOW.strftime("%d/%m/%Y")} é maior que seu saldo vigente = \033[32mR$ {total_balance}.\033[m\n'
                f'Esteja seguro de que poderá pagá-la em sua data, caso use cartão de crédito ou boleto.\n')
        else:
            print(f'Sua dívida total atual = \033[31mR$ {total_purchases}\033[m, atualizada: {NOW.strftime("%d/%m/%Y")} é menor que seu saldo vigente = \033[32mR$ {total_balance}. Dívida segura.\033[m\n')
        

        # Armazenar histórico.
        # Usamos as variáveis para ter mais segurança.
        purchase_history[name_purchase] = {
            unit_price: price, quantity_of_items: 
            quantity, total_value: total_price, description_purchase: description,
            purchase_type: type_of_purchase_user
            }
        
        space()
        for i, k in purchase_history.items():
            print(i, k)


        while True: # Continuar ou parar.
            space()
            another_purchase = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA PLANEJAR OUTRA COMPRA? (1: SIM - 0: NÃO):\033[m ').strip()
            valid_response = ['1', '0']
            if another_purchase not in valid_response:
                time.sleep(0.3)
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                continue

            elif another_purchase == '1':
                break

            else:
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                return  



# MOSTRAR HISTÓRICO DE COMPRAS PLANEJADAS.
def display_history_purchase():
    if not purchase_history:
        print(f'{text_format['highlighted']}{text_collor['white']}Você não planejou nenhuma compra ainda!\033[m\n')
        return
    
    else:    
        print(f'{text_format['underline']}{text_format['highlighted']}{text_collor['gray']}{ej(financeEmojis['grafico_subindo'])}  HISTÓRICO DETALHADO DE PLANEJAMENTO DE COMPRAS  {ej(financeEmojis['grafico_descendo'])} {text_format['none']}\n')
        for purchase, detail in purchase_history.items():
            print(f'{text_format['highlighted']}{ej(utility_symbols2['editar'])}  COMPRA PLANEJADA:\033[m {text_format['highlighted']}{text_collor['white']}{purchase}  {ej(utility_symbols2['seta_retorno'])}\033[m\n'
                f'{text_format['highlighted']}{ej(financeEmojis['nota_dolar'])}  {unit_price}:\033[m {text_collor['red']}R$ {detail[unit_price]}\033[m\n'
                f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  {quantity_of_items}:\033[m {text_format['highlighted']}{text_collor['white']}{detail[quantity_of_items]}\033[m\n'
                f'{text_format['highlighted']}{ej(financeEmojis['saco_dinheiro'])}  {total_value}:\033[m {text_collor['red']}R$ {detail[total_value]}\033[m\n'
                f'{text_format['highlighted']}{ej(emojisAcademy2['documentos'])}  {description_purchase}:\033[m {text_format['highlighted']}{text_collor['white']}{detail[description_purchase]}\033[m\n'
                f'{text_format['highlighted']}{ej(financeEmojis['cartao'])}  {purchase_type}:\033[m {text_format['highlighted']}{text_collor['white']}{detail[purchase_type]}\033[m')
            space()

        current_debt = get_total_future_debt() # Get total.
        current_balance = bank_user_data.get('valor conta', 0.0) # Carteira atual.

        if current_debt > current_balance: # Comparação
            print(f'{ej(financeEmojis["grafico_descendo"])}  \033[33m-->\033[m Sua dívida atual = \033[31mR$ {current_debt}\033[m, data: {NOW.strftime("%d/%m/%Y")} é maior que seu saldo vigente = \033[32mR$ {current_balance}.\033[m\n'
                f'Esteja seguro de que poderá pagá-la em sua data, caso use cartão de crédito ou boleto.\n')
        else:
            print(f'{ej(financeEmojis["grafico_subindo"])}  --> Sua dívida total atual = \033[31mR$ {current_debt}\033[m, atualizada: {NOW.strftime("%d/%m/%Y")} é menor que seu saldo vigente = \033[32mR$ {current_balance}. Dívida segura.\033[m\n')


# Estatísticas
def general_statistics_purchase():
    while True:
        current_debt = get_total_future_debt()
        current_balance = bank_user_data.get('valor conta', 0.0)
        if not purchase_history:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Nenhuma pré-dívida/compra planejada ainda.\n')
            return
        
        print(f'{text_format['highlighted']}{"=" * 72}\033[m')
        print(f'{text_format['highlighted']}{ej(financeEmojis["grafico_subindo"])}  Saldo em caixa: {text_collor['green']}R$ {current_balance}.\033[m')
        print(f'{text_format['highlighted']}{ej(financeEmojis["grafico_descendo"])}  Pré_dívida planejada em compras: {text_collor['red']}R$ {current_debt}\033[m\n')

         
        debts = quantity_debts
        list_debts = debts
        subtotals_per_history = []

        # Total de cada compra.
        for purchase, detail in purchase_history.items():
            
            value = detail.get(total_value, 0.0) 
            subtotals_per_history.append(value)

        standard_deviation = np.std(subtotals_per_history) # Desvio padrão
        mean_debts = np.mean(list_debts) # Média
        max_purchase = np.max(subtotals_per_history) # Mínimo
        min_purchase = np.min(subtotals_per_history) # Máximo

        if mean_debts > 0:
            deviation_percentage = (standard_deviation / mean_debts) * 100
        else:
            deviation_percentage = 0

        # Valores marcadores de desvio em porcentagem.
        # Quantidade de itens.
        excellent_detour = 15
        good_detour = 30
        caution_detour = 50
        quantity_purchase = 0
        # QUantidade
        for value in purchase_history.values():
            quantity = value[quantity_of_items]
            quantity_purchase += quantity

        # Percentual de compas.
        p20 = np.percentile(subtotals_per_history, 20) 
        p40 = np.percentile(subtotals_per_history, 40) 
        p60 = np.percentile(subtotals_per_history, 60)
        p80 = np.percentile(subtotals_per_history, 80) 
        p90 = np.percentile(subtotals_per_history, 90)

        # Exibir resultados.
        print(f'{text_format['highlighted']}Média de gasto por compra: {text_collor['red']}R$ {mean_debts:.2f}\033[m\n'
            f'{text_format['highlighted']}Gasto maior: {text_collor['red']}R$ {max_purchase}\033[m\n'
            f'{text_format['highlighted']}Gasto menor: {text_collor['yellow']}R$ {min_purchase:.2f}\033[m\n'
            f'{text_format['highlighted']}Desvio padrão/compras: {text_collor['yellow']}{standard_deviation:.2f}\033[m\n'
            f'{text_format['highlighted']}Quantidade total de itens: {quantity_purchase}')
        
        if len(subtotals_per_history) == 1:
            time.sleep(0.15)
            space()
            print(f'{text_format['highlighted']}{text_collor['white']}Dica: planeje mais compras para ter um balanço real de seus gastos.\n')
            return
        
        
        else:
            if deviation_percentage < excellent_detour:
                time.sleep(0.15)
                print(f'{text_collor['green']}Desvio padrão excelente! {deviation_percentage:.2f}%\033[m')
            elif deviation_percentage <= good_detour:
                time.sleep(0.15)
                print(f'{text_collor['green']}Desvio padrão bom! {deviation_percentage:.2f}%\033[m')
            elif deviation_percentage <= caution_detour:
                print(f'{text_collor['yellow']}Desvio irregular! Preço de gastos/compras oscilam. {deviation_percentage:.2f}%\033[m')
                time.sleep(0.15)
            else:
                print(f'{text_collor['red']}Desvio padrão alto! Você possui muita instabilidade em seus gastos. {deviation_percentage:.2f}%\033[m\n')
                time.sleep(0.15)
            space()

            print(f'{text_format['underline']}{text_format['highlighted']}{text_collor['white']}PERFIL DE DISTRIBUIÇÃO DE GASTOS\033[m')
            print(f'{text_format['highlighted']}Muito barato -> 20% das suas compras vão até {text_collor['green']}R$ {p20:.2f}\033[m\n'
                f'{text_format['highlighted']}Barato -> 40% das suas compras vão até {text_collor['green']}R$ {p40:.2f}\033[m\n'
                f'{text_format['highlighted']}Médio -> 60% das suas compras vão até {text_collor['yellow']}R$ {p60:.2f}\033[m\n'
                f'{text_format['highlighted']}Caro -> 80% das suas compras vão até {text_collor['red']}R$ {p80:.2f}\033[m\n'
                f'{text_format['highlighted']}Muito caro -> 90% das suas compras vão até {text_collor['red']}R$ {p90:.2f}\033[m')

            print(f'{text_format['highlighted']}{"=" * 72}\033[m')
            space()
            return
        

# Exibição de dados bancários.
def display_pandas_bank():
    if not bank_user_data or bank_user_data is None:
        space()
        time.sleep(0.2)
        print(f'{ej(utility_symbols2['erro'])}  Crie uma conta bancária primeiro.\n')
        return
    
    print(f'{text_format['highlighted']}{text_collor['white']}{ej(financeEmojis["banco"])}  SEUS DADOS BANCÁRIOS{text_format['none']}\n')
        
    purchase_pd = pd.DataFrame([bank_user_data])
    purchase_vertical = purchase_pd.T
    print(purchase_vertical.to_string(header=False))



# Histórico de compras em Pandas.
def display_purchase_history_pd():

    if not purchase_history:
        space()
        time.sleep(0.2)
        print(f'{ej(utility_symbols2['erro'])}  Sem histórico em sistema.\n')
        return

    print(f'{text_format['highlighted']}{text_collor['white']}{ej(financeEmojis["caixa_eletronico"])}  HISTÓRICO EM TABELA{text_format['none']}\n')

    # 1. Cria o DataFrame (Chaves do dicionário viram linhas)
    pd_history = pd.DataFrame.from_dict(purchase_history, orient='index')

    # 2. Configurações para o terminal não "esconder" colunas
    pd.set_option('display.max_columns', None)  # Mostra todas as colunas
    pd.set_option('display.expand_frame_repr', False) # Não quebra a tabela em várias partes
    
    
    display_df = pd_history.reset_index().rename(columns={'index': 'Nome_compra'})

    print(display_df.to_string(index=False)) # Imprime sem a numeração extra do Pandas

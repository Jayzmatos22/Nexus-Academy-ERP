# CRUD DO SETOR BANCÁRIO DO ALUNO.
# FACILITAR INTERAÇÃO NO MAIN COM AS FUNÇÕES DE CRUD DO SETOR BANCÁRIO.


from bankUser.functionBank import (
    create_bank_user, deposit_in_the_bank, withdraw_from_bank, bank_purchase_study_material, display_history_purchase,
    general_statistics_purchase, display_pandas_bank, display_purchase_history_pd
    )

from anscii_sistem.collors import text_collor, text_format, background_collors
from utils.utilsUx import ej
import time
from emojizeSistem.dict_emojize import utility_symbols1, utility_symbols2, techEmojis, workEmojis, academyEmojis, emojisAcademy2
from allFunctions.insertionTypes import insertion_void, space



# DICIONÁRIO DE OPÇÕES DO SUBMENU DO SETOR BANCÁRIO DO ALUNO.
dict_optionsBankUser_to_display = {
    '1': 'CRIAR CONTA BANCÁRIA', '2': 'EXIBIR DADOS DA CONTA BANCÁRIA',
    '3': 'DEPOSITAR DINHEIRO', '4': 'SACAR DINHEIRO', '5': 'PLANEJAR COMPRA DE MATERIAL DE ESTUDO',
    '6': 'EXIBIR HISTÓRICO DE COMPRAS', '7': 'ESTATÍSTICAS GERAIS DE COMPRAS'
    }


# MAPEAMENTO DAS OPÇÕES DO SUBMENU DO SETOR BANCÁRIO DO ALUNO.
get_optionsBankUser_functions = {
    '1': create_bank_user, # Criar conta bancária.
    '2': display_pandas_bank, # Exibir dados da conta bancária.
    '3': deposit_in_the_bank, # Depositar dinheiro.
    '4': withdraw_from_bank, # Sacar dinheiro.
    '5': bank_purchase_study_material, # Planejar compra de material de estudo.
    '6': display_purchase_history_pd, # Exibir histórico de compras.
    '7': general_statistics_purchase, # Estatísticas gerais de compras.
    }

# SUB-MENU CRUD PARA SETOR BANCÁRIO DO ALUNO.
def submenu_crud_bankuser():
    for i, options in dict_optionsBankUser_to_display.items():
        print(f'{text_format["highlighted"]}{background_collors["gray"]} {i} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{options}.\033[m')
        time.sleep(0.2)


# CAPTURAR OPÇÃO DO USUÁRIO E EXECUTAR AUTOMATICAMENTE.
def get_function_bankuser():
    while True:
        try:

            space()
            submenu_crud_bankuser()
            space()
            
            messageError = f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n'
            optionUser = str(input(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO BANCÁRIA (0: Sair / 1-{len(dict_optionsBankUser_to_display)}):\033[m '))
            getResult = get_optionsBankUser_functions.get(optionUser, None) # Opção digitada é usada com o método get.

            if optionUser == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo da área bancária...\033[m\n')
                return
            
            if getResult is not None:
                space()
                time.sleep(0.2)
                getResult()  # Chama a função correspondente à opção escolhida.
                
            else:
                time.sleep(0.2)
                print(messageError)
                continue

            while True: # Continuar ou parar.
                    space()
                    another_bank_consultation = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR NA ÁREA BANCÁRIA? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_bank_consultation not in valid_response:
                        time.sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_bank_consultation == '1':
                        space()
                        break

                    else:
                        space()
                        time.sleep(0.3)
                        print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                        return 
                        
        except Exception as e:
            space()
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')

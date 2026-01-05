
from utils.utilsUx import ej
from emojizeSistem.dict_emojize import utility_symbols1, utility_symbols2
from allFunctions.insertionTypes import insertion_void, space
import time
import inspect
from allFunctions.data_user_functions import display_general_personal_data

from allFunctions.data_user_functions import (
    insertion_name, insertion_age, gender_identity_input, 
    biological_sexuality, insertion_cpf
    )
from anscii_sistem.collors import text_collor, text_format, background_collors




# SUB-MENU CRUD PARA DADOS DO USUÁRIO.
def submenu_crud_datauser():
    print(f'{background_collors['yellow']}{text_format["highlighted"]}{text_collor["white"]} {ej(utility_symbols1['usuario'])}'
          f'{ej(utility_symbols1['linha_vertical'])}\033[m{background_collors['light_blue']}{text_format["highlighted"]}{text_collor["white"]} '
          f'* ÁREA DE DADOS PESSOAIS * {ej(utility_symbols1['bloco_solido'])} {text_format["none"]}\n')

    print(f'    {background_collors['gray']}{text_format["highlighted"]}{text_collor["white"]} VISUALIZE, ALTERE DADOS {text_format["none"]}')




dict_optionsDataUser_to_display = {
    '1': 'VISUALIZAR MEUS DADOS PESSOAIS',
    '2': 'ALTERAR NOME',
    '3': 'ATUALIZAR IDADE',
    '4': 'MUDAR GÊNERO/ORIENTAÇÃO SEXUAL',
    '5': 'ALTERAR SEXO BIOLÓGICO',
    '6': 'ALTERAR CPF',
    }



# EXIBIR DICIONÁRIO DE OPÇÕES DO SUBMENU DE DADOS PESSOAIS..
def display_dictOptionsUser():
    for i, options in dict_optionsDataUser_to_display.items():
        print(f'{text_format['highlighted']}{background_collors['gray']} {i} \033[m -> {text_format['highlighted']}{text_collor['white']}{options}.\033[m')
        time.sleep(0.2)
    space()


# MAPEAMENTO DAS OPÇÕES DO SUBMENU DE DADOS PESSOAIS.
options_crudDataUser_dict = {
    '1': display_general_personal_data,
    '2': insertion_name,
    '3': insertion_age,
    '4': gender_identity_input,
    '5': biological_sexuality,
    '6': insertion_cpf,
    }


# MAPEAR ATRIBUIÇÃO DE DADOS NO DICIONÁRIO 'user_data_dictionary'.
map_option_to_key = {
    '2': 'nome',
    '3': 'idade',
    '4': 'gênero sexual',
    '5': 'sexo biológico',
    '6': 'cpf'
}


# DICIONÁRIO PARA SE USAR COM 'options_crudDataUser_dict' E RETORNAR NOME
found = {insertion_name: 'NOME', insertion_age: 'IDADE',
        gender_identity_input: 'GÊNERO SEXUAL', biological_sexuality:
         'SEU SEXO BIOLÓGICO', insertion_cpf: 'CPF'}


# VERIFICAÇÃO DE PARÂMETROS OBRIGATÓRIOS DE UMA FUNÇÃO.
def check_required_params(function):
    """Retorna o número de argumentos posicionais/keyword obrigatórios."""
    
    assing = inspect.signature(function)
    count = 0

    for param in assing.parameters.values():
        # Verifica se o parâmetro não tem valor padrão (é obrigatório)
        if param.default is inspect.Parameter.empty:
            # Verifica se é um parâmetro que pode ser passado posicionalmente
            if param.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, 
                                 inspect.Parameter.POSITIONAL_ONLY):
                count += 1
                
    return count


# CAPTURAR OPÇÃO DO USUÁRIO E EXECUTAR AUTOMATICAMENTE.
def get_dict_optionsCrudDataUser_to_display():
    while True:
        try:
            space()
            messageNewValue = f'{background_collors['green']} {text_format['highlighted']}{ej(utility_symbols2['editar'])}  ATUALIZAR:\033[m '
            messageError = f'{text_collor['red']}{ej(utility_symbols1['erro'])}  Opção inválida, tente novamente.\033[m\n'

            display_dictOptionsUser()
            

            optionUser = str(input(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO DE DADOS PESSOAIS (0: Sair / 1-{len(dict_optionsDataUser_to_display)}):\033[m '))
            getResult = options_crudDataUser_dict.get(optionUser, None) # Opção digitada é usada com o método get.

            if optionUser == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo da área de dados pessoais...\033[m\n')
                return

            if getResult is None:
                time.sleep(0.3)
                space()
                print(messageError)
                continue

            else:
                foundParams = check_required_params(getResult) # Verifica quantos parâmetros obrigatórios a função tem.
                
                if foundParams == 0:
                    # Se não tem parâmetro obrigatório: Chama sem argumentos.
                    space()
                    resultFunction = getResult()
                    space()
                    print(f'{text_format["highlighted"]}{text_collor["green"]}{ej(utility_symbols2["sucesso"])}  Operação realizada com sucesso!.\033[m\n')
                    
                    
                elif foundParams == 1:
                    # Se tem 1 parâmetro obrigatório: Chama com 1 argumento 'messageNewValue'.
                    space()
                    messageNewValue = f'{background_collors["green"]}{text_format["highlighted"]}{ej(utility_symbols2["editar"])}  ATUALIZAR {found[getResult]}:\033[m '
                    resultFunction = getResult(messageNewValue)
                    space()
                    print(f'{text_format["highlighted"]}{text_collor["green"]}{ej(utility_symbols2["sucesso"])}  Operação realizada com sucesso!.\033[m\n')
                    
                
                elif foundParams > 1:
                    # Se tem mais de 1 parâmetro obrigatório: Exibe erro.
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Função com mais de 1 parâmetro obrigatório não suportada.\033[m\n')
                    continue

                # Atualiza o dicionário 'user_data_dictionary' com a nova informação.
                if optionUser in map_option_to_key:
                    from allFunctions.data_user_functions import user_data_dictionary
                    key_to_update = map_option_to_key[optionUser]
                    user_data_dictionary[key_to_update] = resultFunction
                    space()

                    print(f'{text_format["highlighted"]}{text_collor["green"]}'
                        f'{ej(utility_symbols2["sucesso"])}  {key_to_update.upper()} atualizado com sucesso!\033[m\n')
            
            
            while True: # Continuar ou parar.
                    space()
                    another_data_consultation = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR EM DADOS PESSOAIS? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_data_consultation not in valid_response:
                        time.sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_data_consultation == '1':
                        space()
                        break

                    else:
                        space()
                        time.sleep(0.3)
                        print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                        return resultFunction
                        
        except Exception as e:
            space()
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')
           






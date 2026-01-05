# SCRIPTIS E LISTA DE MENUS E/OU SUBMENUS PARA FACILITAR A LIMPEZA NA COMPILAÇÃO MAIN.

import time
from utils.utilsUx import ej
from allFunctions.insertionTypes import insertion_void, space
from emojizeSistem.dict_emojize import utility_symbols1
from emojizeSistem.dict_emojize import academyEmojis, utility_symbols2
from anscii_sistem.collors import text_collor, text_format, background_collors
from allFunctions.user_academy_functions import display_general_academy_data

from subjects_and_tasksAcademy.subjectTaskFunctions import (
    dell_other_loan, display_all_grades_detailed, display_materials, ranking_quantity_activities_per_materials,
    total_activities_semester, max_grade_activities, display_quantity_of_activities_per_matter
    )

from utilsCrud.crudCreate import create_new_task, list_all_created_tasks, delete_task, update_task, total_tasks_created

from subjects_and_tasksAcademy.subjectTaskFunctions import (
    book_loan, other_loan, display_book_loan_plt, display_other_loan,
    dell_book_loan, update_book_loan, update_isbn, total_books_loan
    )


# EXIBIR LAYOUT DO SUBMENU.
def submenu_layout_academy():
    space()
    print(f'     {background_collors['red']}{text_format["highlighted"]}{text_collor["white"]} {ej(academyEmojis['universidade'])}'
          f'{ej(utility_symbols1['linha_vertical'])}\033[m{background_collors['blue']}{text_format["highlighted"]}{text_collor["white"]} *  '
          f'ÁREA DO UNIVERSITÁRIO * {ej(utility_symbols1['bloco_solido'])} {text_format['none']}')

    print(f'{text_format['highlighted']}{text_collor['light_blue']}     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'   {background_collors['green']}{text_format["highlighted"]}{text_collor["white"]} NAVEGUE PELAS FUNCIONALIDADES ABAIXO {text_format["none"]}\n')



# DICIONÁRIO DE OPÇÕES DO SUBMENU ACADÊMICO.
dict_optionsUniversity_to_display = {
    '1': 'EXIBIR DADOS ACADÊMICOS GERAIS', '2': 'LISTAR MINHAS MATÉRIAS DESTE SEMESTRE', 
    '3': 'MATÉRIA COM MAIS ATIVIDADES', '4': 'TOTAL DE ATIVIDADES/PROVAS NO SEMESTRE', '5': 
    'MAIOR NOTA NAS ATIVIDADES/PROVAS', '6': 'TOTAL DE ATIVIDADES POR MATÉRIA', '7': 'NOTAS DETALHADAS POR CADA MATÉRIA E ATIVIDADE'
    }


# EXIBIR DICIONÁRIO DE OPÇÕES DO SUBMENU ACADÊMICO.
def display_dictOptionsUniversity():
    for i, options in dict_optionsUniversity_to_display.items():
        print(f'{text_format['highlighted']}{background_collors['gray']} {i} \033[m -> {text_format['highlighted']}{text_collor['white']}{options}.\033[m')
        time.sleep(0.2)


# DICIONÁRIO COM A FUNÇÃO OBTIDA PELO NÚMERO DA OPÇÃO.
optionsUniversity_dict = {
    '1': display_general_academy_data, '2': display_materials,
    '3': ranking_quantity_activities_per_materials, '4': total_activities_semester, '5': 
    max_grade_activities, '6': display_quantity_of_activities_per_matter, '7': display_all_grades_detailed
    }


# CAPTURAR OPÇÃO DO USUÁRIO E EXECUTAR AUTOMATICAMENTE.
def get_dict_optionsUniversity_to_display():
    while True:
        try:
            space()
            messageError = f'{text_collor['red']}{ej(utility_symbols2['erro'])}  Opção inválida, tente novamente.\033[m\n'

            display_dictOptionsUniversity()
            space()

            optionUser = str(input(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO ACADÊMICA (0: Sair / 1-{len(dict_optionsUniversity_to_display)}):\033[m '))
            getResult = optionsUniversity_dict.get(optionUser, None) # Opção digitada é usada com o método get.

            if optionUser == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo da área acadêmica...\033[m\n')
                return

            if getResult is None:
                time.sleep(0.3)
                print(messageError)
                continue

            else:
                prompt = f'{text_format["highlighted"]}{text_collor["gray"]}-\033[m' * 45
                space()
                print(prompt)
                getResult()
            
            while True: # Continuar ou parar.
                    space()
                    another_academy_consultation = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR NA ÁREA ACDÊMICA? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_academy_consultation not in valid_response:
                        time.sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_academy_consultation == '1':
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
        


# DICIONÁRIO DE OPÇÕES DO SUBMENU DE EMPRÉSTIMO DE LIVROS.       
loan_books_options_dict = {
    '1': 'REGISTRAR EMPRÉSTIMO DE LIVRO', # book_loan
    '2': 'EXIBIR LIVROS EMPRESTADOS EM TABELA',  # display_book_loan_plt
    '3': 'DELETAR REGISTRO DE EMPRÉSTIMO DE LIVRO', # dell_book_loan
    '4': 'ATUALIZAR DADOS DO EMPRÉSTIMO DE LIVRO', # update_book_loan
    '5': 'ATUALIZAR ISBN DE LIVRO', # update_isbn
    '6': 'TOTAL DE LIVROS EMPRESTADOS', # total_books_loan
    }

get_Functions_loan_books = {
    '1': book_loan, # REGISTRAR EMPRÉSTIMO DE LIVRO
    '2': display_book_loan_plt,  # EXIBIR LIVROS EMPRESTADOS EM TABELA
    '3': dell_book_loan, # DELETAR REGISTRO DE EMPRÉSTIMO DE LIVRO
    '4': update_book_loan, # ATUALIZAR DADOS DO EMPRÉSTIMO DE LIVRO
    '5': update_isbn, # ATUALIZAR ISBN DE LIVRO
    '6': total_books_loan, # TOTAL DE LIVROS EMPRESTADOS
    }


# CRUD PARA EMPRÉSTIMO DE LIVROS.
def dispaly_dictOptionsLoanBooks():
    for i, options in loan_books_options_dict.items():
        print(f'{text_format["highlighted"]}{background_collors["gray"]} {i} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{options}.\033[m')
        time.sleep(0.2)
    space()


# CAPTURAR OPÇÃO DO USUÁRIO E EXECUTAR AUTOMATICAMENTE.
def get_function_loan_books():
    while True:
        try:
            space()

            dispaly_dictOptionsLoanBooks()
            space()

            messageError = f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n'
            optionUser = str(input(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO DE EMPRÉSTIMO DE LIVROS (0: Sair / 1-{len(loan_books_options_dict)}):\033[m '))
            getResult = get_Functions_loan_books.get(optionUser, None) # Opção digitada é usada com o método get.

            if optionUser == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo da área de empréstimos...\033[m\n')
                return  
            
            if getResult is not None:
                space()
                time.sleep(0.2)
                getResult()  # Chama a função correspondente à opção escolhida.
                
            else:
                space()
                time.sleep(0.2)
                print(messageError)
                continue

            while True: # Continuar ou parar.
                    space()
                    another_loan_consultation = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR EM ABA DE EMPÉSTIMOS? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_loan_consultation not in valid_response:
                        time.sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_loan_consultation == '1':
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


# DICIONÁRIO DE OPÇÕES DO SUBMENU DE EMPRÉSTIMO DE OUTROS ITENS.
optionsSubmenu_other_loans_dict = {
    '1': 'REGISTRAR EMPRÉSTIMO DE UM ITEM', # other_loan
    '2': 'EXIBIR ITENS EMPRESTADOS EM TABELA', # display_other_loan
    '3': 'DELETAR REGISTRO DE EMPRÉSTIMO DE ITEM' # dell_other_loan
}  

# EXIBIR DICIONÁRIO DE OPÇÕES DO SUBMENU DE EMPRÉSTIMO DE OUTROS ITENS.
def display_options_other_loan():
    for i, options in optionsSubmenu_other_loans_dict.items():
        print(f'{text_format["highlighted"]}{background_collors["gray"]} {i} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{options}.\033[m')
        time.sleep(0.2)
    space()

functions_other_loan = {
    '1': other_loan, # REGISTRAR EMPRÉSTIMO DE UM ITEM
    '2': display_other_loan, # EXIBIR ITENS EMPRESTADOS EM TABELA
    '3': dell_other_loan, # DELETAR REGISTRO DE EMPRÉSTIMO DE LIV
    }


# LÓGICA PARA CAPTURAR OPÇÃO DO USUÁRIO E EXECUTAR AUTOMATICAMENTE.
def get_function_other_loan():
    while True:
        try:
            space()

            display_options_other_loan()
            space()

            messageError = f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n'
            optionUser = str(input(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO DE EMPRÉSTIMO DE OUTROS ITENS (0: Sair / 1-{len(optionsSubmenu_other_loans_dict)}):\033[m '))
            getResult = functions_other_loan.get(optionUser, None) # Opção digitada é usada com o método get.

            if optionUser == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo da área de empréstimos...\033[m\n')
                return  
            
            if getResult is not None:
                space()
                time.sleep(0.2)
                getResult()  # Chama a função correspondente à opção escolhida.
                
            else:
                space()
                time.sleep(0.2)
                print(messageError)
                continue

            while True: # Continuar ou parar.
                    space()
                    another_loan_consultation = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR EM ABA DE EMPÉSTIMOS? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_loan_consultation not in valid_response:
                        time.sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_loan_consultation == '1':
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
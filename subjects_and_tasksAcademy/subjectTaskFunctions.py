from allFunctions.user_data_var import (
    range_subjects_semester, vector_subjects_name, valid_range_grades_per_activities,
    user_data_dictionary, valid_total_tasks_subject, student_grades, dict_book_loan, 
    min_title, max_title, ISBN10, ISBN13, AUTHOR, BOOKNAME, ISBNID, BOOKSUBJECT, LOANDATE, DELIVERYDATE, QUANTITYBOOKS, QUANTITYOTHER,
    min_subject, max_subject, min_author, max_author, otherGeneric_loan, min_name_loan, max_name_loan, min_quantity_books, 
    max_quantity_books, LOANNAME, PORPUSELOAN, min_purpose, max_purpose, minId_loan, maxId_loan, min_quantity_other, max_quantity_other
    )

from anscii_sistem.collors import text_collor, text_format, background_collors
from emojizeSistem.dict_emojize import utility_symbols2, utility_symbols1, academyEmojis, financeEmojis, emojisAcademy2, workEmojis, techEmojis
from utils.utilsUx import ej
from time import sleep
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from allFunctions.insertionTypes import space, insertion_void, insertion_int, insertion_float
from allFunctions.data_user_functions import insertion_name
from utilsCrud.crudCreate import validation_date
from utilsCrud.crudDataUser import check_required_params



# QUANTIDADE DE MATÉRIAS POR SEMESTRE. MÉDIA DE 4 A 10.
def quantity_subjects_semester(sj: str):
    while True:
        try:

            # USANDO VETOR PARA VERIFICAR SE O USUÁRIO FICOU FORA DA QUANTIDADE COMUM.
            subjects = insertion_int(sj)
            valid_range_subjects = range_subjects_semester
            if subjects not in valid_range_subjects:
                sleep(0.3)
                space()
                print(f'{ej(utility_symbols2['erro'])} Quantidade de matérias inválida. '
                      f'Média entre {min(range_subjects_semester)} e {max(range_subjects_semester)}\033[m\n')
                continue

            else:
                return subjects
        except ValueError:
            print(f'{text_format['highlighted']}Quantidade inválida.\033[m\n')
            continue


# FUNÇÃO PARA PARAMETRIZAR NOME DE MATÉRIAS.
def insertion_subject_name(sn: str):
    while True:
        try:
            min_name = 5
            max_name = 30
            name_subject = input(sn).strip().lower()
            if len(name_subject) < min_name or len(name_subject) > max_name:
                space()
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])}Erro, '
                      f'matéria deve conter entre {min_name} e {max_name} caracteres. \033[m\n')
                continue

            elif not name_subject.replace(' ', '').replace('-', '').replace(':', '').replace('.', '').isalpha():
                space()
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])} Erro, '
                      f'digite apenas letras. \033[m\n')
            else:
                return name_subject

        except ValueError:
            continue


# FUNÇÃO PARA NOMEAR AS MATÉRIAS.
def name_subjects_semester():
    while True:
        try:
            # TOTAL INFORMADO PELO USUÁRIO.
            quantity_subjects = user_data_dictionary.get('quantidade de matérias', None)

            if quantity_subjects is None:
                sleep(0.3)
                space()
                print(f'{ej(utility_symbols2['erro'])}- Erro, quantidade de matérias não informada.\033[m\n')
                return 

            if vector_subjects_name:
                vector_subjects_name.clear()

            # ATRIBUIÇÃO DE CADA MATÉRIA NO VETOR.
            for i in range(1, quantity_subjects +1):
                name_sj = insertion_subject_name(f'{text_format['invert']}{text_collor['yellow']} NOME DA MATÉRIA {i}:\033[m ')
                space()
                vector_subjects_name.append(name_sj)

            # ATRIBUIÇÃO DE CADA MATÉRIA NO DICIONÁRIO.
            for k, value in enumerate(vector_subjects_name, start=1):
                user_data_dictionary[f'matéria {k}'] = value # MATÉRIA + {K} = NÚMERO 1 AO VETOR = quantity_subjects.
            break

        except Exception as e:
            print(f'{ej(utility_symbols2['erro'])} {text_collor['red']} Erro inesperado.\033[m')
            return None


# FUNÇÃO PARA VALIDAR A QUANTIDADE DE TAREFAS/ATIVIDADES POR MATÉRIA. MÉDIA DE 3 A 5.
def validation_quantity_tasks_subject(ts: str):
    while True:
        try:

            # USANDO VETOR PARA VERIFICAR SE O USUÁRIO FICOU FORA DA QUANTIDADE COMUM.
            subjects = insertion_int(ts)
            valid_range_tasks_subject = valid_total_tasks_subject
            if subjects not in valid_range_tasks_subject:
                sleep(0.3)
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Quantidade inválida. '
                      f'Média entre {min(valid_total_tasks_subject)} e {max(valid_total_tasks_subject)}\033[m\n')
                continue

            else:
                return subjects
        except ValueError:
            print(f'{ej(utility_symbols2["erro"])}{text_format["highlighted"]}Quantidade inválida.\033[m\n')
            continue


# FUNÇÃO PARA INSERIR QUANTIDADE DE TAREFAS POR MATÉRIA, USANDO 'validation_quantity_tasks_subject'. 
def quantity_tasks_per_subject():
    while True:
        try:

            # PRECISAMOS DO VETOR PARA EXIBIR AS MATÉRIAS DO ALUNO.
            if vector_subjects_name is None:
                print(f'{text_format['highlighted']} VETOR VAZIO\033[m')
                return None
            
            else:
                print(f'{background_collors["green"]} {ej(utility_symbols2["sucesso"])}  SUAS MATÉRIAS CADASTRADAS SÃO:\033[m\n')
                for i, k in enumerate(vector_subjects_name, start=1):
                    print(f'{text_format["highlighted"]}Matéria {i}: {k.capitalize()}\033[m')
                    
            space()
            # INSERÇÃO = student_grades[f'atividades matéria {index} IGUAL A 1 - A TUDO QUE CONTÉM NO VETOR'] -> FUNÇÃO = 3 A 5.
            # MATÉRIA = [INDEX DO VETOR] + QUANTIDADE VÁLIDA.
            for index, task in enumerate(vector_subjects_name, start=1):
                student_grades[f'quantidade de atividades matéria {task}'] = validation_quantity_tasks_subject(f'{text_format["invert"]}{text_collor["yellow"]} QUANTIDADE DE ATIVIDADES/PROVAS EM -> {task.capitalize()}:\033[m ')
                space()

            break    
        except ValueError:
            print(f'{text_format["highlighted"]}Quantidade inválida.\033[m\n')
            continue



# VALIDARÇÃO DAS NOTAS DAS ATIVIDADES.
# PADRÃO DE 0.0 A 10.0. '00.11' SERÁ NOTA PENDENTE.
def validation_grades_activitys(g: str):
    while True:

        print(f'{text_collor["green"]}INSERÇÃO DE NOTAS: 0 ATÉ 10 - DIGITE "00.11" PARA NOTAS PENDENTES.\033[m\n')

        try:
            valid_grade = valid_range_grades_per_activities
            grade = insertion_float(g)
            if grade < min(valid_grade) or grade > max(valid_grade):
                sleep(0.3)
                space()
                print(f'{ej(utility_symbols2["erro"])} {text_collor["red"]} Nota inválida. '
                    f'Deve ser entre {min(valid_grade)} e {max(valid_grade)}.\033[m\n')
                continue
            else:
                if grade == 00.11:
                    space()
                    print(f'{text_collor["yellow"]}{ej(utility_symbols2["alerta"])}  Nota pendente salva.\033[m\n')
                    return float(f'{grade:.2f}')
                else:
                    space()
                    print(f'{text_collor["green"]}{ej(utility_symbols2["sucesso"])}  Nota salva.\033[m\n')
                    return float(f'{grade:.2f}')
        except ValueError:
            print(f'{ej(utility_symbols2["erro"])} {text_format["highlighted"]} Nota inválida.\033[m\n')
            continue
        

# ATRIBUIR NOTAS EM CADA MATÉRIA E ATIVIDADE DA MATÉRIA.
# NOTAS DAS MATÉRIAS SÃO GUARDADAS NO DICIONÁRIO 'student_grades'
def grades_by_activities():
    while True:
        try:

            # TOTAL INFORMADO PELO USUÁRIO.
            quantity_subjects = user_data_dictionary.get('quantidade de matérias', None)

            if quantity_subjects is None:
                sleep(0.3)
                space()
                print(f'{ej(utility_symbols2['erro'])}- Erro, quantidade de matérias não informada.\033[m\n')
                return None

            # ATRIBUIÇÃO DE CADA NOTA NO DICIONÁRIO.
            for j in range(1, quantity_subjects + 1):
                total_activities = student_grades.get(f'quantidade de atividades matéria {vector_subjects_name[j-1]}', None)
                if total_activities is None:
                    sleep(0.3)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Erro, quantidade de atividades não informada para a matéria {vector_subjects_name[j-1]}.\033[m\n')
                    return None

                for k in range(1, total_activities + 1):
                    space()
                    grade_activity = validation_grades_activitys(f'{text_format["invert"]}{text_collor["yellow"]} NOTA DA ATIVIDADE {k} DA MATÉRIA {vector_subjects_name[j-1].capitalize()}:\033[m ')
                    space()
                    student_grades[f'nota atividade {k} matéria {vector_subjects_name[j-1]}'] = grade_activity  # NOTA ATIVIDADE + {K} MATÉRIA + {J}.

            space()
            break

        except Exception as e:
            space()
            print(f'{ej(utility_symbols2['erro'])} {text_collor['red']} Erro inesperado.\033[m')
            return None


# EXIBIR MATÉRIAS DO ALUNO NO SEMESTRE.
def display_materials():
    print(f'{text_format["highlighted"]}{text_collor["green"]} °SUAS MATÉRIAS SÃO:\033[m\n')

    if not vector_subjects_name:
        space()
        sleep(0.3)
        print('Matérias não informadas ainda.\n')
        return None
    
    for i, materials in enumerate(vector_subjects_name, start=1):
        sleep(0.3)
        print(f'{text_format["highlighted"]}Matéria {i}: {materials.capitalize()}\033[m')


# EXIBIR QUANTIDADE DE ATIVIDADES POR MATÉRIA.
def display_quantity_of_activities_per_matter():
    print(f'{text_collor["green"]}{ej(utility_symbols1["ponto_caixa"])} QUANTIDADE DE ATIVIDADES POR MATÉRIA {ej(utility_symbols1["ponto_caixa"])}\033[m\n')

    if not vector_subjects_name:
        space()
        sleep(0.3)
        print(f'{text_format["highlighted"]}Matérias não informadas ainda.\033[m\n')
        return None
    
    for m in vector_subjects_name:
        total_activities = student_grades.get(f'quantidade de atividades matéria {m}', None)
        print(f'{text_format["highlighted"]}Matéria: {m.capitalize()} - Total de atividades: {total_activities}\033[m')



# EXIBIR TOTAL DE ATIVIDADES NO SEMESTRE. 
def total_activities_semester():
    try:

        sumActivities = 0 # soma total de atividades.

        if not vector_subjects_name:
            space()
            sleep(0.3)
            print(f'{text_format["highlighted"]}Matérias não informadas ainda.\033[m\n')
            return None
        
        # PARA CADA ITERAÇÃO QUE RECBE AS ATIVIDADES DE UMA MATÉRIA, sumActivities RECEBE O VALOR DE total_act.
        for sum in vector_subjects_name:
            total_act = student_grades.get(f'quantidade de atividades matéria {sum}', None)
            if isinstance(total_act, (int, float)):
                sumActivities += total_act
            else:
            # BREAK SE A QUANTIDADE DE MATÉRIAS POR UNIDADE NÃO FOI INFORMADA.
                space()
                print(f'{text_collor["red"]}AVISO: Quantidade de atividades não informada para a matéria {sum}.\033[m\n')
                return None
        print(f'{text_format["highlighted"]}{text_collor["blue"]}TOTAL DE ATIVIDADES NO SEMESTRE  {ej(academyEmojis["livro"])}\033[m\n')
        print(f'{text_format["highlighted"]}Você possui \033[31m{sumActivities}\033[m atividades/provas para o {user_data_dictionary["semestre atual"]}° semestre.\033[m\n')

    except TypeError:
        print(f'{text_format["highlighted"]}Quantidades de matérias não informada integralmente.\033[m\n')
        return None


# MATÉRIA COM MAIS ATIVIDADES.
def ranking_quantity_activities_per_materials():

    if not vector_subjects_name:
        space()
        sleep(0.3)
        print(f'{text_format["highlighted"]}Matérias não informadas ainda.\033[m\n')
        return None
    
    print(f'{text_format["highlighted"]}MAIOR NÚMERO DE ATIVIDADES EM UMA MATÉRIA.\n')

    all_activities = {}
    for mat in vector_subjects_name:
        activities = student_grades.get(f'quantidade de atividades matéria {mat}', None)
        if activities is None:
            space()
            print(f'{text_collor["red"]}AVISO: Quantidade de atividades não informada para a matéria {mat}.\033[m\n')
            return None
        else:
            all_activities[f'{mat}'] = activities
    ranking = max(all_activities, key=all_activities.get)
    print(f'{text_collor["yellow"]}{ej(utility_symbols1["alerta"])}  ATENÇÃO: se você tiver duas matérias com o mesmo número de atividades, apenas uma será exibida!\033[m\n')
    print(f'{text_format["highlighted"]}-> Matéria com com maior número de atividades: {text_collor["green"]}{ranking}.\033[m')
    print(f'{text_format["highlighted"]}-> Número de atividades da matéria {ranking}: {text_collor["green"]}{all_activities[ranking]}\033[m')


# MAIOR NOTA NAS ATIVIDADES. TRAZ A MATÉRIA REFERENTE A NOTA.
def max_grade_activities():
    if not vector_subjects_name:
        space()
        sleep(0.3)
        print(f'{text_format["highlighted"]}Matérias não informadas ainda.\033[m\n')
        return None
    # lista de notas
    list_max_grade = []
    for v in vector_subjects_name:
        activities = student_grades.get(f'quantidade de atividades matéria {v}', None)
        if activities is None:
            space()
            print(f'{text_collor["red"]}AVISO: Quantidade de atividades não informada para a matéria {v}.\033[m\n')
            return None
        
        # Percorre as notas segundo o número de atividades.
        for i in range(1,activities+1):
            key_grade = f'nota atividade {i} matéria {v}'
            grade = student_grades.get(key_grade)
            if grade is not None and grade != 00.11:
                try:
                    # tupla para valor e matéria.
                    list_max_grade.append((grade, v))
                except ValueError:
                    print(f'{text_collor["red"]}Erro, nota inválida {key_grade} para {grade}\033[m\n')
                    continue
 
    found_max_grade = max(list_max_grade, key=lambda item: item[0])
    max_grade = found_max_grade[0]
    subject_max_grade = found_max_grade[1]
    if not found_max_grade:
        print(f'{text_collor["red"]}Não há notas válidas para exibir a maior nota.\033[m\n')
    else:
        print(f'{text_format["highlighted"]}{text_collor["green"]}-> Maior nota atividade {subject_max_grade} = {max_grade}\033[m\n')


# EXIBIR TODAS AS NOTAS DETALHADAS POR MATÉRIA.
def display_all_grades_detailed():
    print(f'{background_collors["blue"]}{text_format["highlighted"]} {ej(academyEmojis["anotacao"])} '
          f'DETALHAMENTO DE NOTAS POR MATÉRIA {text_format["none"]}\n')

    if not vector_subjects_name:
        space()
        print(f'{text_format["highlighted"]}{text_collor["red"]}Matérias não informadas ainda.\033[m\n')
        return None

    for subject in vector_subjects_name:
        # Busca a quantidade de atividades que você cadastrou para esta matéria
        total_activities = student_grades.get(f'quantidade de atividades matéria {subject}', 0)
        
        print(f'{text_format["highlighted"]}{text_collor["yellow"]}MATÉRIA: {subject.upper()}\033[m')
        print(f'{text_collor["light_blue"]}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')

        if total_activities == 0:
            print(f'{text_collor["gray"]}   Sem atividades registradas.\033[m')
        else:
            for k in range(1, total_activities + 1):
                # Busca a nota específica da atividade k da matéria atual
                grade = student_grades.get(f'nota atividade {k} matéria {subject}', "N/A")
                
                # Tratamento visual para notas pendentes (00.11)
                if grade == 00.11:
                    status_grade = f'{text_collor["red"]}PENDENTE (00.11)\033[m'
                else:
                    status_grade = f'{text_collor["green"]}{grade}\033[m'

                print(f'   {ej(utility_symbols1["ponto_caixa"])} Atividade {k}: {status_grade}')
        space()
        sleep(0.2)


# Nome do livro.
def valid_title():
    while True:
        try:
            min = min_title
            max = max_title
            title = input(f'{text_format['highlighted']}{ej(emojisAcademy2['livros'])}  NOME DO LIVRO:\033[m ').strip().lower()

            if len(title) < min or len(title) > max:
                space()
                print(f'{ej(utility_symbols1['erro'])}  Tamanho inválido, mínimo: {min}, máximo: {max} caracteres.\n')
                continue

            return title
        
        except ValueError:
            print(f'{ej(utility_symbols1['erro'])} Erro, digite apenas letras.\n')



# ISBN válido.
def valid_isbn():
    while True:
        try:
            # Tamanho válido.
            i10 = ISBN10
            i13 = ISBN13
            isbn = insertion_void(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  NÚMERO ISBN:\033[m ').strip()

            if not isbn.isdigit():
                space()
                print(f'{ej(utility_symbols1['erro'])} Erro, insira apenas dígitos.\n')
                continue

            if len(isbn) != i10 and len(isbn) != i13:
                space()
                print(f'{ej(utility_symbols1['erro'])} Erro, ISBN deve ter {i10} ou {i13} dígitos.\n')
                continue

            return isbn

        except ValueError:
            print(f'{ej(utility_symbols1['erro'])} Erro, insira apenas dígitos/números.\n')



# Assunto do livro.
def valid_subject_book():
    while True:
        try:
            min = min_subject
            max = max_subject
            subject = insertion_void(f'{text_format['highlighted']}{ej(emojisAcademy2['pergaminho'])}  ASSUNTO DO LIVRO:\033[m ')

            if len(subject) < min or len(subject) > max:
                space()
                print(f'{ej(utility_symbols1['erro'])} Assunto deve conter entre {min} e {max} caracteres.\n')
                continue
            if not subject.replace(' ', '').replace('-', '').replace(':', '').replace('.', '').isalpha:
                space()
                print(f'{ej(utility_symbols1['erro'])} Digite apenas letras.\n')
                continue

            return subject
        
        except ValueError:
            space()
            print(f'{ej(utility_symbols1['erro'])} Digite apenas letras.\n')
            


# Validar nome do autor.
def valid_author(prompt: str):
    while True:
        try:
            min = min_author
            max = max_author 

            author = input(prompt).strip().lower()

            if not author.replace(' ', '').replace('-', '').replace(':', '').replace('.', '').isalpha(): 
                space()
                print(f'{ej(utility_symbols2['erro'])}  Digite apenas letras.\n')
                continue

            elif len(author) < min or len(author) > max:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Nome deve conter entre {min} e {max} caracteres.\n')
                continue

            return author

        except ValueError:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Digite apenas letras.\n')



# Qauntidade de livros.
def valid_quantity_books():
    while True:
        try:
            min = min_quantity_books
            max = max_quantity_books

            quantity = insertion_int(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  QUANTIDADE:\033[m ')

            if quantity < min or quantity > max:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Quantidade deve estar entre {min} e {max} livros.\n')
                continue

            return quantity
        
        except ValueError:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Digite apenas números.\n')



# EMPRÉSTIMO DE LIVROS.
def book_loan():
    while True:
        try:
            university_user = user_data_dictionary.get('universidade', None)

            print(f'{text_format['highlighted']}{text_collor['white']}{ej(emojisAcademy2["caderno"])} {ej(utility_symbols1['linha_vertical'])} '
                f'REGISTRE EMPRÉSTIMO DE LIVROS - {university_user} {ej(utility_symbols1['linha_vertical'])}{text_format['none']}\n')
            
            # Entrada de dados.
            book_name = valid_title()
            author_name = valid_author(f'{text_format['highlighted']}{ej(utility_symbols2['usuario'])}  NOME DO AUTOR:\033[m ')

            # Verificação: ISBN repetido.
            while True:
                size_isbn = valid_isbn()
                if size_isbn in dict_book_loan:
                    sleep(0.2)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} ISBN já existente.\033[m\n')
                    continue
                
                else:
                    break


            subject = valid_subject_book()
            quantity_book = valid_quantity_books()

            while True: #Datas compatíveis com prazos lógicos.
                loan_date = validation_date(f'{text_format['highlighted']}{ej(workEmojis["calendario"])}  DATA DE EMPRÉSTIMO:\033[m ')
                delivery_date = validation_date(f'{text_format['highlighted']}{ej(workEmojis["calendario"])}  PREVISÃO DE ENTREGA:\033[m ')

                if datetime.strptime(loan_date, '%d/%m/%Y') > datetime.strptime(delivery_date, '%d/%m/%Y'):
                    space()
                    sleep(0.2)
                    print(f'{ej(utility_symbols2['erro'])}  Data de entrega não deve ser menor que a de empréstimo.\n')
                    continue
        
                break

            # Atribuição de dados.
            dict_book_loan[size_isbn] = {
                BOOKNAME: book_name, 
                AUTHOR: author_name, 
                BOOKSUBJECT: subject,
                LOANDATE: loan_date,
                DELIVERYDATE: delivery_date,
                QUANTITYBOOKS: quantity_book
                }

            while True: # Continuar ou parar.
                space()
                another_loan = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA REGISTRAR OUTRO EMPRÉSTIMO? (1: SIM - 0: NÃO):\033[m ').strip()
                valid_response = ['1', '0']
                if another_loan not in valid_response:
                    sleep(0.3)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                    continue

                elif another_loan == '1':
                    space()
                    break

                else:
                    space()
                    sleep(0.3)
                    print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                    return  
                
        except Exception as e:
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')



# Exibir um item do dicionário.
def display_book_details_loan(isbn):
    try:

        details = dict_book_loan[isbn]

        
        space()
        print(f"{text_format['highlighted']}ISBN: {isbn}\033[m")
        print(f"Titulo = {details[BOOKNAME]}")
        print(f"Autor = {details[AUTHOR]}")
        print(f"Assunto = {details[BOOKSUBJECT]}")
        print(f"Empréstimo = {details[LOANDATE]}")
        print(f"Devolução = {details[DELIVERYDATE]}")
        print(f"Quantidade = {details[QUANTITYBOOKS]}")
        space()
        return

    except KeyError:
        space()
        print(f"{ej(utility_symbols2['erro'])}  ISBN não encontrado.\n")
        return


# Exibir todos livros.
def display_all_books():
    try:
        if not dict_book_loan or dict_book_loan is None:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Nenhum livro registrado ainda.\n')
            return
            
        else:
            for isbn, detail in dict_book_loan.items():
                print(f'{ej(workEmojis['numeros'])}  {text_format['highlighted']}{text_collor['white']}ISBN: {isbn}\033[m\n'
                          f'{ej(emojisAcademy2['livro'])}  Titulo = {detail[BOOKNAME]}\n'
                          f'{ej(utility_symbols1['usuario'])}  Autor = {detail[AUTHOR]}\n'
                          f'{ej(emojisAcademy2['diario'])}  Assunto = {detail[BOOKSUBJECT]}\n'
                          f'{ej(workEmojis['calendario'])}  Data de Empréstimo = {detail[LOANDATE]}\n'
                          f'{ej(workEmojis['calendario'])}  Data de Devolução = {detail[DELIVERYDATE]}\n'
                          f'{ej(workEmojis['numeros'])}  Quantidade = {detail[QUANTITYBOOKS]}\n')
            space()

    except Exception as a:
            space()
            print(f'{ej(utility_symbols2['erro'])} Erro: {a}')
            return


# Deletar livros.
def dell_book_loan():

    while True:
        try:
            if not dict_book_loan or dict_book_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Nenhum livro registrado ainda.\n')
                return
            
            # layout
            print(f'{text_format['highlighted']}{text_collor['white']}{text_format['underline']}{ej(workEmojis['marcador'])}  DELETE LIVROS DO SEU REGISTRO DE EMPRÉSTIMOS.\033[m\n'
                  f'         {text_format['highlighted']}{text_collor['gray']}Digite 0 (10x) para sair).\033[m\n')
            # Exibir isbn e nome.
            for isbn, book in dict_book_loan.items():
                print(f'{text_format['highlighted']}{text_collor['white']}ISBN: {isbn}:\033[m {text_format['highlighted']}{text_collor['green']}{book[BOOKNAME]}\033[m')
            space()

            identification = valid_isbn()
            if identification == '0000000000':
                space()
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                return

            if dict_book_loan.get(identification, None) is None:
                space()
                print(f'ISBN inválido. Tente novamente.\n')
                continue

            else:
                dict_book_loan.pop(identification)
                space()
                print(f'{ej(utility_symbols1['sucesso'])}  Livro deletado dos registros.\n')

            # Verificação, para não imprimir mensagem abaixo em vão.
            if not dict_book_loan or dict_book_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Registro de livros vazio.\n')
                return
            
            else:
                while True: # Continuar ou parar.
                    space()
                    another_loan = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA DELETAR OUTRO LIVRO? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_loan not in valid_response:
                        sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_loan == '1':
                        space()
                        break

                    else:
                        space()
                        sleep(0.3)
                        print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                        return  
                    
        except Exception as e:
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')




# Atualizar livros registrados.
def update_book_loan():
    while True:
        try:
            if not dict_book_loan or dict_book_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Nenhum livro registrado ainda.\n')
                return
            
            print(f'{text_format['highlighted']}{background_collors['green']}{ej(techEmojis['teclado'])}  ATUALIZE SEU REGISTRO DE LIVROS {ej(emojisAcademy2['caneta'])}  \033[m\n'
                  f'\n  {text_format['highlighted']}{text_collor['white']}{ej(workEmojis['numeros'])}  Digite o ISBN do livro.\033[m\n')
            
            
            for isbn, book in dict_book_loan.items():
                print(f'{text_format['highlighted']}{text_collor['white']}ISBN: {isbn}:\033[m {text_format['highlighted']}{text_collor['green']}{book[BOOKNAME]}\033[m')
            space()

            identification = valid_isbn()

            if dict_book_loan.get(identification, None) is None:
                space()
                print(f'ISBN inválido. Tente novamente.\n')
                continue

            #BOOKNAME: book_name, 
                #AUTHOR: author_name, 
                #BOOKSUBJECT: subject,
                #LOANDATE: loan_date,
                #DELIVERYDATE: delivery_date,
                #QUANTITYBOOKS: quantity_book

            
            while True:
                # Campos.
                items_update = {
                    '1': BOOKNAME, '2': AUTHOR, '3': BOOKSUBJECT, 
                    '4': LOANDATE, '5': DELIVERYDATE, '6': QUANTITYBOOKS
                    }
                
                # Obter função de cada campo.
                get_function = {
                    BOOKNAME: valid_title, AUTHOR: valid_author,
                    BOOKSUBJECT: valid_subject_book, LOANDATE: validation_date, 
                    DELIVERYDATE: validation_date, QUANTITYBOOKS: valid_quantity_books
                    }
                
                space()
                for number, item in items_update.items():
                    sleep(0.15)
                    print(f'{number}: {item}')
                
                space()
                ItemUpdate = insertion_void(f'{text_format['highlighted']}QUAL ITEM DE "{dict_book_loan[identification][BOOKNAME].upper()}" DESEJA ATUALIZAR:\033[m ')
                get_update = items_update.get(ItemUpdate, None)

                
                if get_update is None:
                    space()
                    print(f'{ej(utility_symbols2['erro'])}  Campo inválido.\n')
                    continue

                get_params = check_required_params(get_function[get_update])

            

                if get_params == 0:
                    space()
                    dict_book_loan[identification][get_update] = get_function[get_update]()
                elif get_params == 1:
                    while True:
                        # Caso especial. Datas.
                        prompt = f"{text_format['highlighted']} ATUALIZAR {get_update}:\033[m "
                        new_value = get_function[get_update](prompt)

                        # 2. Se for uma DATA, validamos a lógica antes de salvar
                        if get_update in [LOANDATE, DELIVERYDATE]:
                            # Pegamos a data que JÁ ESTÁ lá para comparar com a NOVA
                            if get_update == LOANDATE:
                                str_loan = new_value
                                str_delivery = dict_book_loan[identification][DELIVERYDATE]
                            else:
                                str_loan = dict_book_loan[identification][LOANDATE]
                                str_delivery = new_value

                            # Transformamos em objetos para o "IF" funcionar
                            obj_loan = datetime.strptime(str_loan, '%d/%m/%Y')
                            obj_delivery = datetime.strptime(str_delivery, '%d/%m/%Y')

                            if obj_loan > obj_delivery:
                                space()
                                print(f"{ej(utility_symbols2['erro'])} Data inválida! Data de empréstimo: {str_loan} é maior que data de devolução: {str_delivery}.\n")
                                continue # Volta e pede a data de novo
                            break
                        
                        dict_book_loan[identification][get_update] = new_value

                        # Exibir resultados.
                        

                        break # Sai do loop da data
                break

            # Exibir resultados.
            space()
            print(f'{text_format['highlighted']}{text_collor['green']}{ej(utility_symbols1['sucesso'])}  DADOS ATUALIZADOS.\033[m\n'
                  f'\n{text_format['highlighted']}{text_collor['white']}ISBN = {identification}\033[m')
            for key, value in dict_book_loan[identification].items():
                
                key_fmt = f"{text_format['highlighted']}{text_collor['white']}{key.capitalize()}\033[m"
                
                
                if isinstance(value, str):
                    
                    value_fmt = f"{text_format['highlighted']}{value.capitalize()}\033[m"
                else:
                    
                    value_fmt = f"{text_format['highlighted']}{value}\033[m"
                
                print(f"{key_fmt} = {value_fmt}")


            # Outra atualização.
            while True:
                space()
                another_update = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA ATUALIZAR OUTRO LIVRO? (1: SIM - 0: NÃO):\033[m ').strip()
                valid_response = ['1', '0']

                if another_update not in valid_response:
                    sleep(0.3) 
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                    continue

                elif another_update == '1':
                    space()
                    break

                else:
                    space()
                    sleep(0.3)
                    print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                    return       
                        

        except Exception as e:
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')




# ATUALIZAR ISBN.
def update_isbn():
    while True:
        try:

            if not dict_book_loan or dict_book_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Nenhum registro criado ainda.\n')
                return
            
            print(f'{text_format['highlighted']}{background_collors['gray']}{text_collor['blue']}{ej(emojisAcademy2['caneta'])} {ej(emojisAcademy2['documentos'])}  ATUALIZAÇÃO DE ISBN. \033[m\n')

            for isbn, book in dict_book_loan.items():
                print(f'{text_format['highlighted']}{text_collor['white']}ISBN: {isbn}:\033[m {text_format['highlighted']}{text_collor['green']}{book[BOOKNAME]}\033[m')
            space()

            old_isbn = input(f'{text_format['highlighted']}DIGITE ISBN QUE QUER ATUALIZAR (0: SAIR):\033[m ').strip()

            if old_isbn == '0':
                space()
                print(f'{ej(utility_symbols2['seta_retorno'])}  Saindo.\n')
                return
            
            if old_isbn not in dict_book_loan:
                space()
                print(f'{ej(utility_symbols2['erro'])}  ISBN inexistente.\n')
                continue
            space()

            # Pegamos a isbn e seus valores.
            get_key = old_isbn
            details = dict_book_loan[get_key]

            # Verificar se a chave nova já existe.
            while True:
                print(f'Digite novo valor para: \033[32m{get_key}:\033[m:\n')
                new_isbn = valid_isbn()
                if new_isbn in dict_book_loan:
                    space()
                    print(f'{ej(utility_symbols2['erro'])}  ISBN já existe.\n')
                    continue
                else:
                    del dict_book_loan[get_key]
                    dict_book_loan[new_isbn] = details
                    space()
                    print(f'{text_collor['green']}{ej(utility_symbols1['sucesso'])}  Dados atualizados!\033[m\n')

                    # Exibir atualização,
                    display_book_details_loan(new_isbn)


                    break # Finalizar atualização.

            while True:
                space()
                update_new_isbn = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA ATUALIZAR OUTRO ISBN? (1: SIM - 0: NÃO):\033[m ').strip()
                valid_response = ['1', '0']

                if update_new_isbn not in valid_response:
                    sleep(0.3) 
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                    continue

                elif update_new_isbn == '1':
                    space()
                    break

                else:
                    space()
                    sleep(0.3)
                    print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                    return 

        except KeyError:
            space()
            print(f'{ej(utility_symbols2['erro'])}  ISBN inexistente.\n')



# Qauntidade de livros emprestados.
def total_books_loan():
    try:
        if not dict_book_loan or dict_book_loan is None:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Nenhum livro registrado ainda.\n')
            return
        
        total_books = 0

        for details in dict_book_loan.values():
            quantity = details[QUANTITYBOOKS]
            total_books += quantity

        space()
        print(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  TOTAL DE UNIDADES DE LIVROS: {total_books}')
        
    except KeyError:
        space()
        print(f'{ej(utility_symbols2['erro'])}  Erro de chave.\n')



# EXIBIR LIVROS EMPRESTADOS.
def display_book_loan_plt():
    try:
        if not dict_book_loan or dict_book_loan is None:
            space()
            sleep(0.2)
            print(f'{ej(utility_symbols1['erro'])} Sem registro de empréstimo de livros.\n')
            return
        
        else:
            space()
            df = pd.DataFrame.from_dict(dict_book_loan, orient='index').reset_index()
    
            # Renomeamos as colunas usando suas constantes para ficar bonito no gráfico
            df.columns = ['ISBN', BOOKNAME, AUTHOR, BOOKSUBJECT, LOANDATE, DELIVERYDATE, QUANTITYBOOKS]

            # 2. Configura a Janela do Gráfico (sem eixos, pois queremos apenas a tabela)
            fig, ax = plt.subplots(figsize=(12, 4)) 
            ax.axis('tight')
            ax.axis('off')

            # 3. Cria a Tabela Visual
            # loc='center' garante que a tabela fique no meio da imagem
            table = ax.table(cellText=df.values, 
                            colLabels=df.columns, 
                            cellLoc='center', 
                            loc='center')

            # Estilização da Tabela
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 1.8) # Ajusta o tamanho das células (largura, altura)

            # Deixa o cabeçalho em negrito
            for (row, col), cell in table.get_celld().items():
                if row == 0:
                    cell.set_text_props(weight='bold', color='white')
                    cell.set_facecolor("#078e38") 

            plt.title('LIVROS EMPRESTADOS ATIVOS', fontsize=14, pad=20)
            plt.show()

    except Exception as e:
        print(f'{ej(utility_symbols2['erro'])}  Erro inesperado: {e}.\n')
        return
    

# Nome do empréstimo.
def valid_loan_name():
    while True:
        try:
            min = min_name_loan
            max = max_name_loan

            name = insertion_void(f'{text_format['highlighted']}{ej(techEmojis['computador'])}  NOME DO ACESSÓRIO:\033[m ')
            if len(name) < min or len(name) > max:
                sleep(0.3)
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}\033[m Nome deve ter entre {min} e {max} caracteres.\033[m\n')
                continue

            return name 
        
        except Exception as e:
            print(f'{ej(utility_symbols2['erro'])}  Erro inesperado: {e}.\n')
            return
            


# Finalidade do empréstimo.
def valid_porpuse_loan():
        while True:
            try:
                min = min_purpose
                max = max_purpose

                porpuse = insertion_void(f'{text_format['highlighted']}{ej(utility_symbols2['ajuda'])} FINALIDADE DO EMPRÉSTIMO:\033[m ')

                if len(porpuse) < min or len(porpuse) > max:
                    sleep(0.3)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}\033[m Finalidade deve ter entre {min} e {max} caracteres.\033[m\n')
                    continue

                return porpuse 
            
            except Exception as e:
                print(f'{ej(utility_symbols2['erro'])}  Erro inesperado: {e}.\n')
                return


# Identificador de empréstimo.
def valid_id_loan():
    while True:
        try:
            min = minId_loan
            max = maxId_loan

            id = insertion_void(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  CRIE UM ID NUMÉRICO:\033[m ')
            if len(id) < min or len(id) > max:
                space()
                print(f'{ej(utility_symbols2['erro'])}  ID deve ter entre {min} e {max} dígitos.\n')
                continue

            return id
        
        except ValueError:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Apenas dígitos.\n')
            continue


# Quantidade de acessório.
def valid_quantity_other_loan():
    while True:
        try:
            min = min_quantity_other
            max = max_quantity_other

            quantity = insertion_int(f'{text_format['highlighted']}{ej(workEmojis['numeros'])}  QUANTIDADE:\033[m ')

            if quantity < min or quantity > max:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Quantidade deve estar entre {min} e {max}.\n')
                continue

            return quantity
        
        except ValueError:
            space()
            print(f'{ej(utility_symbols2['erro'])}  Apenas dígitos.\n')
            continue



# Outros tipos de empréstimos.
def other_loan():
    while True:
        try:
            university_user = user_data_dictionary.get('universidade', None)
            print(f'{text_format['highlighted']}{text_collor['white']}{ej(emojisAcademy2["caderno"])} {ej(utility_symbols1['linha_vertical'])} '
                f'REGISTRE OUTROS EMPRÉSTIMOS - {university_user} {ej(utility_symbols1['linha_vertical'])}{text_format['none']}\n')
            
            loan_name = valid_loan_name()
            porpuse_loan = valid_porpuse_loan()
            quantity_loan = valid_quantity_other_loan()

            # Verificação: ID igual.
            while True:
                id_loan = valid_id_loan()
                if id_loan in otherGeneric_loan:
                    space()
                    sleep(0.2)
                    print(f'{ej(utility_symbols2['erro'])}  ID já existente, escolha outro.\n')
                    continue
                else:
                    break


            while True:
                loan_date = validation_date(f'{text_format['highlighted']}{ej(workEmojis["calendario"])}  DATA DE EMPRÉSTIMO:\033[m ')
                delivery_date = validation_date(f'{text_format['highlighted']}{ej(workEmojis["calendario"])}  PREVISÃO DE ENTREGA:\033[m ')

                if datetime.strptime(loan_date, '%d/%m/%Y') > datetime.strptime(delivery_date, '%d/%m/%Y'):
                    space()
                    sleep(0.2)
                    print(f'{ej(utility_symbols2['erro'])}  Data de entrega não deve ser menor que a de empréstimo.\n')
                    continue
                break

            otherGeneric_loan[id_loan] = {LOANNAME: loan_name, 
                                          PORPUSELOAN: porpuse_loan, 
                                          LOANDATE: loan_date, 
                                          DELIVERYDATE: delivery_date,
                                          QUANTITYOTHER: quantity_loan
                                          }
                

            while True: # Continuar ou parar.
                space()
                another_loan = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA REGISTRAR OUTRO EMPRÉSTIMO? (1: SIM - 0: NÃO):\033[m ').strip()
                valid_response = ['1', '0']
                if another_loan not in valid_response:
                    sleep(0.3)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                    continue

                elif another_loan == '1':
                    space()
                    break

                else:
                    space()
                    sleep(0.3)
                    print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                    return  

        except Exception as e:
            print(f'{ej(utility_symbols2['erro'])}  Erro inesperado: {e}.\n')
            return



# DELETAR EMPRÉSTIMOS SECUNDÁRIOS.
def dell_other_loan():

    while True:
        try:
            if not otherGeneric_loan or otherGeneric_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Nenhum registro criado ainda.\n')
                return
            
            # layout
            print(f'{text_format['highlighted']}{text_collor['white']}{text_format['underline']}{ej(workEmojis['marcador'])}  DELETE EMPRÉSTIMOS DE ITENS GERAIS DO SEU REGISTRO.\033[m\n'
                  f'         {text_format['highlighted']}{text_collor['gray']}Digite 0 (10x) para sair).\033[m\n')
            # Exibir id e nome.
            for id_loan, loan in otherGeneric_loan.items():
                print(f'{text_format['highlighted']}{text_collor['white']}ID: {id_loan}:\033[m {text_format['highlighted']}{text_collor['green']}{loan[LOANNAME]}\033[m')
            space()

            identification = str(insertion_void(f'{text_format['highlighted']}DIGITE O ID DO EMPRÉSTIMO QUE DESEJA DELETAR:\033[m ').strip())
            if identification == '0000000000':
                space()
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                return

            if otherGeneric_loan.get(identification, None) is None:
                space()
                print(f'ID inválido. Tente novamente.\n')
                continue

            else:
                space()
                print(f'{ej(utility_symbols1['sucesso'])}  Empréstimo: "{otherGeneric_loan[identification][LOANNAME]}" deletado dos registros.\n')
                otherGeneric_loan.pop(identification)

            # Verificação, para não imprimir mensagem abaixo em vão.
            if not otherGeneric_loan or otherGeneric_loan is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Registro de empréstimos vazio.\n')
                return
            
            else:
                while True: # Continuar ou parar.
                    space()
                    another_dell = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} DESEJA DELETAR OUTRO EMPRÉSTIMO? (1: SIM - 0: NÃO):\033[m ').strip()
                    valid_response = ['1', '0']
                    if another_dell not in valid_response:
                        sleep(0.3)
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                        continue

                    elif another_dell == '1':
                        space()
                        break

                    else:
                        space()
                        sleep(0.3)
                        print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo....\033[m\n')
                        return  
                        
        except Exception as e:
            space()
            print(f'{text_format['highlighted']}{text_collor['white']}Erro inesperado: "{e}".\033[m\n')


# EXIBIR TABELAS DE EMPRÉSTIMOS SECUNDÁRIOS.
def display_other_loan():
    try:
        if not otherGeneric_loan or otherGeneric_loan is None:
            space()
            sleep(0.3)
            print(f'{text_format["highlighted"]}{text_collor["white"]}{ej(utility_symbols2["erro"])}  Você ainda não realizou nenhum registro.\033[m\n')
            return  
        
        other_pd = pd.DataFrame.from_dict(otherGeneric_loan, orient='index').reset_index()
        other_pd.columns = ['ID', LOANNAME, PORPUSELOAN, LOANDATE, DELIVERYDATE, QUANTITYOTHER] 
        fig, ax = plt.subplots(figsize=(12, 4)) 
        ax.axis('tight')
        ax.axis('off')

        table = ax.table(cellText=other_pd.values, 
                                colLabels=other_pd.columns, 
                                cellLoc='center', 
                                loc='center')
        
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.8)

        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor("#078e38")

        plt.title('EMPRÉSTIMOS DE ITENS GERAIS', fontsize=14, pad=20)
        plt.show()

    except Exception as e:
        space()
        print(f'{ej(utility_symbols2['erro'])}  Erro inesperado: {e}.\n')
        return
    


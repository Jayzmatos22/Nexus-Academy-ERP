# MÓDULO PARA FUNÇÕES RELACIONADAS ÀS INFORMAÇÕES DO ALUNO NA UNIVERSIDADE.

import calendar
from allFunctions.user_data_var import (
    user_data_dictionary, particular_science,
    general_science, shifts, valid_shifts, hours_per_class,
    year_now, month_now, types_of_education, duration_per_type_education,
    valid_range_registration, valid_approval_grade
    )

from utils.utilsUx import ej
from emojizeSistem.dict_emojize import utility_symbols2
from allFunctions.insertionTypes import insertion_int, insertion_float, space
from anscii_sistem.collors import text_collor, text_format, background_collors
import pandas as pd
from time import sleep

def science_area():
    while True:
        print(f'{text_format['highlighted']}{text_collor['green']}📚 {text_format['underline']}'
              f'ÁREAS GERAIS DAS CIÊNCIAS 📚\033[m'.center(44))
        print(f'{text_collor['blue']} -Escolha uma das áreas-\033[m\n'.center(20))

        for code, name in general_science.items():
            print(f'{text_format['highlighted']}{text_collor['yellow']} {code} - {name} \033[m')

        print()
        area_choice_user = input(f'{text_format['invert']} Digite o número da área geral:\033[m ').strip()
        print()

        # Validação da área geral
        if area_choice_user not in general_science:
            print(f'{text_collor['red']}{ej(utility_symbols2['erro'])} Área inválida!\033[m\n')
            continue

        oficial_area = general_science[area_choice_user]
        user_data_dictionary['area'] = oficial_area

        while True:
            sleep(0.3)
            print(
                f'{text_format['highlighted']}{text_collor['green']}SUBÁREAS DA CIÊNCIA\033[m - \033[1m{text_collor['blue']}{oficial_area}\033[m\n')
            for cod_sub, name_sub in particular_science[oficial_area].items():
                print(f'{text_format['highlighted']}{text_collor['yellow']}{cod_sub} - {name_sub}\033[m')

            space()
            area_choice = input(f'{text_format['invert']} Digite o número da subárea:\033[m ').strip()
            space()

            if area_choice not in particular_science[oficial_area]:
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])} Subárea inválida!\033[m\n')
                continue

            subarea_escolhida = particular_science[oficial_area][area_choice]
            user_data_dictionary['subarea'] = subarea_escolhida
            print(f'{text_collor['green']}\n🎉 Você escolheu a subárea: {text_format['highlighted']}{subarea_escolhida}\033[m\n')
            return user_data_dictionary


# FUNÇÃO PARA CAPTAR NOME DA UNIVERSIDADE/FACULDADE.
def university_name(n: str):
    while True:
        min_university = 15
        max_university = 70
        # VETOR E VARIÁVEL PARA CONTAR ERROS.
        errors_university = []
        quantity_university_errors = 0
        name_u = input(n).strip().lower()

        # CONDIÇÃO QUE PEGA NÚMEROS E ALFANUMÉRICOS.
        if (name_u.replace(' ', '').isnumeric() or name_u.replace(' ', '').isdigit()
                or (name_u.replace(' ', '').isalnum and not name_u.replace(' ', '').isalpha())):
            errors_university.append(f'{text_collor['red']}Erro, Digite Apenas palavras, sem números ou simbolos\033[m')
            quantity_university_errors += 1

        if len(name_u) < min_university:
            errors_university.append(
                f'{text_collor['red']}Erro, tamanho mínimo: {min_university} caracteres. Não abrevie!\033[m')
            quantity_university_errors += 1

        if len(name_u) > max_university:
            errors_university.append(
                f'{text_collor['red']}Erro, tamanho máximo: {max_university} caracteres. Não abrevie!\033[m')
            quantity_university_errors += 1

        if errors_university:
            space()
            print(f'{text_collor['red']}{quantity_university_errors} Erros encontrados:\033[m')
            for error_u in errors_university:
                print(f'\033[31m-{error_u}\033[m')
            print()
        else:
            return name_u


def insertion_course_shift(cs: str):
    while True:
        print(f'{text_collor['green']}{text_format['underline']}- 🌄 TURNOS DISPONÍVEIS -\033[m\n')
        for shift in valid_shifts:
            print(f'{text_format['highlighted']}{text_collor['yellow']}°{shift}\033[m', end=' / ')
        print()
        space()
        sh = input(cs).strip().lower()
        if sh not in valid_shifts:
            print(f'{text_collor['red']}{ej(utility_symbols2['erro'])}Turno inválido, tente novamente\033[m\n')
        else:
            return sh


# OS HORÁRIOS (start_class, end_class) DE AULA É IGUAL A:
# O TURNO ESCOLHIDO + O INÍCIO E FIM DELES, RESPECTIVAMENTE ATRAVÉS DE 'shifts'.
def course_schedule(user_shift_course):
    start_class = shifts[user_shift_course][0]
    end_class = shifts[user_shift_course][1]
    user_data_dictionary['começo de aula'] = start_class
    user_data_dictionary['fim de aula'] = end_class
    return user_data_dictionary


def quantity_class_day(s: str):
    while True:
        min_class = 3
        max_class = 6
        q_class = insertion_int(s)
        if q_class not in range(min_class, max_class + 1):
            print(f'{text_collor['red']}Quantidade inválida, média de {min_class} a {max_class} aulas por dia.\033[m\n')
        else:
            return q_class


# FUNÇÃO PARA RETORNAR QUANTIDADE DE IDAS À FACULDADE POR SEMANA.
def trips_to_university_week(s: str):
    while True:

        trip = insertion_int(s)
        min_trip = 3
        max_trip = 6
        if trip not in range(min_trip, max_trip + 1):
            print(f'{text_collor['red']}Quantidade inválida. Média {min_trip} a {max_trip} idas por semana.\033[m\n')
            continue

        else:
            return trip


# IMPORTAMOS A VARIÁVEL USADA EM MAIN PARA QUANTIDADE DE AULAS POR DIA E IDAS POR SEMANA (MÉDIA).
# CALCULAMOS COM A FUNÇÃO ABAIXO.
def quantity_class_for_week(class_day: int, trips_week: int):
    final_quantity_class_week = class_day * trips_week
    user_data_dictionary['aulas por semana'] = final_quantity_class_week
    return user_data_dictionary


def quantity_class_per_month():
    cpw = user_data_dictionary['aulas por semana']
    days_per_month = calendar.monthrange(year_now, month_now)
    cpm = cpw * (days_per_month[1] / 7)
    user_data_dictionary['aulas por mês'] = round(cpm, 2)
    return user_data_dictionary


# FUNÇÃO PARA CALCULAR HORAS POR SEMANA
def hours_per_day_week(hr_c: int, trips_week: int):
    hpw = (hr_c * trips_week) * hours_per_class
    user_data_dictionary['horas de aula por dia'] = hours_per_class
    user_data_dictionary['horas de aula por semana'] = hpw
    return user_data_dictionary


# FUNÇÃO PARA CALCULAR HORAS POR MÊS.
def hours_per_month():
    days_per_month = calendar.monthrange(year_now, month_now)
    hpw = user_data_dictionary['horas de aula por semana']
    hpm = hpw * (days_per_month[1] / 7)
    user_data_dictionary['horas de aula por mês'] = round(hpm, 2)
    return user_data_dictionary



# FUNÇÃO PARA EXIBIR DADOS ATUAIS ACADÊMICOS.
def display_general_academy_data():
    df_dict_academy = {
        '---  INFORMAÇÕES PRIMÁRIAS  ---': ['-'],
        ' - - - - - - - - - -': ['-'],
        'Universidade': [user_data_dictionary.get('universidade', 'N/A')],
        'Turno': [user_data_dictionary.get('turno', 'N/A')],
        'Início/aula': [user_data_dictionary.get('começo de aula', 'N/A')],
        'Fim/aula': [user_data_dictionary.get('fim de aula', 'N/A')],
        'Tipo de Curso': [user_data_dictionary.get('tipo de curso', 'N/A')],
        'Quantidade de Semestres': [user_data_dictionary.get('quantidade de semestres', 'N/A')],
        'Semestre atual': [user_data_dictionary.get('semestre atual', 'N/A')],
        'Quantidade de matérias': [user_data_dictionary.get('quantidade de matérias', 'N/A')],
        'Aulas por Dia': [user_data_dictionary.get('aulas por dia', 'N/A')],
        'Idas por Semana': [user_data_dictionary.get('idas por semana', 'N/A')],
        'Nota média de aprovação': [user_data_dictionary.get('nota média de aprovação', 'N/A')],
        # CÁLCULOS BÁSICOS.
        '--------------------': ['-'],
        '---  INFORMAÇÕES SECUNDÁRIAS  ---': ['-'],
        '---------------------': ['-'],
        'Horas por Aula Média': [user_data_dictionary.get('horas de aula por dia', 'N/A')],
        'Horas/Semana Média': [user_data_dictionary.get('horas de aula por semana', 'N/A')],
        'Horas/Mês Média': [user_data_dictionary.get('horas de aula por mês', 'N/A')],
        'Aulas/Mês Média': [user_data_dictionary.get('aulas por mês', 'N/A')]
    }

    # CONVERSÃO PARA DATAFRAME E INVERSÃO.
    df_academy = pd.DataFrame(df_dict_academy)
    df_academy_vert = df_academy.T
    df_academy_vert.columns = ['-- Dados Coletados --']

    print(f'{text_format["highlighted"]}{text_collor["white"]}'
          f' {background_collors["blue"]}📖📚 DADOS ACADÊMICOS DO(A) ALUNO(A) \033[m\n')

    print(df_academy_vert.to_string(header=True))


# FUNÇÃO PARA VALIDAR TIPO DE CURSO DO USUÁRIO.
def get_course_user(cc: str):
    while True:
        try:

            print(f'{text_format["highlighted"]}{text_collor["blue"]}- TIPOS DE CURSOS ELEGÍVEIS -\033[m\n')
            types_of_education.remove('tecnologo')  # REMOVEMOS A DUPLICATA.
            for c in types_of_education:
                print(f'{text_format["highlighted"]}{text_collor["blue"]}{c}\033[m')

            space()
            course = input(cc).strip().lower()
            types_of_education.append('tecnologo')  # REINSERIMOS A DUPLICATA.
            if course not in types_of_education:
                space()
                sleep(0.3)
                print(f'{text_collor["red"]}Curso inválido, tente novamente.\033[m\n')
                continue
            else:
                return course
        except ValueError:
            print(f'{text_collor["red"]}Curso não encontrado\033[m')


# FUNÇÃO PARA VALIDAR QUANTIDADE DE SEMESTRES DE ACORDO COM TIPO DE CURSO.
def get_quantity_semester(sm: str):
    while True:
        try:
            # PEGAMOS O TIPO DE CURSO DO USUÁRIO, DEPOIS BUSCAMOS AS DURAÇÕES VÁLIDAS.
            course = user_data_dictionary.get('tipo de curso')
            valid_semesters = duration_per_type_education.get(course)
            min_sem = min(valid_semesters)  # MÍNIMO DE SEMESTRES
            max_sem = max(valid_semesters)  # MÁXIMO DE SEMESTRES
            print(
                f'{text_collor["yellow"]}Selecione a quantidade de semestres para o tipo de curso:\033[m \033[32m{course}: \033[m\n')

            q_semester = insertion_int(sm)

            if q_semester is None or q_semester not in valid_semesters:
                space()
                sleep(0.3)
                print(
                    f'{text_collor["red"]}Quantidade inválida. Para {course}, escolha entre {min_sem} e {max_sem} semestres.\033[m\n')
                continue
            else:
                return q_semester
        except TypeError:
            continue


# FUNÇÃO PARA CAPTAR MATRÍCULA.
def registration_number(rgt: str):
    while True:
        try:

            # RANGE DE 6 A 10
            min_registration = min(valid_range_registration)
            max_registration = max(valid_range_registration)
            print(f'{text_format["highlighted"]}-> INFORME SUA MATRÍCULA (RA) NA FACULDADE.\033[m\n')
            registration = insertion_int(rgt)

            if len(str(registration)) < min_registration or len(str(registration)) > max_registration:
                space()
                sleep(0.3)
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])}Matrícula inválida! número de caracteres deve ser entre: '
                      f'{min_registration} e {max_registration}.\033[m\n')
                continue
            else:
                return registration
        except ValueError:
            print(f'{text_collor['red']}{ej(utility_symbols2['erro'])}Erro, tente novamente.\033[m')
            continue


# VALIDAR O SEMESTRE ATUAL
def current_semester(sem: str):
    while True:
        try:

            min_sem = 1  # MÍNIMO SEMESTRE ATUAL
            # TOTAL DE SEMESTRES
            total_semesters = user_data_dictionary['quantidade de semestres']
            current_sm = insertion_int(sem)

            if current_sm < min_sem:
                space()
                sleep(0.3)
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])} Erro, '
                      f'semestre mínimo atual deve ser igual ou maior a {min_sem} e {total_semesters}.\033[m\n')
                continue

            elif current_sm > total_semesters:
                space()
                sleep(0.3)
                print(f'{text_collor['red']}{ej(utility_symbols2['erro'])} Erro, '
                      f'semestre atual não pode ser maior que o total de semestres do seu curso: ({total_semesters}).\033[m\n')
                continue

            else:
                return current_sm

        except ValueError:
            print(f'{ej(utility_symbols2['erro'])} ERRO, TENTE NOVAMENTE {ej(utility_symbols2['erro'])}\n\033[m')
            continue


# FUNÇÃO PARA OBTER MÉDIA DA UNIVERSIDADE DO ALUNO.
def approval_grade(ap: str):
    while True:
        try:

            # MÁXIMO E MÍNIMO (INTERVALO).
            approval = insertion_float(ap)
            range_approval = valid_approval_grade
            min_approval = min(range_approval)
            max_approval = max(range_approval)
            if approval < min_approval:

                space()
                sleep(0.2)
                print(f'{text_collor['red']}Média não pode ser inferior a {min_approval}\033[m\n')
                continue
            elif approval > max_approval:
                space()
                sleep(0.2)
                print(f'{text_collor['red']}Média não pode ser superior a {max_approval}\033[m\n')
                continue

            approval = f'{approval:.2f}'
            return approval
        except ValueError:
            print(f'{ej((utility_symbols2['erro'])) * 3} Erro, dado inválido\033[m\n')




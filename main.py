# IMPORTAÇÕES PARA UX.
from anscii_sistem.collors import (
    text_collor,
    text_format,
    )

# IMPORTAÇÕES PARA FUNÇÕES DO USUAÁRIO.
from allFunctions.data_user_functions import (
    insertion_email, insertion_password, biological_sexuality,
    insertion_cpf, insertion_age, insertion_name, gender_identity_input
    )

# IMPORTAÇÕES DE FUNÇÕES PARA USO ACADÊMICO.
from allFunctions.user_academy_functions import (
    science_area, university_name, course_schedule,
    insertion_course_shift, quantity_class_day,
    trips_to_university_week, quantity_class_per_month,
    quantity_class_for_week, hours_per_day_week, hours_per_month,
    get_course_user,get_quantity_semester, registration_number, current_semester, approval_grade
    )


# IMPORTAÇÃO DO DICIONÁRIO PRINCIPAL PARA DADOS.
from allFunctions.user_data_var import user_data_dictionary

# IMPORTAÇÃO PARA UTILIDADES.
from allFunctions.insertionTypes import space


# IMPORTAÇÕES DE FUNÇÕES DE CRUD E UX.
from utils.utilsUx import (
    display_smart_layout, init_message, display_calendar, display_menu_options,
    displaynow, layout_submenu_bank, layout_submenu_loan_books, layout_submenu_other_loans, layout_submenu_tasks, message_create_login, display_message_science_area,
    message_personal, confirmation, logo_message_app, submenu_crud_datauser, display_allgeneral_options, layout_input_academic_data2
)

# FUNÇÕES DE NOTAS, MATÉRIAS E ATIVIDADES.
from subjects_and_tasksAcademy.subjectTaskFunctions import (
    quantity_subjects_semester, name_subjects_semester, 
    quantity_tasks_per_subject, grades_by_activities,
    )

# CRUD DE EMPRÉSTIMOS DA UNIVERSIDADE E OUTROS.
from utilsCrud.crudUniversity import (
    get_function_other_loan, submenu_layout_academy,
    get_dict_optionsUniversity_to_display, get_function_loan_books
    )

# CRUD DE DADOS DO USUÁRIO.
from utilsCrud.crudDataUser import (
    submenu_crud_datauser, get_dict_optionsCrudDataUser_to_display
    )

# CRUD DE TAREFAS/AGENDA/BANCO/EMPRÉSTIMOS.
from utilsCrud.crudCreate import get_function_tasks
from utilsCrud.crudBankUser import get_function_bankuser



display_smart_layout()
space()
init_message()
space()
display_calendar()
space()
displaynow()
space()
message_create_login()
space()



# CRIAÇÃO DE LOGN SIMPLES COM APLICAÇÃO DAS FUNÇÕES.
while True:

    create_email = insertion_email(f'{text_format["invert"]} CRIAR EMAIL:\033[m ')
    space()
    create_password = insertion_password(f'{text_format["invert"]} CRIAR SENHA:\033[m ')
    space()

    space()
    if confirmation():
        # ATRIBUIÇÃO DE DADOS AO DICIONÁRIO PRINCIPAL
        user_data_dictionary['email'] = create_email
        user_data_dictionary['senha'] = create_password
        print(f'{text_format['highlighted']}{text_collor["green"]}'
              f'Login criado com sucesso.\033[m')
        space()
        break

    else:
        continue


# FLUXO DE COLETA DE DADOS PESSOAIS.
while True:
    message_personal()

    username = insertion_name(f'{text_format["invert"]} NOME COMPLETO:\033[m ')
    user_data_dictionary['nome'] = username

    age_user = insertion_age()
    user_data_dictionary['idade'] = age_user
    space()

    cpf_user = insertion_cpf(f'{text_format["invert"]} CPF (somente números):\033[m ')
    user_data_dictionary['cpf'] = cpf_user
    space()

    bioSexuality_user = biological_sexuality(f'{text_format["invert"]}SEU SEXO BIOLÓGICO:\033[m ')
    space()

    gender_user = gender_identity_input(f'{text_format["invert"]} IDENTIDADE DE GÊNERO:\033[m ')
    space()

    if confirmation():
        user_data_dictionary['nome'] = username
        user_data_dictionary['idade'] = age_user
        user_data_dictionary['cpf'] = cpf_user
        user_data_dictionary['sexo biológico'] = bioSexuality_user
        user_data_dictionary['gênero sexual'] = gender_user
        break

    else:
        continue


# FLUXO DE COLETA DE DADOS ACADÊMICOS PRIMÁRIOS.
while True:
    display_message_science_area()

    # ÁREA E SUBÁREA SÃO ATUALIZADAS AO UTILIZAR A FUNÇÃO SOZINHA.
    science_area()
    user_university_name = university_name(f'{text_format["invert"]}NOME DA UNIVERSIDADE:\033[m ')
    user_data_dictionary['universidade'] = user_university_name
    space()

    user_registration_number = registration_number(f'{text_format['invert']} MATRÍCULA/RA:\033[m ')
    space()

    student_course_user = get_course_user(f'{text_format["invert"]}TIPO DE CURSO:\033[m ')
    user_data_dictionary['tipo de curso'] = student_course_user
    space()

    course_shift_user = insertion_course_shift(f'{text_format["invert"]} TURNO DO CURSO:\033[m ')
    space()

    quantity_semester_user = get_quantity_semester(f'{text_format["invert"]} QUANTIDADE DE SEMESTRES DO CURSO:\033[m ')
    user_data_dictionary['quantidade de semestres'] = quantity_semester_user
    space()

    current_semester_user = current_semester(f'{text_format["invert"]} SEMESTRE ATUAL:\033[m ')
    user_data_dictionary['semestre atual'] = current_semester_user
    space()

    quantity_subject_user = quantity_subjects_semester(f'{text_format["invert"]} QUANTIDADE DE MATÉRIAS NESSE SEMESTRE:\033[m ')
    user_data_dictionary['quantidade de matérias'] = quantity_subject_user
    space()


    user_shift_course = course_schedule(course_shift_user)

    quantity_class_user = quantity_class_day(f'{text_format["invert"]} '
                                             f'QUANTIDADE DE AULAS POR DIA (MÉDIA):\033[m ')
    space()
    trip_university_user = trips_to_university_week(f'{text_format["invert"]} '
                                                    f'IDAS À FACULDADE POR SEMANA (MÉDIA):\033[m ')
    space()

    approval_grade_university = approval_grade(f'{text_format["invert"]} NOTA (MÉDIA) DE APROVAÇÃO EM '
                                               f'{user_data_dictionary['universidade'].capitalize()}:\033[m ')
    user_data_dictionary['nota média de aprovação'] = approval_grade_university

    # USO DAS FUNÇÕES PARA CALCULAR:
    # AULAS POR SEMANA, MÊS - HORAS POR SEMANA, MÊS
    user_data_dictionary['turno'] = course_shift_user
    user_data_dictionary['aulas por dia'] = quantity_class_user
    user_data_dictionary['idas por semana'] = trip_university_user
    quantity_class_for_week(quantity_class_user, trip_university_user)
    quantity_class_per_month()
    hours_per_day_week(quantity_class_user, trip_university_user)
    hours_per_month()
    space()

    # NOTAS - MATÉRIAS - ATIVIDADES
    # INSERÇÃO DE DADOS ACADÊMICOS SECUNDÁRIOS.
    layout_input_academic_data2()
    space()

    name_subjects_semester()
    space()
 
    quantity_tasks_per_subject()
    space()

    grades_by_activities()
    space()

    if confirmation():
        break
    else:
        # Limpa os dados para evitar sujeira se o usuário quiser recomeçar
        from allFunctions.user_data_var import vector_subjects_name, student_grades
        vector_subjects_name.clear()
        student_grades.clear()
        continue



# MENU PRINCIPAL COM SUBMENUS.
while True:
    logo_message_app()
    space()
    display_allgeneral_options()
    options = display_menu_options()

    # 1: MEUS RELATÓRIOS ACADÊMICOS
    if options == '1':
        space()
        
        submenu_layout_academy()
        get_dict_optionsUniversity_to_display()
        continue

    # 2: ÁREA DO USUÁRIO (DADOS PESSOAIS)
    elif options == '2':
 
        submenu_crud_datauser()
        get_dict_optionsCrudDataUser_to_display()
        continue

    # 3: GERENCIAR TAREFAS/AGENDAS
    elif options == '3':
        space()
        layout_submenu_tasks()
        get_function_tasks()
        continue

    # 4: SETOR BANCÁRIO DO ALUNO
    elif options == '4':
        space()
        layout_submenu_bank()
        space()
        get_function_bankuser()
        continue

    # 5: EMPRÉSTIMO DE LIVROS DA UNIVERSIDADE
    elif options == '5':
        layout_submenu_loan_books()
        get_function_loan_books()
        continue

    # 6: OUTROS EMPRÉSTIMOS GENÉRICOS
    elif options == '6':
        layout_submenu_other_loans()
        get_function_other_loan()
        continue

    # 0: SAIR DO SISTEMA
    elif options == '0':
        break
    break

    





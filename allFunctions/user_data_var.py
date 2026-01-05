import datetime

# SIMPLES DATABASE PARA O CURSO DO USUÁRIO

general_science = {
    '1': 'Ciências Exatas e da Terra',
    '2': 'Ciências Biológicas',
    '3': 'Engenharia',
    '4': 'Ciências da Saúde',
    '5': 'Ciências Agrárias',
    '6': 'Ciências Humanas',
    '7': 'Ciências Sociais Aplicadas',
    '8': 'Linguística, Letras e Artes'
}


particular_science = {
    'Ciências Exatas e da Terra': {
        '1': 'Matemática',
        '2': 'Probabilidade e Estatística',
        '3': 'Ciência da Computação',
        '4': 'Astronomia',
        '5': 'Física',
        '6': 'Química',
        '7': 'Geologia',
        '8': 'Geofísica',
        '9': 'Meteorologia'
    },

    'Ciências Biológicas': {
        '1': 'Biologia Geral',
        '2': 'Genética',
        '3': 'Zoologia',
        '4': 'Botânica',
        '5': 'Ecologia'
    },

    'Engenharia': {
        '1': 'Engenharia Civil',
        '2': 'Engenharia Mecânica',
        '3': 'Engenharia Elétrica',
        '4': 'Engenharia Química',
        '5': 'Engenharia da Computação'
    },

    'Ciências da Saúde': {
        '1': 'Medicina',
        '2': 'Enfermagem',
        '3': 'Odontologia',
        '4': 'Farmácia',
        '5': 'Nutrição'
    },

    'Ciências Agrárias': {
        '1': 'Agronomia',
        '2': 'Zootecnia',
        '3': 'Engenharia Florestal',
        '4': 'Medicina Veterinária'
    },

    'Ciências Humanas': {
        '1': 'Filosofia',
        '2': 'História',
        '3': 'Geografia',
        '4': 'Psicologia',
        '5': 'Educação'
    },

    'Ciências Sociais Aplicadas': {
        '1': 'Administração',
        '2': 'Direito',
        '3': 'Economia',
        '4': 'Arquitetura e Urbanismo',
        '5': 'Turismo'
    },

    'Linguística, Letras e Artes': {
        '1': 'Linguística',
        '2': 'Letras',
        '3': 'Artes Visuais',
        '4': 'Música',
        '5': 'Teatro'
    }
}


# MODELO DE HORÁRIOS SIMPLES POR TURNO.
shifts = {
    'matutino': ('07:00', '10:30'),
    'vespertino': ('13:00', '16:30'),
    'noturno': ('19:00', '22:30')
    }

# HORAS POR AULA
hours_per_class = 3.5


# TURNOS DISPONÍVEIS
valid_shifts = ['matutino','noturno', 'vespertino']


# DICIONÁRIO ONDE FICARÂO AS PRINCIPAIS INFO DO USUÁRIO.
user_data_dictionary = {}


# VARIÁVEIS SOBRE ANO E MÊS ATUAL ATUALIZADOS.
year_now = datetime.datetime.now().year
month_now = datetime.datetime.now().month


# TIPOS DE EDUCAÇÃO. AS 3 PRINCIPAIS.
types_of_education = [
    "tecnólogo",
    "licenciatura",
    "bacharelado",
    'tecnologo'
    ]

# TIPOS DE CURSOS E SUAS DURAÇÕES MÍNIMAS E MÁXIMAS EM SEMESTRES.
technologist_duration = [4, 5, 6]
bachelors_degree_duration = [8, 9, 10]
bachelor_duration = [8, 9, 10, 11, 12]

duration_per_type_education = {
    "tecnólogo": technologist_duration,
    "licenciatura": bachelors_degree_duration,
    "bacharelado": bachelor_duration,
    "tecnologo": technologist_duration
    }


# SEXO BIOLÓGICO.
valid_sexualitys = ['homem', 'mulher']


# NÚMERO MÁXIMO E MÍNIMO DE MATRÍCULA
valid_range_registration = [6, 7, 8, 9, 10]


# INTERVALO DE MATÉRIAS NO SEMESTRE.
range_subjects_semester = [4, 5, 6, 7, 8, 9, 10]


# VETOR PARA NOMES DAS MATÉRIAS.
vector_subjects_name = []


# MÉDIA DE APROVAÇÃO EM UNIVERSIDADES.
valid_approval_grade = [5.0, 7.0]


# TOTAL DE ATIVIDADES VÁLIDAS POR MATÉRIA.
valid_total_tasks_subject = [3, 4, 5]


valid_range_grades_per_activities = [0.0, 10.0]

# DICIONÁRIO PARA GUARDAR AS NOTAS DAS MATÉRIAS.
student_grades = {} 


# DICIONÁRIO PARA ARMAZENAR TAREFAS CRIADAS.
tasks_created = {}


# DICIONÁRIO PARA EMPRÉSTIMO DE LIVROS.
# Variáveis e constantes.
dict_book_loan = {}
ISBN10 = 10
ISBN13 = 13
min_title = 10
max_title = 150
min_subject = 2
max_subject = 50
min_author = 10
max_author = 100
min_quantity_books = 1
max_quantity_books = 20
BOOKNAME = 'título do livro'
AUTHOR = 'nome do autor'
ISBNID = 'id ISBN'
BOOKSUBJECT = 'assunto do livro'
LOANDATE = 'data de empréstimo'
DELIVERYDATE = 'data de devolução'
QUANTITYBOOKS = 'quantidade'

# DICIONÁRIO EMPRÉSTIMOS GENÉRICOS.
# Variáveis e constantes.
otherGeneric_loan = {}
LOANNAME = 'nome empréstimo'
PORPUSELOAN = 'finalidade'
QUANTITYOTHER = 'quantidade'
min_quantity_other = 1
max_quantity_other = 10
minId_loan = 4
maxId_loan = 13
min_name_loan = 5
max_name_loan = 35
min_purpose = 8
max_purpose = 45



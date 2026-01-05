# MÓDULO PARA VALIDAR OS DADOS DO USUÁRIO
# USAMOS PARÂMETROS IDEIAS PARA ISSO (EX. IDADE, EMAIL...)

from anscii_sistem.collors import text_collor, text_format, background_collors
from time import sleep
import datetime
from allFunctions.insertionTypes import insertion_int, space
from extensiveList_generies.listMaxGender import gender_identitiesNp, gender_identitiesPunctuation
from allFunctions.user_data_var import valid_sexualitys
from utils.utilsUx import ej
from emojizeSistem.dict_emojize import utility_symbols2
import pandas as pd
from allFunctions.user_data_var import user_data_dictionary

def insertion_name(m: str):
    while True:
 
        # SIMBOLOS PROIBIDOS DE USAR NO NOME.
        simbolos = ('@#$%^&*"()-_=+[]{};:,.<>?/|`~¬§±¢£¥€©®™¶•†‡∞≠≈≤≥÷×√∑∏µΩ∆π∂∞→←↑↓↔↕↩↪↠↯∀∃⊂⊃⊆⊇⊕⊗⊥∴∵∽≡∈∉∧∨¬-Q'
                    '\∩∪◊□■▪▫▲△▼▽◆◇○●◉◎◌◍☀☁☂☃☄★☆✡✦✧✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋☼☽☾☯☮☢☣⚐⚑⚒⚓⚔⚕⚖'
                    '⚗⚙⚛⚜♠♣♥♦♤♧♡♢♩♪♫♬♭♮♯⌘⌂⌛⌚⌫⏎⏏⎈⎋')
        name_min = 7
        name_max = 30
        errors_name = []  # VETOR QUE ARMAZENA OS ERROS DO USUÁRIO NO NOME.
        quantity_errors_name = 0  # CONTABILIZA OS ERROS
        name_user = input(m).strip().lower()

        # LIMPEZA DE ERROS. ARMAZENA NO VETOR E MOSTRA NO FINAL.
        try:
            if name_user.isdigit() or name_user.isnumeric():
                errors_name.append(f'{text_collor["red"]}Erro, digite apenas palavras!\033[m')
                quantity_errors_name += 1
            if '.' in name_user:
                errors_name.append(
                    f'{text_collor["red"]}Erro, não pode conter pontos/pontos duplos (".")\033[m')
                quantity_errors_name += 1
            if len(name_user.replace(" ", "")) < name_min:
                errors_name.append(f'{text_collor["red"]}Erro, tamanho mínimo exigído: {name_min}\033[m')
                quantity_errors_name += 1
            if len(name_user.replace(' ', '')) > name_max:
                errors_name.append(
                    f'{text_collor["red"]}Erro, tamanho máximo permitido: {name_max}\033[m')
                quantity_errors_name += 1
            if any(s in simbolos.replace(' ', '') for s in name_user):
                errors_name.append(
                    f'{text_collor["red"]}Erro, nome não pode conter símbolos/caracteres não puramente alfabéticos!\033[m')
                quantity_errors_name += 1
            if not ' ' in name_user:
                errors_name.append(
                    f'{text_collor["red"]}Erro, formato inválido, use "nome - sobrenome ..."!\033[m')
                quantity_errors_name += 1
            if errors_name:
                sleep(0.3)
                print(f'{text_collor["gray"]}-->VALIDANDO\033[m\n')
                sleep(0.3)
                print(f'{text_format["highlighted"]}{quantity_errors_name} ERRO(S) ENCONTRADO(S):')
                sleep(0.3)
                for e_u in errors_name:
                    sleep(0.3)
                    print(f'{e_u}')
                sleep(0.3)
                print(f'{text_collor["green"]}{text_format["highlighted"]}### TENTE NOVAMENTE ###\033[m\n')

            # COMO CADA IF FOI FEITO SEPARADAMENTE, SE NÃO HÁ ERRO PEGO PELO IF ANTERIOR, ENTÃO RETORNA "name".
            else:
                return name_user
        except ValueError:
            continue


def insertion_password(msg, min_password: int = 8, max_password: int = 20):
    vazio_espaco = ''
    while True:  # Uso de while True para que o usuário sempre tenha a chance de acessar a conta.
        password_user = input(msg).strip()  # Variavel que recebe o input da senha.
        errors_password = []  # VETOR QUE ARMAZENA OS ERROS PEGO PELOS IF.                                                                                             # Vetor que recebe os erros acumulados em cada if, alocados atraves do método 'append'
        simbolos = '\033[35m@#$%^&*~!"¨><´`()-_=+[]{};:,.?/\\|\033[m'  # Símbolos aceitos na validação de senha.
        quantity_errors_password = 0  # Soma a quantidade de erros que o usuário cometeu, vindo após isso os erros em si (erros_senha).
        # SÉRIE DE CRITÉRIOS PARA UMA SENHA FORTE. USO DO ANY PARA VALIDAR PELO MENOS UM 1 CRITÉRIO DA CONDIÇÃO DENTRO DA SENHA
        if not any(c.isupper() for c in password_user):
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MAIÚSCULO!\033[m')
            quantity_errors_password += 1
        if not any(c.islower() for c in password_user):
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MINÚSCULO!\033[m')
            quantity_errors_password += 1
        if not any(c.isdigit() for c in password_user):
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mDÍGITO!\033[m')
            quantity_errors_password += 1
        if len(password_user) < min_password:
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m{min_password}\033[m \033[31mCARACTERES!\033[m')
            quantity_errors_password += 1
        if not any(c in simbolos for c in password_user):
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER ALGUM SÍMBOLO ESPECIAL! \033[m' + simbolos)
            quantity_errors_password += 1
        if len(password_user) > max_password:
            errors_password.append(
                f'{text_collor['red']}A SENHA DEVE CONTER NO MÁXIMO:\033[m \033[34m{max_password}\033[m \033[31mCARACTERES!\033[m')
            quantity_errors_password += 1

        # MOSTRA O VETOR DE ERROS SOMENTE SE ELE CONTÉM ALGUM ELEMENTO:
        if errors_password:  # Condição para ser possível exibir os erros e a sua soma. o else abaixo verifica a inexistência dos erros, retornando, assim, "password'.
            if quantity_errors_password == 1:
                sleep(0.5)
                print(f'{text_collor['gray']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(
                    f'{text_collor['red']}{quantity_errors_password}\033[m \033[37mERRO ENCONTRADO NA SUA SENHA:\033[m\n')
                sleep(0.5)
                for erro in errors_password:
                    sleep(0.5)
                    print(erro)
                print(f'{text_collor['green']}### TENTE NOVAMENTE! ###\033[m\n')
            else:
                sleep(0.5)
                print(f'{text_collor['gray']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(
                    f'{text_collor['red']}{quantity_errors_password}\033[m \033[37mERROS ENCONTRADOS NA SUA SENHA:\033[m\n')
                for erroS in errors_password:
                    sleep(0.5)
                    print(erroS)
                print(f'{text_collor['green']}// TENTE NOVAMENTE! //\033[m\n')
                sleep(0.5)
        else:
            return password_user


def insertion_email(mg: str, min_email: int = 10, max_email: int = 30):
    while True:  # while True para o restante da função, pois os critérios devem ser atentidos, podendo ser possível refazer o processo caso o usuário erre em algum critério.
        quantity_errors_email = 0  # Variável para soma dos erros dos usuário na criação do email.
        errors_email = []  # Vetor onde é armazenado os erros cometidos pelo usuário na criação do email.
        emai = input(
            mg).strip().lower()  # A funão lower é usada para ignorar maiusculas, de forma que se o usuário cria um email "XXX', ele pode acessar como 'XxX'.
        # SÉRIE DE CRITÉRIOS ('@', SEM DOIS PONTOS SEGUIDOS '..' ETC) QUE OS EMAILS NORMALMENTE POSSUEM.
        if not emai:
            errors_email.append(f'{text_collor['red']}ERRO, ESPAÇO VAZIO!\033[m')
            quantity_errors_email += 1
        if ' ' in emai:
            errors_email.append(f'{text_collor['red']}NÃO PODE CONTER ESPAÇOS!\033[m')
            quantity_errors_email += 1
        if len(emai) < min_email:
            errors_email.append(
                f'{text_collor['red']}O EMAIL DEVE CONTER AO MENOS\033[m \033[34m{min_email}\033[m \033[31mCARACTERES!\033[m')
            quantity_errors_email += 1
        if len(emai) > max_email:
            errors_email.append(
                f'{text_collor['red']}O EMAIL DEVE CONTER NO MÁXIMO\033[m \033[34m{max_email}\033[m \033[31mCARACTERES!\033[m')
            quantity_errors_email += 1
        if not '@' in emai:
            errors_email.append(f'{text_collor['red']}O EMAIL DEVE CONTER\033[m \033[32m"@"\033[m')
            quantity_errors_email += 1
        if emai.count('@') > 1:
            errors_email.append(f'{text_collor['red']}ERRO, DEVE CONTER APENAS UM\033[m \033[32m"@"\033[m')
            quantity_errors_email += 1
        if '..' in emai:
            errors_email.append(f'{text_collor['red']}ERRO, NÃO É PERMITIDO PONTOS CONSECUTIVOS!\033[m')
            quantity_errors_email += 1
        if not '.' in emai:
            errors_email.append(f'{text_collor['red']}O EMAIL DEVE CONTER PONTO "."\033[m')
            quantity_errors_email += 1
        if '@' in emai:
            local, dominio_parte = emai.split('@', 1)
            if local.startswith('.') or local.endswith('.'):
                errors_email.append(
                    f'{text_collor['red']}ERRO, PARTE\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR NEM TERMINAR COM PONTO: "."\033[m')
                quantity_errors_email += 1
            if dominio_parte.startswith('.') or dominio_parte.endswith('.'):
                errors_email.append(
                    f'{text_collor['red']}DOMÍNIO DEPOIS\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR/TERMINAR COM PONTO: "."\033[m')
                quantity_errors_email += 1
            if '..' in emai:
                errors_email.append(f'{text_collor['red']}NÃO PODE CONTER PONTOS CONSECUTIVOS: ".."\033[m')
        if errors_email:  # Condição para exibição dos erros.
            if quantity_errors_email == 1:
                print(f'{text_collor['gray']}---->VALIDANDO...\033[m')
                print(f'{text_collor['red']}{quantity_errors_email}\033[m \033[37mERRO ENCONTRADO!\033[m\n')
                for erro in errors_email:
                    sleep(0.5)
                    print(erro)
                print(f'{text_collor['green']}// TENTE NOVAMENTE //\033[m\n')
            else:
                sleep(0.5)
                print(f'{text_collor['gray']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(f'{text_collor['red']}{quantity_errors_email}\033[m \033[37mERROS ENCONTRADOS!\033[m\n')
                for erro in errors_email:
                    sleep(0.5)
                    print(erro)
                print(f'{text_collor['green']}{text_format['highlighted']}// TENTE NOVAMENTE //\033[m\n')
        else:
            return emai


def insertion_age():
    # 🎯 O loop garante que o programa só sairá com uma idade válida
    while True:
        try:
            print()
            print(f'{text_collor["yellow"]}Por favor, digite sua data de nascimento (apenas números) {ej(utility_symbols2['data_nascimento'])}\n\033[m')

            # Coleta as três partes em uma única tentativa
            day = insertion_int(f'{text_format["invert"]} DIA (DD):\033[m ')
            print()
            month = insertion_int(f'{text_format["invert"]} MÊS (MM):\033[m ')
            print()
            year = insertion_int(f'{text_format["invert"]} ANO (AAAA):\033[m ')

            # 1. Tenta criar o objeto datetime.date
            # Se for uma data inválida no calendário (ex: 30 de Fevereiro),
            # o Python lança um ValueError, que é pego pelo 'except' abaixo.
            date_birth = datetime.date(year, month, day)

            # 2. Se a data é válida, calcula a idade:
            today = datetime.date.today()

            # Cálculo base (diferença dos anos)
            idade_base = today.year - date_birth.year

            # Ajuste de idade: Verifica se o aniversário já ocorreu neste ano
            if (today.month, today.day) < (date_birth.month, date_birth.day):
                idade_final = idade_base - 1
                return idade_final
            else:
                idade_final = idade_base
                return idade_final
            # 3. Se tudo deu certo, imprime o resultado e sai do loop

        except ValueError as e:

            # Verifica se o erro é específico do datetime (data inválida)
            if "day is out of range for month" in str(e) or "month must be in 1..12" in str(e):
                print()
                print(
                    f"⚠️ {text_collor['red']}Data inválida no calendário: {e}. Verifique se o dia existe no mês.\033[m")

            print(f"{text_collor['yellow']}Tente novamente.\033[m")
            continue  # Volta para o início do 'while True' para nova tentativa


def insertion_cpf(c: str):
    while True:

        # COLETA DE ERROS PARA AJUDAR USUÁRIO.
        size_cpf = 11
        errors_cpf = []
        quantity_errors_cpf = 0
        try:
            sleep(0.3)
            cp = input(c)
            if not cp:
                errors_cpf.append(f'{text_collor['red']}Caixa vazia\033[m\n')
                quantity_errors_cpf += 1
            if not cp.isdigit():
                errors_cpf.append(f'{text_collor['red']}Digite apenas números\033[m\n')
                quantity_errors_cpf += 1
            if len(cp) > size_cpf or len(cp) < size_cpf:
                errors_cpf.append(f'{text_collor['red']}Tamanho inválido, necessário {size_cpf} dígitos\033[m\n')
                quantity_errors_cpf += 1
            if errors_cpf:
                sleep(0.3)
                print(f'{text_collor['red']}{quantity_errors_cpf} Erro(s) encontrados: \033[m\n')
                sleep(0.3)
                for cc in errors_cpf:
                    print(cc)
            else:
                sleep(0.3)

                return cp
        except ValueError:
            continue


# FUNÇÃO PARA VALIDAÇÃO DE SEXO BIOLÓGICO
def biological_sexuality(sx: str):
    while True:
        v_s = valid_sexualitys
        print(
            f'{text_collor["green"]}{text_format["underline"]}VOCÊ É HOMEM OU MULHER? (BIOLOGICAMENTE FALANDO)?\033[m\n')
        sleep(0.3)
        sexuality = input(sx).lower().strip()
        if sexuality not in v_s:
            space()
            print(f'{text_collor['red']} Sexualidade inválida, tente novamente\033[m\n')
            continue
        else:
            return sexuality

        # FUNÇÃO PARA INSERÇÃO DE IDENTIDADE DE GÊNERO.


# Gênero Sexual.
def gender_identity_input(g: str):
    while True:
        print(f'{text_collor["green"]}{text_format["underline"]}- IDENTIDADES DE GÊNERO DISPONÍVEIS -\033[m\n')
        sleep(0.3)

        for i, identity in enumerate(gender_identitiesPunctuation, start=1):
            print(f'{text_format["highlighted"]}{text_collor["yellow"]}{i}° --> {identity}\033[m')
            sleep(0.1)

        space()
        gender = input(g).strip().lower()
        if gender not in gender_identitiesNp and gender not in gender_identitiesPunctuation:
            space()
            print(f'{text_collor["red"]}Opção inválida, tente novamente\033[m\n')
            sleep(0.3)
        else:
            return gender


# FUNÇAO PARA EXIBIR DADOS DE FORMA LIMPA USANDO PANDAS.
def display_general_personal_data():
    df_personal_data = {
        'Nome Completo': [user_data_dictionary.get('nome', 'N/A')],
        'Idade': [user_data_dictionary.get('idade', 'N/A')],
        'CPF': [user_data_dictionary.get('cpf', 'N/A')],
        'Sexo Biológico': [user_data_dictionary.get('sexo biológico', 'N/A')],
        'Gênero': [user_data_dictionary.get('gênero sexual', 'N/A')]
    }

    # CONVERSÃO PARA DATAFRAME E INVERSÃO DE COLUNAS.
    df_personal = pd.DataFrame(df_personal_data)
    df_personal_vert = df_personal.T
    df_personal_vert.columns = ['-- Dados Coletados --']
    space()

    print(f'{text_format["highlighted"]}{text_collor["white"]}'
          f' {background_collors["blue"]}👤 DADOS PESSOAIS DO(A) ALUNO(A) \033[m\n')

    print(df_personal_vert.to_string(header=True))



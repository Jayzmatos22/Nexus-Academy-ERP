from anscii_sistem.collors import text_collor, text_format, background_collors
from emoji import emojize
from time import sleep
import datetime
from emojizeSistem.dict_emojize import academyEmojis, workEmojis, techEmojis, financeEmojis, emojisAcademy2
import calendar
from allFunctions.insertionTypes import space
from emojizeSistem.dict_emojize import utility_symbols2, utility_symbols1
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from pyfiglet import figlet_format


# VARIÁVEIS DAS DATAS
today = datetime.date.today()
current_day = today.day
current_month = today.month
current_year = today.year


# UMA DAS MENSAGNES INICIAIS. PARA EXIBIR DATA E HORÁRIO.
def displaynow():
    sleep(0.3)
    print(f'{text_format['highlighted']}{background_collors['green']} {ej(techEmojis['engrenagem'])}  SISTEMA INICIADO EM - '
          f'{background_collors['yellow']} {current_day}/{current_month}/{current_year} ÀS '
          f'{datetime.datetime.now().strftime("%H:%M:%S")}...\033[m\n')


# FUNÇÃO PARA FACILITAR EXIBIÇÃO DE EMOJI (SEM USAR "EMOJIZE").
def ej(code):
    return emojize(code, language='alias')


# IXIBIR CALENDÁRIO
def display_calendar():
    print(
        f'{text_format["highlighted"]}{text_collor["green"]}       {ej(workEmojis["calendario"])} CALENDARIO GERAL {ej(workEmojis['cronometro'])}{text_format["none"]}\n')
    sleep(0.5)
    print(f'{text_format["highlighted"]}{text_collor["green"]}{text_format["invert"]}'
          f'{calendar.month(current_year, current_month)}{text_format["none"]}\n')


# MENSAGEM INICIAL.
def init_message():
    msg = (
        f'{text_format["highlighted"]}{text_collor["blue"]} {ej(academyEmojis["biblioteca"])} BEM VINDO À BIBLIOTECA DE ESTUDOS {ej(academyEmojis["caderno"])}{text_format["none"]}\n')
    msx = msg.split(' ', 6)
    for m in msx:
        sleep(0.5)
        print(m, end=' ')

# função de criação de login.
def message_create_login():
    sleep(0.2)
    print(f'{text_format['highlighted']}{background_collors['red']} {ej(techEmojis['web'])}  ANTES DE PODER USAR O SISTEMA, POR GENTILEZA CRIE UM LOGIN!\033[m'.center(15))
    sleep(0.1)
    space()
    print(f'{text_format['highlighted']}PREENCHA OS CAMPOS ABAIXO {ej(utility_symbols2['info'])}\033[m\n')





# MENSAGEM DA ÁREA A ESCOLHER.
def display_message_science_area():
    print(
        f'{text_format["highlighted"]}{text_collor["white"]} '
        f'{background_collors["blue"]}📖 AGORA, INFORME SUA ÁREA DE ESTUDO 📖\033[m\n')


# MENSAGEM DE DADOS PESSOAIS.
def message_personal():
    print(
        f'{text_format["highlighted"]}{text_collor["white"]} {background_collors["green"]}👤 '
        f'POR GENTILEZA, NOS INFORME ALGUNS DADOS PESSOAIS 👤\033[m\n')


# FUNÇÃO PARA CONFIRMAR ALGUMA ENTRADA DE DADOS.
def confirmation():
    print(
        f'{text_collor["yellow"]}{ej(utility_symbols1['alerta'])}  CONFIRMAR DADOS? '
        f'(1: SIM - OUTRO BOTÃO: REDIGITAR):\033[m\n')
    cf =str(input(f'{text_format['invert']}{text_collor['green']} CONFIRMAÇÃO:\033[m '))
    if cf == '1':
        sleep(0.3)
        space()
        print(f'{text_format["highlighted"]}{text_collor["green"]}'
              f'{ej(utility_symbols2['sucesso'])}  Dados salvos \033[m\n')
        return True
    else:
        sleep(0.3)
        space()
        print(f'{text_collor["yellow"]}{ej(utility_symbols1['alerta'])} Redigitar dados...\033[m\n')
        return False


# INSERÇÃO DE DADOS ACADÊMICOS 2.
def layout_input_academic_data2():
    print(f'{text_format["highlighted"]}{text_collor["white"]} {background_collors["gray"]} '
          f'{ej(academyEmojis["caneta"])}  FORNEÇA DADOS ACADÊMICOS SOBRE MATÉRIAS E NOTAS  {ej(academyEmojis["caneta"])}  \033[m\n')


# LOGO UX APÓS ENTRADA DE DADOS PRIMÁRIAS PARA MENU GERAL.
def logo_message_app():
    space()
    print(f'          {text_format[f'highlighted']}{background_collors['purple']}{text_collor['white']} {ej(techEmojis['computador'])} = '
          f'BIBLIOTECA INTELIGENTE = {ej(techEmojis['computador'])} {ej(academyEmojis['livro'])}{text_format["none"]}')
    print(f'          {text_format['highlighted']}{background_collors['white']} {ej(academyEmojis['ideia']) * 2}== == == == == == == == == '
          f'{ej(academyEmojis['ideia']) * 2}{text_format['none']}')
    print(f'          {text_format[f'highlighted']}{background_collors['white']}{text_collor['purple']}'
          f'   -SUA VIDA ACADÊMICA FACILITADA-  {text_format["none"]}')


# LSUB-MENU CRUD - FUNÇÕES ACADÊMICAS.
def submenu_crud_academy():
    space()
    print(f'     {background_collors['red']}{text_format["highlighted"]}{text_collor["white"]} {ej(academyEmojis['universidade'])}'
          f'{ej(utility_symbols1['linha_vertical'])}\033[m{background_collors['blue']}{text_format["highlighted"]}{text_collor["white"]} *  '
          f'ÁREA DO UNIVERSITÁRIO * {ej(utility_symbols1['bloco_solido'])} {text_format['none']}')

    print(f'{text_format['highlighted']}{text_collor['light_blue']}     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'   {background_collors['green']}{text_format["highlighted"]}{text_collor["white"]} NAVEGUE PELAS FUNCIONALIDADES ABAIXO {text_format["none"]}')
    space()


# SUB-MENU CRUD PARA DADOS DO USUÁRIO.
def submenu_crud_datauser():
    print(f'{background_collors['yellow']}{text_format["highlighted"]}{text_collor["white"]} {ej(utility_symbols1['usuario'])}{ej(utility_symbols1['linha_vertical'])}\033[m{background_collors['light_blue']}{text_format["highlighted"]}{text_collor["white"]} * ÁREA DE DADOS PESSOAIS * {ej(utility_symbols1['bloco_solido'])} {text_format["none"]}\n')

    print(
        f'    {background_collors['gray']}{text_format["highlighted"]}{text_collor["white"]} VISUALIZE, ALTERE DADOS {text_format["none"]}')
    space()
    

# DICIONÁRIO DE OPÇÕES GERAIS DO MENU PRINCIPAL.
dict_GeneralOptions = {'0': 'SAIR', '1': 'MEUS RELATÓRIOS ACADÊMICOS', '2': 'ÁREA DO USUÁRIO (DADOS PESSOAIS)', 
                       '3': 'GERENCIAR TAREFAS/AGENDAS', '4': 'SETOR BANCÁRIO DO ALUNO', '5': 'EMPRÉSTIMO DE LIVROS DA UNIVERSIDADE',
                       '6': 'EMPRÉSTIMO DE OUTROS ITENS'
                       }


# EXIBIR MENU GERAL COM TODAS AS OPÇÕES.
def display_menu_options():
    while True:
        print(f'{background_collors["gray"]}{text_format["highlighted"]}{text_collor["white"]} MENU PRINCIPAL - FERRAMENTAS E FUNCIONALIDADES -->\033[m\n')
        print(f'{text_format["highlighted"]}{background_collors["green"]} °EM QUE PODEMOS TE AJUDAR  {ej(utility_symbols2["ajuda"])}\033[m\n')

        options = str(input(f'{background_collors["blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO (0-{len(dict_GeneralOptions)-1}):\033[m '))
        if options == '0':
            space()
            sleep(0.3)
            print(f'{text_format["highlighted"]}{background_collors["red"]}{text_collor["white"]}ENCERRANDO SISTEMA...\033[m\n')
            break
        elif options == '1':
            return '1'
        elif options == '2':
            space()
            return '2'
        elif options == '3':
            return '3'
        elif options == '4':
            return '4'
        elif options == '5':
            return '5'
        elif options == '6':
            return '6'
        elif options not in dict_GeneralOptions:
            space()
            sleep(0.3)
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')



# Exibir todas as opções gerais.
def display_allgeneral_options():
    for k, v in dict_GeneralOptions.items():
        print(f'{text_format['highlighted']}{k}: {v}\033[m')
        sleep(0.15)
    space()


# LAYOUT DO SUBMENU TAREFAS.
def layout_submenu_tasks():
    print(f'{text_format["highlighted"]}{background_collors["red"]}{text_collor["yellow"]} {ej(utility_symbols2["calendario"])} '
          f'ÁREA DE GERENCIAMENTO DE TAREFAS/AGENDAS {ej(workEmojis["cronometro"])}  {text_format["none"]}\n'
          f'{text_format["highlighted"]}{text_collor["gray"]}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m\n'
          f' {background_collors["gray"]}{text_format["highlighted"]}{text_collor["yellow"]} Organize suas tarefas, provas e compromissos {text_format["none"]}\n')


# LAYOUT DO SUBMENU BANCÁRIO.
def layout_submenu_bank():
    print(f'{text_format["highlighted"]}{background_collors["green"]}{text_collor["white"]} {ej(financeEmojis["banco"])} '
          f'ÁREA DE GERENCIAMENTO BANCÁRIO {ej(financeEmojis["moedas"])}  {text_format["none"]}\n'
          f'{text_format["highlighted"]}{text_collor["white"]}--------------------------------------\033[m\n'
          f' {text_format["highlighted"]}{text_collor["white"]}Monitore sua conta bancária,\033[m\n{text_format["highlighted"]}{text_collor["white"]} planeje a compra de materiais\033[m\n {text_format["highlighted"]}{text_collor["white"]}de estudo e gerencie gastos acadêmicos. {text_format["none"]}\n')
    


# LAYOUT DO SUBMENU DE EMPRÉSTIMO DE LIVROS.
def layout_submenu_loan_books():
    space()
    print(f'{text_format["highlighted"]}{background_collors["light_blue"]}{text_collor["gray"]} {ej(academyEmojis["livro"])} '
          f'ÁREA DE EMPRÉSTIMO DE LIVROS {ej(emojisAcademy2["livro"])}  {text_format["none"]}\n'
          f'{text_format["highlighted"]}{text_collor["white"]}-------------------------------------\033[m\n'
          f' {text_format["highlighted"]}{text_collor["white"]}Gerencie o registro de empréstimo de\033[m\n{text_format["highlighted"]}{text_collor["white"]} livros realizados na sua universidade. {text_format["none"]}\n')
    space()


# LAYOUT SUBMENU EMPRÉSTIMOS SECUNDÁRIOS.
def layout_submenu_other_loans():
    space()
    print(f'{text_format["highlighted"]}{background_collors["gray"]}{text_collor["green"]} {ej(techEmojis["smartphone"])} '
          f'ÁREA DE EMPRÉSTIMO DE OUTROS ITENS {ej(techEmojis["computador"])}  {text_format["none"]}\n'
          f'{text_format["highlighted"]}{text_collor["white"]}------------------------------------------\033[m\n'
          f' {text_format["highlighted"]}{text_collor["white"]}Gerencie o registro de empréstimo de\033[m\n{text_format["highlighted"]}{text_collor["white"]} outros itens realizados na sua universidade. {text_format["none"]}\n')
    space()




# LAYOUT SISTEMA INTELIGENTE.
def smart_layout(title="Smart System", subtitle=""):
    # Título grande (pyfiglet)
    console = Console()
    ascii_title = figlet_format(title, font="slant")

    console.print(
        Panel.fit(
            Align.center(ascii_title),
            style="bold cyan",
            border_style="blue"
        )
    )

    if subtitle:
        console.print(
            Panel(
                f"📌 {subtitle}",
                style="bold white",
                border_style="cyan"
            )
        )

def display_smart_layout():
    smart_layout(
    title="Smart Library",
    subtitle="Sistema inteligente de gerenciamento de estudos, provas e \nquestões acadêmcas, focando em organização e eficiência."
)

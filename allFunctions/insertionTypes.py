
# MÓDULO PARA FUNÇÕES DE VALIDAÇÃO DE INPUT DE TIPOS PRIMITIVOS.
from emoji import emojize
from anscii_sistem.collors import text_collor, text_format



# PULAR ESPAÇO
def space():
    print()


# RETORNAR NÚMERO INTEIRO
def insertion_int(msg):
    while True:
        try:
            user_input_int = int(input(msg).strip())
            return user_input_int
        except ValueError:
            space()
            print(f'{text_collor["red"]}Erro, digite apenas numeros inteiros.{text_format["none"]}')
            space()


# FUNÇÃO PARA SEMPRE RETORNAR UM NÚMERO REAL.
def insertion_float(msg):
    while True:
        try:
            user_input_float = input(msg).strip()
            return float(user_input_float)
        except ValueError:
            space()
            print(f'{text_collor["red"]}Erro, digite apenas numeros reais.{text_format["none"]}')
            space()


# Evitar texto vazio.
def insertion_void(msg):
    while True:
        user_input_void = input(msg).strip()
        if user_input_void == '' or not user_input_void:
            space()
            print(f'{text_collor["red"]}Erro, o campo não pode ficar vazio.{text_format["none"]}\n')
        else:
            return user_input_void


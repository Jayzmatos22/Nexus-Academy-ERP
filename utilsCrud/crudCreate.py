# MÓDULO PARA CRIAÇÃO DE INFORMAÇÕES TANTO DE USUÁRIO COMO ACADÊMICAS.

from anscii_sistem.collors import text_collor, text_format, background_collors
from emojizeSistem.dict_emojize import utility_symbols1, utility_symbols2, emojisAcademy2, workEmojis
from allFunctions.insertionTypes import space, insertion_int, insertion_void
import time
from utils.utilsUx import ej
from allFunctions.user_data_var import tasks_created
from datetime import datetime
from utilsCrud.crudDataUser import check_required_params

# VALIDAR NOME DA TAREFA/ATIVIDADE CRIADA.
def validate_task_name():
    while True:
        # Limites.
        min_task = 5
        max_task = 25

        # condições de validação.
        task = input(f'{ej(emojisAcademy2["documentos"])}  NOME DA TAREFA/ATIVIDADE:\033[m ').strip().lower()
        if not task:
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} O nome da tarefa não pode estar vazio.\033[m\n')
            continue
        if len(task) < min_task:
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} O nome da tarefa deve ter pelo menos {min_task} caracteres.\033[m\n')
            continue
        if len(task) > max_task:
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} O nome da tarefa deve ter no máximo {max_task} caracteres.\033[m\n')
            continue
        if not task.replace(' ', '').isalpha():
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} O nome da tarefa deve conter apenas letras e espaços.\033[m\n')
            continue

        return task


# FORMATOS DE DATA E HORA.
FORMATED_DATE = "%d/%m/%Y"
FORMATED_HOUR = "%H:%M"



def validation_hour(prompt: str) -> time:
    """
    Solicita um horário (HH:MM) e o valida, retornando um objeto time.
    """
    while True:
        hour = input(prompt).strip()
        if not hour:
            space()
            print("❌ Erro! O horário não pode ser vazio. Tente novamente.")
            continue
            
        try:
            # Tenta converter para um objeto datetime
            date_hour_obj = datetime.strptime(hour, FORMATED_HOUR)
            # Retorna apenas a parte do horário (objeto time)
            return date_hour_obj.strftime(FORMATED_HOUR)
            
        except ValueError:
            space()
            print(f"❌ Erro! Formato inválido. Use o formato {FORMATED_HOUR} (Ex: 21:30)\n")
            continue



def validation_date(prompt: str) -> datetime | None:
    """
    Solicita a data/hora ao usuário e tenta convertê-la para um objeto datetime.
    Retorna o objeto datetime se for válido, ou None se for inválido.
    """
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            print("A data e o horário não podem ser vazios.")
            continue
            
        try:
            # Tenta converter a string para um objeto datetime usando o formato
            date_obj = datetime.strptime(date_str, FORMATED_DATE)
            return date_obj.strftime(FORMATED_DATE)
            
        except ValueError:
            # Captura o erro se a string não corresponder ao formato ou for inválida (ex: dia 32)
            space()
            print(f"❌ Erro! Formato inválido ou data inexistente. Use o formato DD/MM/AAAA HH:MM (Ex: {datetime.now().strftime(FORMATED_DATE)})\n")
            # Se a conversão falhou, o loop continua e pede novamente
            continue

range_importance_task = [0, 1, 2, 3, 4, 5]



# DICIONÁRIO PARA DESCRIÇÃO DO NÍVEL DE URGÊNCIA.
parameterized_urgency_description_to_display = {'0': 'facultativo', '1': 'muito baixo', '2': 'baixo', '3': 'normal', '4': 'alto', '5': 'muito alto'}
parameterized_urgency_description = {0: 'facultativo', 1: 'muito baixo', 2: 'baixo', 3: 'normal', 4: 'alto', 5: 'muito alto'}


# FUNÇÃO PARA OBTER A DESCRIÇÃO DA URGÊNCIA.
def get_urgency_description(level: int) -> str:
    return parameterized_urgency_description.get(level, None)



# FUNÇÃO PARA VALIDAR A URGÊNCIA DA TAREFA/ATIVIDADE EM NÍVEL NUMÉRICO.  DEPOIS USAR ESSA FUNÇÃO PARA OBTER A DESCRIÇÃO.
def urgency_of_the_task():
    while True:
        try:
            for key, value in parameterized_urgency_description_to_display.items():
                print(f'{text_format["highlighted"]}{background_collors["gray"]} {key} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{value}.\033[m')
            space()
            
            urgency = insertion_int(f'{ej(utility_symbols1["info"])}  NÍVEL DE URGÊNCIA DA TAREFA/ATIVIDADE (0-5):\033[m ')
            if urgency not in range_importance_task:
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Nível inválido. Escolha um número entre 0 e 5.\033[m\n')
                continue

            # Descrição da urgência.
            global urgency_description
            urgency_description = get_urgency_description(urgency)
            return urgency
        
        except ValueError:
            space()
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Entrada inválida. Por favor, insira um número entre 0 e 5.\033[m\n')



# FUNÇÃO PARA DESCRIÇÃO DA TAREFA/ATIVIDADE.
def description_of_task(d: str):
    while True:
        min_description = 10
        max_description = 100
        description = insertion_void(d).strip().lower()
        if len(description) < min_description:
            space()
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} A descrição da tarefa deve ter pelo menos {min_description} caracteres.\033[m\n')
            continue
        if len(description) > max_description:
            space()
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} A descrição da tarefa deve ter no máximo {max_description} caracteres.\033[m\n')
            continue

        return description
    


# FUNÇÃO PARA CRIAR UMA NOVA TAREFA/ATIVIDADE.
def create_new_task():

    while True:

        print(f'{background_collors["gray"]}{text_format["highlighted"]}{text_collor["white"]}{ej(emojisAcademy2["caneta"])} '
            f'{ej(utility_symbols1["linha_vertical"])}\033[m{background_collors["yellow"]} {text_format["highlighted"]}{text_collor["white"]} '
            f'- CRIAR NOVA TAREFA/ATIVIDADE - {ej(utility_symbols1["bloco_solido"])} {text_format["none"]}\n')
        
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 40}\033[m') 
        print(f'{text_format["highlighted"]}{text_collor["gray"]}Tenha sua própria agenda com lista de tarefas e horários que\nprecisa cumprir. Crie tarefas, para depois consultar.{text_format["none"]}')
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 40}\033[m\n')

        while True:
            task_name = validate_task_name()

            # Verificar se a tarefa já existe.
            for task in tasks_created.keys():
                if task_name.lower().strip() == task.lower().strip():
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Já existe uma tarefa com esse nome. Escolha outro nome.\033[m\n')
                    break
            else:
                break  # Sai do loop se a tarefa for válida e não existir.
                  

        # Ddados da tarefa.
        date = validation_date(f'{ej(workEmojis["calendario"])}  DATA DA TAREFA (DD/MM/AAAA):\033[m ')
        hour_time = validation_hour(f'{ej(workEmojis["cronometro"])}  HORÁRIO DA TAREFA (HH:MM):\033[m ')
        space()
        
        importance_level = urgency_of_the_task()
        description_task = description_of_task(f'{ej(emojisAcademy2["documentos"])}  DESCRIÇÃO DA TAREFA/ATIVIDADE:\033[m ')
        global urgency_description
        urgency_description = get_urgency_description(importance_level)
        tasks_created[task_name] = {'data tarefa': date, 'horário tarefa': hour_time, 'nível importância': importance_level, 'descrição importância': urgency_description, 'descrição tarefa': description_task}
            
        
        while True:
            space()
            create_another_task = input(f'{text_collor["yellow"]}{ej(workEmojis["marcador"])} DESEJA CRIAR OUTRA TAREFA/ATIVIDADE? (SIM/NÃO):\033[m ').strip().upper()
            if create_another_task == 'SIM':
                space()
                break
            elif create_another_task == 'NÃO' or create_another_task == 'NAO':
                space()
                return
            else:
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida. Digite "Sim" para prosseguir ou "Não" para rejeitar.\033[m\n')
                continue




# FUNÇÃO PARA LISTAR AS TAREFAS/ATIVIDADES CRIADAS.
def list_all_created_tasks():
    if not tasks_created:
        print(f'{text_collor["red"]}{ej(utility_symbols1["info"])} Nenhuma tarefa/atividade criada ainda.\033[m\n')
        return None
    else:
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 18}\033[m') 
        print(f'{text_format["highlighted"]}{text_collor["gray"]}Lista de Tarefas/Atividades Criadas:{text_format["none"]}')
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 18}\033[m\n')

        for task, details in tasks_created.items():
            # Exibir detalhes da tarefa.
            print(f'{text_format["highlighted"]}{text_collor["blue"]} Tarefa/Atividade: "{task}"\033[m')
            print(f'{ej(workEmojis["calendario"])} Data da Tarefa: {details["data tarefa"]}\033[m')
            print(f'{ej(workEmojis["cronometro"])}  Horário da Tarefa: {details["horário tarefa"]}\033[m')
            print(f'{ej(workEmojis["urgente"])} Nível de Importância: {details["nível importância"]}\033[m')
            print(f'{ej(workEmojis["prioridade"])} Descrição da Importância: {details["descrição importância"]}\033[m')
            print(f'{ej(emojisAcademy2["documentos"])} Descrição da Tarefa: {details["descrição tarefa"]}\033[m\n')



# QUANTIDADE DE TAREFAS/ATIVIDADES CRIADAS.
def total_tasks_created():
    total = len(tasks_created)
    if total:
        print(f'{text_format["highlighted"]}{text_collor["green"]}{ej(utility_symbols2["sucesso"])}  Total de Tarefas/Atividades Criadas: {total}\033[m\n')
        return total
    else:
        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Nenhuma tarefa/atividade criada ainda.\033[m\n')
        return False



# FUNÇÃO PARA DELETAR UMA TAREFA/ATIVIDADE.
def delete_task():
        while True:

            if tasks_created is None:
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Nenhuma tarefa/atividade criada ainda.\033[m\n')
                return

            # Exibir todas as tarefas criadas.
            # São exibidas para o usuário escolher qual deletar.
            # Somente nesse loop, pois se o user deletar uma tarefa, a lista será atualizada e pode dar erro se não haver mais tarefas.

            else:
                while True:
                    space()
                    print(f'{background_collors["gray"]}{text_format["highlighted"]}{text_collor["white"]}{ej(utility_symbols1["seta_retorno"])} '
                        f'{ej(utility_symbols1["linha_vertical"])}\033[m{background_collors["red"]} {text_format["highlighted"]}{text_collor["white"]} '
                        f'- DELETAR TAREFA/ATIVIDADE - ENTER "0" PARA SAIR {ej(utility_symbols1["bloco_solido"])} {text_format["none"]}\n')


                    # Verificar se há tarefas criadas após possível deleção.
                    if tasks_created:
                        for task, details in tasks_created.items():
                            print(f'{text_format["highlighted"]}{text_collor["blue"]} Tarefa/Atividade: "{task}"\033[m')
                            print(f'{ej(workEmojis["calendario"])} Data da Tarefa: {details["data tarefa"]}\033[m')
                            print(f'{ej(workEmojis["cronometro"])}  Horário da Tarefa: {details["horário tarefa"]}\033[m')
                            print(f'{ej(workEmojis["urgente"])} Nível de Importância: {details["nível importância"]}\033[m')
                            print(f'{ej(workEmojis["prioridade"])} Descrição da Importância: {details["descrição importância"]}\033[m')
                            print(f'{ej(emojisAcademy2["documentos"])} Descrição da Tarefa: {details["descrição tarefa"]}\033[m\n')

                    else:
                        print(f'{text_format["highlighted"]}{text_collor["white"]}Atualmente você não possui tarefas, crie uma.\033[m\n')
                        return # Sair da função se não houver tarefas.

                    # Evitar usuário ficar preso aqui por não ter tarefas criadas após deletar todas ou não lembrar.
                    task_name = input(f'{ej(workEmojis["critico"])}  DIGITE O NOME DA TAREFA/ATIVIDADE A SER DELETADA (<0> PARA SAIR):\033[m ').strip().lower()
                    if task_name == '0':
                        space()
                        print(f'{text_collor["yellow"]}{ej(utility_symbols1["info"])} Operação de exclusão cancelada pelo usuário.\033[m\n')
                        return
                    
                    # Verificar se a tarefa existe.
                    for task in tasks_created.keys():
                        if task_name.lower().strip() == task.lower().strip():
                            del tasks_created[task_name]
                            space()
                            print(f'{text_format["highlighted"]}{text_collor["green"]}{ej(utility_symbols2["sucesso"])}  Tarefa/Atividade "{task_name}" deletada com sucesso.\033[m\n')
                            break

                    else:
                        space()
                        print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Nenhuma tarefa/atividade encontrada com esse nome "{task_name}".\033[m\n')
                        break # Sai do loop para pedir o nome novamente.

                    # Perguntar se deseja deletar outra tarefa.
                    while True:
                        space()
                        delete_another_task = input(f'{text_collor["yellow"]}{ej(workEmojis["marcador"])} DESEJA DELETAR OUTRA TAREFA/ATIVIDADE? (SIM/NÃO):\033[m ').strip().upper()
                        if delete_another_task == 'SIM':
                            space()
                            break
                        elif delete_another_task == 'NÃO' or delete_another_task == 'NAO':
                            space()
                            return # Sai da função.
                        else:
                            space()
                            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida. Digite "Sim" para prosseguir ou "Não" para rejeitar.\033[m\n')
                            continue



# DICIONÁRIO PARA ATUALIZAÇÃO PARAMETRIZADA DA TAREFA/ATIVIDADE.                       
parameterized_update_task_dict = {
    '1': 'nome tarefa', '2': 'data tarefa', '3': 
    'horário tarefa', '4': 'nível importância', '5': 'descrição tarefa'
    }


# # PARA EXIBIR.
parameterized_update_task = [
    'nome tarefa', 'data tarefa', 
     'horário tarefa', 'nível importância', 'descrição tarefa' 
     ]


# DICIONÁRIO DE FUNÇÕES PARA ATUALIZAR A TAREFA/ATIVIDADE DE ACORDO COM A OPÇÃO.
get_function_to_update_task_dict = {
    'nome tarefa': validate_task_name,
    'data tarefa': validation_date,
    'horário tarefa': validation_hour,
    'nível importância': urgency_of_the_task,
    'descrição tarefa': description_of_task
}



# FUNÇÃO PARA ATUALIZAR UMA TAREFA/ATIVIDADE.
def update_task():
    while True:
        if not tasks_created:
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Nenhuma tarefa/atividade criada ainda.\033[m\n')
            return

        # Exibir todas as tarefas criadas.
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 18}\033[m') 
        print(f'{text_format["highlighted"]}{text_collor["gray"]}Lista de Tarefas/Atividades Criadas:{text_format["none"]}')
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 18}\033[m\n')

        # Exibir tarefas e suas descrições.
        for task, details in tasks_created.items():
            print(f'{text_format["highlighted"]}{text_collor["blue"]} Tarefa/Atividade: "{task}"\033[m')
            print(f'{ej(workEmojis["calendario"])} Data da Tarefa: {details["data tarefa"]}\033[m')
            print(f'{ej(workEmojis["cronometro"])}  Horário da Tarefa: {details["horário tarefa"]}\033[m')
            print(f'{ej(workEmojis["urgente"])} Nível de Importância: {details["nível importância"]}\033[m')
            print(f'{ej(workEmojis["prioridade"])} Descrição da Importância: {details["descrição importância"]}\033[m')
            print(f'{ej(emojisAcademy2["documentos"])} Descrição da Tarefa: {details["descrição tarefa"]}\033[m\n')


        # Solicitar ao usuário o nome da tarefa a ser atualizada.
        task_name = input(f'{ej(workEmojis["critico"])}  DIGITE O NOME DA TAREFA/ATIVIDADE A SER ATUALIZADA:\033[m ').strip().lower()
        for task in tasks_created.keys():
            if task_name == task.lower().strip():
                task_to_update = task       # GUARDA A STRING (Ex: "Matemática")
                get_task = tasks_created[task] # GUARDA OS DETALHES (Dicionário)
                break  

        else:
            space()
            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Nenhuma tarefa/atividade encontrada com esse nome "{task_name}".\033[m\n')
            continue
        space()

        # Exibir opções de atualização de descrições da tarefa.
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 20}\033[m') 
        print(f'{text_format["highlighted"]}{text_collor["gray"]}Opções de Atualização da Tarefa/Atividade:{text_format["none"]}')
        print(f'{text_format["highlighted"]}{text_collor["white"]}{"--" * 20}\033[m\n')

        for i, option in enumerate(parameterized_update_task, start=1):
            print(f'{text_format["highlighted"]}{background_collors["gray"]} {i} \033[m -> {text_format["highlighted"]}{text_collor["white"]}{option}.\033[m')
            time.sleep(0.2)

        while True:
            space()
            # Opção do usuário para atualizar.
            # Checagem de validade segundo o dicionário parametrizado.
            
            user_option = insertion_void(f'{background_collors["light_blue"]}{text_format["highlighted"]}{text_collor["white"]} ESCOLHA UMA OPÇÃO PARA ATUALIZAR (<0> SAIR):\033[m ').strip().lower()

            if user_option == '0': # sair.
                space()
                print(f'{text_collor["yellow"]}{ej(utility_symbols1["info"])} Operação de atualização cancelada pelo usuário.\033[m\n')
                return
            
            if user_option not in parameterized_update_task_dict.keys():
                space()
                print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Opção inválida, tente novamente.\033[m\n')
                continue

            get_description_task = parameterized_update_task_dict.get(user_option, None) # Ex: 'nome tarefa'
            get_function = get_function_to_update_task_dict.get(get_description_task, None) # Função correspondente.


            # CASO ESPECIAL 1.
            if get_description_task == 'nome tarefa':
                while True:
                    new_name_task = validate_task_name()
                    # Verificar se a nova tarefa já existe.
                    for task in tasks_created.keys():
                        if new_name_task.lower().strip() == task.lower().strip():
                            space()
                            print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])} Já existe uma tarefa com esse nome. Escolha outro nome.\033[m\n')
                            break
                    else:
                        tasks_created[new_name_task] = tasks_created.pop(task_to_update)
                        update_task = new_name_task # Atualiza a variável para o novo nome da tarefa.
                        for i, d in tasks_created.items():
                            print(i, d)
                        break  # Sai do loop se a tarefa for válida e não existir.

            # CASO ESPECIAL 2.
            elif get_description_task == 'nível importância':
                ts = update_task # Usar a variável correta para a tarefa a ser atualizada.
                new_level = urgency_of_the_task()
                tasks_created[ts][get_description_task] = new_level
                tasks_created[ts]['descrição importância'] = get_urgency_description(new_level)

            # Podemos aplicar o get_function diretamente.
            else:

                found_params = check_required_params(get_function)
                if found_params == 0:
                    task = ts # Variável que pode ter sido atualizada em 'nome tarefa'.
                    tasks_created[task][get_description_task] = get_function()
                    for i, d in tasks_created.items():
                            print(i, d)
                elif found_params == 1:
                    task = ts # Variável que pode ter sido atualizada em 'nome tarefa'.
                    tasks_created[task][get_description_task] = get_function(f'ATUALIZAR {get_description_task}:\033[m ')
                    for i, d in tasks_created.items():
                            print(i, d)
        


# Exibir opções.
dict_OptionsTasks_display = {'1': 'CRIAR NOVA TAREFA', '2': 'LISTAR MINHAS TAREFAS', 
                     '3': 'TOTAL DE TAREFAS CRIADAS', '4': 'DELETAR TAREFA', '5': 'ATUALIZAR TAREFA'}

# exibir submenu de criação de tarefas.
def display_submenu_tasks():
    for k, v in dict_OptionsTasks_display.items():
        print(f'{text_format['highlighted']}{background_collors['gray']} {k} \033[m -> {text_format['highlighted']}{text_collor['white']}{v}.\033[m') 
        time.sleep(0.15)
    space()

# Obter função da task.
dict_optionsTasks = {'CRIAR NOVA TAREFA': create_new_task, 'LISTAR MINHAS TAREFAS': list_all_created_tasks, 
                     'TOTAL DE TAREFAS CRIADAS': total_tasks_created, 'DELETAR TAREFA': delete_task, 'ATUALIZAR TAREFA': update_task}



# Obter função de tarefas.
def get_function_tasks():
    while True:
        try:
            space()
            display_submenu_tasks()
            space()
            user_option = input(f'{text_format['highlighted']}{background_collors["light_blue"]}ESCOLHA UMA OPÇÃO - TAREFAS (0: Sair / 1-{len(dict_OptionsTasks_display)}):\033[m ')

            if user_option == '0':
                space()
                time.sleep(0.3)
                print(f'{text_format["highlighted"]}{text_collor["yellow"]} {ej(utility_symbols2["seta_retorno"])}  Saindo de Tarefas...\033[m\n')
                return

            get_option = dict_OptionsTasks_display.get(user_option, None)
            if get_option is None:
                space()
                print(f'{ej(utility_symbols2['erro'])}  Opção inválida.\n')
                continue

            else:
                function = dict_optionsTasks.get(get_option, None)
                if function:
                    function()
                else:
                    print("Erro interno: Função não encontrada para esta opção.\n")
                    break

            while True: # Continuar ou parar.
                space()
                another_task = insertion_void(f'{text_format["invert"]}{text_collor["yellow"]} CONTINUAR EM TAREFAS? (1: SIM - 0: NÃO):\033[m ').strip()
                valid_response = ['1', '0']
                if another_task not in valid_response:
                    time.sleep(0.3)
                    space()
                    print(f'{text_collor["red"]}{ej(utility_symbols2["erro"])}  Opção inválida, tente novamente.\033[m\n')
                    continue

                elif another_task == '1':
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

            



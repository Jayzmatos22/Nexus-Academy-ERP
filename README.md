# 🎓 Sistema Integrado de Gestão Acadêmica e Financeira

Este é um ecossistema completo desenvolvido em Python para estudantes universitários, integrando gestão de notas, agenda de tarefas e um setor bancário simulado.

## 📊 Métricas do Projeto
O projeto destaca-se pela sua arquitetura modular e volume de lógica implementada:

* **Total de Funções (`def`):** 125
* **Total de Linhas de Código:** ~4.500
* **Arquivos Modulares:** 16 ficheiros `.py`



## 🛠️ Funcionalidades Principais

### 1. Gestão Académica 📚
- Cadastro de matérias para checagem.
- Ranking de produtividade e alertas de notas pendentes.
- Registo de empréstimos de livros com validação de ISBN.

### 2. Setor Bancário 💰
- Fluxo completo de depósitos, saques e planeamento de compras.
- **Data Science:** Uso de `Pandas` e `Numpy` para gerar estatísticas de gastos e histórico de transações.

### 3. Agenda de Tarefas (CRUD) 🗓️
- Sistema completo para Criar, Ler, Atualizar e Eliminar tarefas.
- Validação rigorosa de datas e status de atividades.

### 4. Interface e UX 🎨
- Interface de terminal rica com cores ANSI e emojis.
- Gráficos de tabelas gerados via `Matplotlib` para visualização de relatórios.



## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Bibliotecas:** Pandas, Matplotlib, Numpy, Pyfiglet, Colorama, Rich.


## 🚀 Como Usar

### 1. Pré-requisitos
Para rodar esse sistema de +4.500 linhas, você vai precisar do **Python 3.x** instalado e das seguintes bibliotecas:
* **Pandas**: Para o processamento de dados financeiros e estatísticas.
* **Numpy**: Para operações matemáticas do sistema.

### 2. Instalação
Clone o repositório e instale as dependências necessárias:

```bash
# Clonar o projeto
git clone [https://github.com/Jayzmatos22/Nexus-Academy-ERP](https://github.com/Jayzmatos22/Nexus-Academy-ERP)

# Entrar na pasta
cd Nexus-Academy-ERP

# Instalar bibliotecas necessárias
pip install pandas numpy
---bash


# 📂 Project Structure

```text
Nexus-Academy-ERP/
┃
┣━━ 📂 allFunctions/
┃   ┣━━ 📜 data_user_functions.py
┃   ┣━━ 📜 user_academy_functions.py
┃   ┣━━ 📜 user_data_var.py
┃   ┗━━ 📜 insertionTypes.py
┃
┣━━ 📂 anscii_sistem/
┃   ┗━━ 📜 collors.py
┃
┣━━ 📂 bankUser/
┃   ┣━━ 📜 functionBank.py
┃   ┗━━ 📜 variablesBank.py
┃
┣━━ 📂 emojizeSistem/
┃   ┗━━ 📜 dict_emojize.py
┃
┣━━ 📂 extensiveList_generies/
┃   ┗━━ 📜 listMaxGender.py
┃
┣━━ 📂 subjects_and_tasksAcademy/
┃   ┗━━ 📜 subjectTaskFunctions.py
┃
┣━━ 📂 utils/
┃   ┗━━ 📜 utilsUx.py
┃
┣━━ 📂 utilsCrud/
┃   ┣━━ 📜 crudCreate.py
┃   ┣━━ 📜 crudUniversity.py
┃   ┣━━ 📜 crudDataUser.py
┃   ┗━━ 📜 crudBankUser.py
┃
┣━━ 📜 main.py
┗━━ 📜 README.md                   
       
# ==== SKILLLINK ====
# 1. Cadastrar usuário
# 2. Editar usuário
# 3. Montar equipe
# 4. Recomendação de ReSkill
# 5. Listar usuários e habilidades
# 6. Sair

import random

usuarios = {
    "bernardo": {
        "idade": 22,
        "habilidades": ["Python", "SQL"],
        "nivel": "intermediario"
    },
    "amanda": {
        "idade": 28,
        "habilidades": ["JavaScript", "React", "Node.js"],
        "nivel": "avançado"
    },
    "carlos": {
        "idade": 19,
        "habilidades": ["HTML", "CSS"],
        "nivel": "basico"
    },
    "daniela": {
        "idade": 35,
        "habilidades": ["Java", "Spring", "Docker", "Kubernetes"],
        "nivel": "avançado"
    },
    "eduardo": {
        "idade": 24,
        "habilidades": ["Python", "Django", "PostgreSQL"],
        "nivel": "intermediario"
    },
    "fernanda": {
        "idade": 31,
        "habilidades": ["C#", ".NET", "Azure"],
        "nivel": "avançado"
    },
    "gabriel": {
        "idade": 20,
        "habilidades": ["Python", "Machine Learning"],
        "nivel": "basico"
    },
    "helena": {
        "idade": 27,
        "habilidades": ["PHP", "Laravel", "MySQL", "Vue.js"],
        "nivel": "intermediario"
    },
    "igor": {
        "idade": 33,
        "habilidades": ["Go", "Microservices", "Redis", "MongoDB"],
        "nivel": "avançado"
    }
}

equipes = {
    "Equipe DevOps": {
        "Integrantes": {
            "gabriel": {
                "idade": 20,
                "habilidades": ["Python", "Machine Learning"],
                "nivel": "basico"
            },
            "helena": {
                "idade": 27,
                "habilidades": ["PHP", "Laravel", "MySQL", "Vue.js"],
                "nivel": "intermediario"
            },
            "igor": {
                "idade": 33,
                "habilidades": ["Go", "Microservices", "Redis", "MongoDB"],
                "nivel": "avançado"
            }
        }
    }
}

cursos = [
    "Python para Iniciantes",
    "JavaScript Fundamentos",
    "Banco de Dados SQL",
    "React Avançado",
    "Docker para Desenvolvedores",
    "Machine Learning com Python",
    "Node.js e Express",
    "HTML e CSS Essencial"
]

def verifica_vazio(msg):
    mensagem = input(msg + "\n -> ")
    while len(mensagem) == 0:
        print("O campo não pode ficar vazio")
        mensagem = input(msg + "\n -> ")
    return mensagem

def verifica_input(msg, lista):
    mensagem = input(msg + "\n -> ")
    while mensagem.lower() not in lista:
        print(f"Apenas {', '.join(lista[:-1])} ou {lista[-1]} são permitidos")
        mensagem = input(msg + "\n -> ")
    return mensagem

def verifica_num(msg):
    mensagem = input(msg + "\n -> ")
    while not mensagem.isnumeric():
        print("Apenas números são permitidos")
        mensagem = input(msg + "\n -> ")
    return int(mensagem)

def printa_dic(dic):
    for d in dic.keys():
        print(f"---{d.upper()}---")
        for info, values in dic[d].items():
            print(f"{info} -> {values}")
        print("")

# FUNÇÃO CADASTRAR
def cadastro(servidor):
    nome = verifica_vazio("Qual o seu nome")
    servidor[nome] = {}
    servidor[nome]["idade"] = verifica_num("Qual sua idade")
    servidor[nome]["habilidades"] = verifica_vazio("Quais são suas habilidade").replace(",", "").split(" ")
    servidor[nome]["nivel"] = verifica_input("Qual seu nível (basico, intermediario, avançado)", ["basico", "intermediario", "avançado"])

# FUNÇÃO EDITAR
def editar(servidor):
    nome = verifica_input("Qual o nome do usuário que você quer editar", servidor.keys())
    for u in servidor[nome].keys():
        if verifica_input(f"Quer editar o(a) {u} (s/n)", ["s", "n"]) == "s":
            servidor[nome][u] = verifica_vazio(f"Qual(is) o(a) novo(a) {u}")

# FUNÇÃO MONTAR EQUIPE
def montar_equipe(servidor):
    candidatos = []
    finalistas = {}
    nome = verifica_vazio("Qual o nome da equipe")
    qtd = verifica_num("Quantas pessoas você quer na equipe")
    nivel = verifica_input("Qual seu nível você quer na equipe (basico, intermediario, avançado)", ["basico", "intermediario", "avançado"])
    habilidades = verifica_vazio("Quais habilidades você precisa na equipe")

    for users in servidor.keys():
        if (servidor[users]["nivel"]).lower() == nivel:
            candidatos.append(users)
        for h in servidor[users]["habilidades"]:
            if h.lower() == habilidades.lower():
                candidatos.append(users)
                break

    if len(candidatos) < qtd:
        print(f"Apenas {len(candidatos)} candidatos encontrados. Ajustando quantidade.")
        qtd = len(candidatos)

    random_candidatos = random.sample(list(candidatos), qtd)

    for r in random_candidatos:
        finalistas[r] = servidor[r]

    equipes[nome] = finalistas
    return equipes

# FUNÇÃO GERAR RECOMENDAÇÃO
def recomendacao(servidor):
    nome = verifica_input("Para qual usuário você quer a recomendação", list(servidor.keys()))
    resultado = random.sample(list(cursos), 1)
    if servidor[nome]["nivel"] == "basico":
        resultado = random.sample(list(cursos), 3)
    elif servidor[nome]["nivel"] == "intermediario":
        resultado = random.sample(list(cursos), 2)

    return resultado

# FUNÇÃO LISTAR USUÁRIOS
def listar_users(servidor):
    printa_dic(servidor)

def menu(lista):
    print(f" ==== SKILLLINK ==== \n 1. Cadastrar usuário \n 2. Editar usuário \n 3. Montar equipe \n 4. Recomendação de ReSkill \n 5. Listar usuários e habilidades \n 6. Sair \n")
    escolha = verifica_input("Qual opção você quer", lista)
    return escolha

actions = {
    "1" : cadastro,
    "2" : editar,
    "3" : montar_equipe,
    "4" : recomendacao,
    "5": listar_users,
    "6": "Sair"
}


while True:
    option = menu(list(actions.keys()))
    if option == "6":
        break
    actions[option](usuarios)
# ==== SKILLLINK ====
# 1. Cadastrar usuário
# 2. Editar usuário
# 3. Montar equipe
# 4. Recomendação de ReSkill
# 5. Listar usuários e habilidades
# 6. Sair
# 7.Simular IA de ReSkill
from idlelib.mainmenu import menudefs

usuarios = {
  "bernardo": {
      "idade": 22,
      "habilidades": ["Python", "SQL"],
      "nivel": "Intermediário"
  },
}

def verifica_vazio(msg):
    mensagem = input(msg + "\n -> ")
    while len(mensagem) == 0:
        print("O campo não pode ficar vazio")
        mensagem = input(msg + "\n -> ")
    return mensagem

def verifica_input(msg, lista):
    mensagem = input(msg + "\n -> ")
    while mensagem.lower() not in lista:
        print(f"Apenas {' ou '.join(lista)} são permitidos")
        mensagem = input(msg + "\n -> ")
    return mensagem


def verifica_num(msg):
    mensagem = input(msg + "\n -> ")
    while not mensagem.isnumeric():
        print("Apenas números são permitidos")
        mensagem = input(msg + "\n -> ")
    return int(mensagem)


def cadastro(servidor):
    nome = verifica_vazio("Qual o seu nome")
    servidor[nome] = {}
    servidor[nome]["idade"] = verifica_num("Qual sua idade")
    servidor[nome]["habilidades"] = verifica_vazio("Quais são suas habilidade").replace(",", "").split(" ")
    servidor[nome]["habilidades"] = verifica_input("Qual seu nível (basico, intermediario, avançado)", ["basico", "intermediario", "avançado"])

def editar(servidor):
    nome = verifica_input("Qual o nome do usuário que você quer editar", servidor.keys())
    for u in servidor[nome].keys():
        if verifica_input(f"Quer editar o(a) {u} (s/n)", ["s", "n"]) == "s":
            servidor[nome][u] = verifica_vazio(f"Qual(is) o(a) novo(a) {u}")


def montar_equipe(servidor):


# cadastro(usuarios)
editar(usuarios)
print(usuarios)
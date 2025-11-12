# 🧠 SkillLink - Sistema Python (Global Solution)

## 👥 Integrantes
- **Bruna Sadi Duarte** — RM 561870  
- **Sara Marangon de Macedo** — RM 563807  
- **Bernardo Moreira Lopes Sousa** — RM 564103  

📹 **Vídeo de Apresentação:** [https://youtu.be/_8hPssoNNEE](https://youtu.be/_8hPssoNNEE)  
💻 **Repositório GitHub:** [https://github.com/Bernardo07dev/Skill-Link-Python](https://github.com/Bernardo07dev/Skill-Link-Python)

---

## 🧩 Descrição do Projeto
O **SkillLink** foi desenvolvido como parte da **Global Solution 2025**, com o tema *“O Futuro do Trabalho”*.  
O sistema simula uma plataforma de **requalificação e montagem de equipes inteligentes**, construída em **Python** com foco em lógica estruturada e interação via terminal.

Seu diferencial está em permitir:
- Cadastro e edição de usuários.  
- Criação de equipes automáticas com base em habilidades.  
- Recomendações de cursos personalizados (*ReSkill*).  

---

## ⚙️ Principais Funcionalidades
- 🧾 Cadastro de usuários (com idade, habilidades e nível).  
- ✏️ Edição de perfis existentes.  
- 🤝 Montagem automática de equipes com base em habilidades.  
- 🎓 Recomendação de cursos personalizados.  
- 👥 Exibição de todos os usuários e equipes.  
- 🧩 Sistema de menu interativo com validação e tratamento de erros.

---

## 🧠 Estrutura do Código
- Uso de **dicionários** para armazenar dados de usuários e equipes.  
- **Funções** para modularizar o código e facilitar manutenção.  
- **Validações de entrada** (texto, números, opções válidas).  
- Uso da biblioteca **`random`** para gerar recomendações dinâmicas.  
- Aplicação de **laços e condicionais** para controle de fluxo do sistema.  

---

## 💻 Resumo do Código-Fonte

```python
import random

# Dicionário de usuários e equipes
usuarios = {...}
equipes = {...}

# Funções: cadastro, edição, montar equipe, recomendação, listagem
def cadastro(servidor): ...
def editar(servidor): ...
def montar_equipe(servidor): ...
def recomendacao(servidor): ...
def listar_users(servidor): ...
def mostrar_listas(servidor): ...

# Menu principal e loop de execução
while True:
    option = menu(list(actions.keys()))
    if option == "7":
        break
    actions[option](usuarios)

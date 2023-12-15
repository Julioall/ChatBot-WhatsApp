import random

'''#Descomente para testar a função
import mensagem'''

#Usado quando o sistema em execução  com o whatsApp
from src.model import mensagem


nivel_do_menu = ""
resposta_do_bot = ""

def exibir_menu(opcoes):
    return "\n".join(opcoes)

def criar_arquivo_de_nivel_de_menu():
    with open("nivel_do_menu.txt", "w") as arquivo:
        pass

def ler_nivel_do_menu_do_arquivo():
    try:
       
        with open("nivel_do_menu.txt", "r") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return ''

def processar_mensagem(resposta_cliente, nivel_do_menu):

    # Inicialização do menu
    if resposta_cliente and nivel_do_menu == "":
        resposta_do_bot = random.choice(mensagem.SAUDACAO)
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        nivel_do_menu = "menu principal"
        return nivel_do_menu, resposta_do_bot

    #Conhecer mais sobre a empresa
    #Opcao menu 
    if "conhecer mais sobre a empresa" in resposta_cliente or "1" in resposta_cliente and nivel_do_menu == "menu principal":
        resposta_do_bot = exibir_menu(
            list(mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA.keys()))
        nivel_do_menu = "conhecer mais sobre a empresa"
        return nivel_do_menu, resposta_do_bot

    #Sub-Opcao
    if "quem somos" in resposta_cliente or "1.1" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.1 - Quem somos"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    #Sub-Opcao
    if "nossos valores" in resposta_cliente or "1.2" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.2 - Nossos valores"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    #Sub-Opcao
    if "missao" in resposta_cliente or "1.3" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.3 - Missão"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL_ATUALIZADO
        return nivel_do_menu, resposta_do_bot

    #Sub-Opcao
    if "visao" in resposta_cliente or "1.4" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.4 - Visão"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL_ATUALIZADO
        return nivel_do_menu, resposta_do_bot

   #Voltar para o menu principal
    if "Voltar" in resposta_cliente or "0" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        nivel_do_menu = "menu principal"
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["0 - Voltar"]
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot




    # Dúvidas Frequentes
    #Opcao menu duvidas frequentes
    if "duvidas frequentes" in resposta_cliente or "2" in resposta_cliente and nivel_do_menu == "menu principal":
        resposta_do_bot = exibir_menu(list(mensagem.DUVIDAS_FREQUENTES.keys()))
        nivel_do_menu = "duvidas frequentes"
        return nivel_do_menu, resposta_do_bot

    #SubOpcao menu duvidas frequentes
    if "como funciona a energia solar" in resposta_cliente or "2.1" in resposta_cliente and nivel_do_menu == "duvidas frequentes":
        resposta_do_bot = mensagem.DUVIDAS_FREQUENTES["2.1 - Como funciona a energia solar?"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    #SubOpcao menu duvidas frequentes
    if "beneficios da energia solar" in resposta_cliente or "2.2" in resposta_cliente and nivel_do_menu == "duvidas frequentes":
        resposta_do_bot = mensagem.DUVIDAS_FREQUENTES["2.2 - Quais são os benefícios da energia solar?"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    #SubOpcao menu duvidas frequentes
    if "adquirir um sistema de energia solar" in resposta_cliente or "2.3" in resposta_cliente and nivel_do_menu == "duvidas frequentes":
        resposta_do_bot = mensagem.DUVIDAS_FREQUENTES["2.3 - Como posso adquirir um sistema de energia solar?"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot
    
    #Voltar para o menu principal
    if "Voltar" in resposta_cliente or "0" in resposta_cliente and nivel_do_menu == "duvidas frequentes":
        resposta_do_bot = mensagem.DUVIDAS_FREQUENTES["0 - Voltar"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot


    #Se o cliente mandar uma msg que não possa ser respondida.
    else:
        resposta_do_bot = "Não entendi. \n\nAqui estão algumas opções para você:\n\n"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        nivel_do_menu = "menu principal"
        return nivel_do_menu, resposta_do_bot

'''#Descomente para testar a função
# Exemplo de uso
while True:
    msg_cliente = input("Mensagem Cliente: ")
    nivel_do_menu, resposta = processar_mensagem(msg_cliente, nivel_do_menu)
    print(f"Resposta bot: \n{resposta}")'''

import random
import mensagem
nivel_do_menu = ""
resposta_do_bot = ""


def exibir_menu(opcoes):
    return "\n".join(opcoes)


def processar_mensagem(resposta_cliente, nivel_do_menu):
    # Inicialização do menu
    if resposta_cliente and nivel_do_menu == "":
        resposta_do_bot = random.choice(mensagem.SAUDACAO)
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        nivel_do_menu = "menu principal"
        return nivel_do_menu, resposta_do_bot





    # conhecer mais sobre a empresa
    if "conhecer mais sobre a empresa" in resposta_cliente or "1" in resposta_cliente and nivel_do_menu == "menu principal":
        resposta_do_bot = exibir_menu(
            list(mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA.keys()))
        nivel_do_menu = "conhecer mais sobre a empresa"
        return nivel_do_menu, resposta_do_bot

    if "quem somos" in resposta_cliente or "1.1"  in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.1 - Quem somos"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    if "nossos valores" in resposta_cliente or "1.2" in resposta_cliente and nivel_do_menu == "conhecer mais sobre a empresa":
        resposta_do_bot = mensagem.CONHECER_MAIS_SOBRE_A_EMPRESA["1.2 - Nossos valores"]
        nivel_do_menu = "menu principal"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        return nivel_do_menu, resposta_do_bot

    else:
        resposta_do_bot = "Não entendi. \n\nAqui estão algumas opções para você:\n\n"
        resposta_do_bot += mensagem.MENU_PRINCIPAL
        nivel_do_menu = "menu principal"
        return nivel_do_menu, resposta_do_bot


# Exemplo de uso
while True:
    msg_cliente = input("Mensagem Cliente: ")
    nivel_do_menu, resposta = processar_mensagem(msg_cliente, nivel_do_menu)
    print(f"Resposta bot: \n{resposta}")

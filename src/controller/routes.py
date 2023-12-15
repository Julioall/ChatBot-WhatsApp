from flask import Flask, request
from src.model.whatsapp import WhatsApp
from src.model.respostas import processar_mensagem,criar_arquivo_de_nivel_de_menu,ler_nivel_do_menu_do_arquivo
import src.model.mensagem

app = Flask(__name__)
meu_bot = WhatsApp()
meu_bot.conectar()

criar_arquivo_de_nivel_de_menu()

@app.route('/home', methods=['POST'])
def home():

    # Ler msg do cliente
    resposta_cliente = request.form['Body'].lower()

    # Recuperar o nível do menu do arquivo
    nivel_do_menu = ler_nivel_do_menu_do_arquivo()

    # Processando a msg do client e gerando a resposta
    nivel_do_menu, resposta_do_bot = processar_mensagem(resposta_cliente, nivel_do_menu)
    
    #Enviando a resposta para o cliente
    meu_bot.enviar_mensagem(resposta_do_bot)

    # Salvar o nível do menu no arquivo
    with open("nivel_do_menu.txt", "w") as arquivo:
        arquivo.write(nivel_do_menu)

    return ""  

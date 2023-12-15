from flask import Flask, request
from src.model.whatsapp import WhatsApp
from src.model.mensagem import ProcessadorDeMensagens

app = Flask(__name__)
meu_bot = WhatsApp()
mensagem = ProcessadorDeMensagens()
meu_bot.conectar()
@app.route('/home', methods=['POST'])
def home():
    resposta_cliente = request.form['Body'].lower()
    if resposta_cliente():
        mensagem.processar_informacoes_contato(resposta_cliente)
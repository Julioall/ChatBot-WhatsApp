# Sistema de Atendimento Virtual

Bem-vindo ao Sistema de Atendimento Virtual desenvolvido em Flask para interação com o WhatsApp.

## Configuração

1. **Clonar o repositório:**
```bash
   git clone https://github.com/Julioall/solutions-energy-bot-main/
   cd sua-repo
```
2. **Configurar o Ambiente Virtual:**
```bash
python -m venv venv
source venv/bin/activate   # No Windows use `venv\Scripts\activate`
```
4. **Instalar as Dependências:**
```bash
    pip install -r requirements.txt
```
5. Configurar as Credenciais do WhatsApp:
Insira suas credenciais do WhatsApp no arquivo src/model/whatsapp.py.

6. Executar o Aplicativo:
```bash
python run.py
```

## Acessar o Sistema:
O sistema estará disponível em http://127.0.0.1:5000.

## Uso
O sistema oferece um atendimento virtual interativo via WhatsApp.
Os níveis do menu são salvos e lidos a partir do arquivo nivel_do_menu.txt.
Personalize as mensagens e as respostas no arquivo src/model/mensagem.py.
Contribuições
Sinta-se à vontade para contribuir para o desenvolvimento do sistema. Faça um fork do repositório, crie uma branch, faça suas alterações e envie um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

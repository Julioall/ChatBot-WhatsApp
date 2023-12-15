from src.controller.routes import app



'''
import ptvsd
#Iniciar com debug do VSCode
ptvsd.enable_attach(address=('localhost', 5000), redirect_output=True)
app.run(debug=True, host="0.0.0.0", port=5000)'''


#Iniciar para produção
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

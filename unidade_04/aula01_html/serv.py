from flask import Flask
from pyngrok import ngrok


# Criando a aplicação Flask
app = Flask(__name__)


# Criando a rota principal
@app.route("/")
def index():
    return "Olá, esta é a rota principal do back-end!"


# Executando o servidor
if __name__ == "__main__":

    # Inicia o servidor Flask na porta 5000
    port = 5000

    # Cria um túnel público através do ngrok
    public_url = ngrok.connect(port)

    print("URL pública:", public_url)

    # Inicia o Flask
    app.run(port=port)
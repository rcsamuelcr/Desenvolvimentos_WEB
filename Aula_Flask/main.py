from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Configuração do BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'


db = SQLAlchemy(app)

# Modelo do Banco
class Estudante(db.Model):
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primeiro_nome   = db.Column(db.String(150), nullable=False)
    ultimo_nome     = db.Column(db.String(150), nullable=False)
    idade           = db.Column(db.Integer, nullable=False)

# Crição da tabela dentro do app context
with app.app_context():
        db.create_all()         #Todas as tabelas (Estudante)


@app.route("/")
def home():
    estudantes = Estudante.query.all()
    return render_template('index.html', estudantes=estudantes)

@app.route("/add", methods=["GET", "POST"]) # Indica que a rota aceita dois tipos de requisição: 
                                            # GET: Utilizado para recuperar dados e carregar páginas (como exibir um formulário), enviando informações pela URL.
                                            # POST: Usado para enviar dados ao servidor para processamento ou criação (como submeter formulários ou criar usuários), 
                                            # ocultando os dados no corpo da requisição, ideal para segurança e grandes quantidades de dados. 
def add():
    if request.method == "POST":    # Se o método da requisição for POST, é usado para acessar dados de solicitações HTTP (GET/POST) em funções de visualização.
        primeiro_nome = request.form.get("primeiro_nome")   # Captura o valor do formulário e armazena em uma variável
        ultimo_nome   = request.form.get("ultimo_nome")
        idade         = request.form.get("idade")

        if primeiro_nome and ultimo_nome and idade:  # Realiza uma validação simples de presença de dados antes de tentar salvar as informações no banco de dados.
            e = Estudante(
                primeiro_nome = primeiro_nome,
                ultimo_nome   = ultimo_nome,
                idade         = int(idade)
            )
            db.session.add(e)
            db.session.commit()
            return redirect("/") # Redireciona para a rota "/" após salvar

    return render_template('add.html')

if __name__ == ('__main__'):
    app.run(debug=True)





























# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     variavel_nome = "Samuel"
#     is_admin = True
#     return render_template('index.html', nome=variavel_nome, admin=is_admin)

# if __name__ == '__main__':
#     app.run(debug=True)


# <!DOCTYPE html>
# <html>
# <head>
#     <title>Minha Página</title>
# </head>
# <body>
#     <h1>Olá, {{ nome }}!</h1>
#     {% if admin %}
#         <p>Você é um administrador.</p>
#     {% else %}
#         <p>Você é um usuário comum.</p>
#     {% endif %}
# </body>
# </html>

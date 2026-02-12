from flask import Flask, render_template
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

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

db = SQLAlchemy(app)

# Modelo do banco
class Estudante(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primeiro_nome = db.Column(db.String(150), nullable=False)
    ultimo_nome = db.Column(db.String(150), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

# Criação da tabela dentro do app context
with app.app_context():
    db.create_all()                             # cria a tabela estudante

# Rota principal
@app.route("/")
def index():
    estudantes = Estudante.query.all()
    return render_template("index.html", estudantes=estudantes)

# Rota para adicionar estudante
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        primeiro_nome = request.form.get("primeiro_nome")
        ultimo_nome   = request.form.get("ultimo_nome")
        idade         = request.form.get("idade")

        if primeiro_nome and ultimo_nome and idade:
            e = Estudante(
                primeiro_nome = primeiro_nome, 
                ultimo_nome   = ultimo_nome, 
                idade         = int(idade)
            )
            db.session.add(e)
            db.session.commit()
            return redirect("/")
        
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    estudante = Estudante.query.get_or_404(id)  # Busca o estudante pelo ID ou dá 404
    
    if request.method == "POST":
        # Atualiza os dados com os valores do formulário
        estudante.primeiro_nome = request.form.get("primeiro_nome")
        estudante.ultimo_nome   = request.form.get("ultimo_nome")
        estudante.idade         = int(request.form.get("idade"))

        db.session.commit()                     # Salva no banco
        return redirect("/")                    # Redireciona para a página principal

    # Se for GET, mostra o formulário com os dados preenchidos
    return render_template("edit.html", estudante=estudante)

@app.route("/delete/<int:id>")
def delete(id):
    estudante = Estudante.query.get_or_404(id)  # Busca o estudante pelo ID ou retorna 404
    db.session.delete(estudante)                # Deleta o registro
    db.session.commit()                         # Confirma a alteração no banco
    return redirect("/")                        # Redireciona para a página principal

if __name__ == "__main__":
    app.run(debug=True)
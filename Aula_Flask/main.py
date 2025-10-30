from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


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

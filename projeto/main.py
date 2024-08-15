from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Inicializa a lista de filmes com dicionários
filmes = [
    {'codigo': 1, 'titulo': 'Oppenheimer', 'genero': 'Suspense', 'ano': 2023},
    {'codigo': 2, 'titulo': 'Deadpool & Wolverine', 'genero': 'Ação', 'ano': 2024},
    {'codigo': 3, 'titulo': 'Titanic', 'genero': 'Romance', 'ano': 1997}
]

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/apagar_filme/<int:codigo>', methods=['GET', 'POST'])
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome_filme = request.form['nome_filme']
        genero = request.form['genero']
        ano = int(request.form['ano'])
        codigo = len(filmes) + 1  # Gera um novo código
        filmes.append({'codigo': codigo, 'titulo': nome_filme, 'genero': genero, 'ano': ano})
        return redirect('/')
    return render_template('adicionar_filme.html')  # Certifique-se de ter um template para isso

@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    if request.method == 'POST':
        nome_filme = request.form['nome_filme']
        genero = request.form['genero']
        ano = int(request.form['ano'])
        for filme in filmes:
            if filme['codigo'] == codigo:
                filme['titulo'] = nome_filme
                filme['genero'] = genero
                filme['ano'] = ano
                break
        return redirect('/')
    filme = filmes[codigo]
    return render_template('editar_filme.html', filme=filme)  # Certifique-se de ter um template para isso

if __name__ == '__main__':
    app.run(debug=True)

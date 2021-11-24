from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

funcionarios = [
    {'nome': 'Matheus Oba','salario': 'R$ 5500'},
    {'nome': 'Moises Corrêa','salario': 'R$ 22000'},
    {'nome': 'Josué de Almeida','salario': 'R$ 11000'},
    {'nome': 'João Cleber Filho','salario': 'R$ 569'},
]

@app.route('/')
def index():
    return render_template('index.html', lista=funcionarios)

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    pesquisa = request.form['pesquisa']
    lista_pesquisa_funcionarios = []
    if pesquisa > '':
        for funcionario in funcionarios:
            if pesquisa.upper() in funcionario['nome'].upper():
                lista_pesquisa_funcionarios.append(funcionario)
        return render_template('pesquisa.html', lista_pesquisa_funcionarios=lista_pesquisa_funcionarios)      

    return render_template('erro.html')

@app.route('/deletar', methods=['POST'])
def deletar():
    delete = request.form['delete']
    if delete > '':
        delete = int(delete)
        if delete <= len(funcionarios) and delete > 0 and delete != None: 
            del funcionarios[delete-1]
            return redirect('https://5000-emerald-cougar-e8goxv34.ws-us17.gitpod.io/')

    return render_template('erro.html')

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    salario = request.form['salario']
    funcionario = {'nome': nome, 'salario': 'R$ ' + salario}
    if nome > '' and salario > '':
        funcionarios.append(funcionario)
        return redirect('https://5000-emerald-cougar-e8goxv34.ws-us17.gitpod.io/')

    return render_template('erro.html')

app.run(debug=True)
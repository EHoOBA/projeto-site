from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

funcionarios = [
    {'nome': 'Matheus o OBA','salario': 'R$ 5000'},
    {'nome': 'Moises o CORREA','salario': 'R$ 22000'},
    {'nome': 'Jonathan o GARCIA','salario': 'R$ 12000'},
    {'nome': 'Lucas o RODRIGO','salario': 'R$ 569'},
]

@app.route('/')
def index():
    return render_template('index.html', lista=funcionarios)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/deletar', methods=['POST'])
def deletar():
    delete = request.form['delete']
    if delete > '':
        delete = int(delete)
        if delete <= len(funcionarios) and delete > 0 and delete != None: 
            del funcionarios[delete-1]
            return redirect('https://5000-purple-prawn-2mkzutd3.ws-us18.gitpod.io/')

    return render_template('erro.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    salario = request.form['salario']
    funcionario = {'nome': nome, 'salario': 'R$ ' + salario}
    funcionarios.append(funcionario)

    return redirect('https://5000-chocolate-crocodile-1x66zhrm.ws-us18.gitpod.io')

app.run(debug=True)
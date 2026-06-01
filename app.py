from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_alertas'

# Configurações de conexão com o seu MySQL local
db_config = {
    'host': 'localhost',
    'user': 'root',       
    'password': 'fatec',  
    'database': 'nova_aurora_db'
}

def salvar_no_banco(tabela, nome, cpf, telefone, email):
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
     
        sql = f"INSERT INTO {tabela} (nome_completo, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
        valores = (nome, cpf, telefone, email)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        cursor.close()
        conexao.close()
        return True
    except mysql.connector.Error as err:
        print(f"Erro no banco de dados: {err}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('Contato.html')

@app.route('/inscricao', methods=['GET', 'POST'])
def srcricao():
    if request.method == 'POST':
        nome = request.form.get('nome_completo')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        curso = request.form.get('curso')

        tabelas_cursos = {
            'ads': 'inscritos_ads',
            'eng': 'inscritos_engenharia',
            'adm': 'inscritos_administracao',
            'mkt': 'inscritos_marketing'
        }

        tabela_destino = tabelas_cursos.get(curso)

        if tabela_destino:
            sucesso = salvar_no_banco(tabela_destino, nome, cpf, telefone, email)
            if sucesso:
                return render_template('sucesso.html')
            else:
                return render_template('erro.html')
        else:
            return "<h1>Selecione um curso válido.</h1><br><a href='/inscricao'>Voltar</a>"

    return render_template('inscricao.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        cpf = request.form.get('cpf')

        tabelas = ['inscritos_ads', 'inscritos_engenharia', 'inscritos_administracao', 'inscritos_marketing']
        usuario_encontrado = None

        try:

            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="fatec",
                database="nova_aurora_db"
            )
            cursor = conexao.cursor(dictionary=True)

            for tabela in tabelas:
                query = f"SELECT nome_completo, email, cpf FROM {tabela} WHERE email = %s AND cpf = %s"
                cursor.execute(query, (email, cpf))
                resultado = cursor.fetchone()
                
                if resultado:
                    usuario_encontrado = resultado
                    break 

            cursor.close()
            conexao.close()

            if usuario_encontrado:
                session['usuario_id'] = usuario_encontrado['cpf']
                session['usuario_nome'] = usuario_encontrado['nome_completo']
                return redirect('/')
            else:
                return render_template('login.html', erro="Candidato não encontrado. Verifique o E-mail e o CPF.")

        except mysql.connector.Error as err:
            return render_template('login.html', erro="Erro de conexão com o banco de dados.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
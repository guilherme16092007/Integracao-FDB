from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_alertas'

# Configurações de conexão com o seu MySQL local
db_config = {
    'host': 'localhost',
    'user': 'root',       
    'password': 'guilherme',  
    'database': 'nova_aurora_db'
}

def salvar_no_banco(tabela, nome, cpf, telefone, email):
    """Função auxiliar para conectar e inserir os dados na tabela correta"""
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        
        # Comando SQL dinâmico baseado na tabela do curso escolhido
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

# Rota da página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota da página Sobre Nós
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota da página de Contato
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
                # ALTERADO AQUI: Caso dê erro (como CPF duplicado), abre a tela de erro estilizada!
                return render_template('erro.html')
        else:
            return "<h1>Selecione um curso válido.</h1><br><a href='/inscricao'>Voltar</a>"

    return render_template('inscricao.html')

if __name__ == '__main__':
    app.run(debug=True)
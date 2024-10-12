from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html')  # Modificado para index.html

# Rota para exibir a lista de clientes
@app.route('/clientes')
def clientes():
    conn = get_db_connection()
    clientes = conn.execute('SELECT * FROM clientes').fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

# Rota para adicionar um novo cliente
@app.route('/add_cliente', methods=('GET', 'POST'))
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        empresa = request.form['empresa']
        conn = get_db_connection()
        conn.execute('INSERT INTO clientes (nome, empresa) VALUES (?, ?)', (nome, empresa))
        conn.commit()
        conn.close()
        return redirect(url_for('clientes'))
    return render_template('add_cliente.html')

# Rota para deletar um cliente
@app.route('/delete_cliente/<int:id>', methods=('POST',))
def delete_cliente(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('clientes'))

# Inicializando o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)

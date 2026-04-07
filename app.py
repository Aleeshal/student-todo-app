from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('todos.db')
    conn.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('todos.db')
    todos = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect('todos.db')
    conn.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('todos.db')
    conn.execute('DELETE FROM todos WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_FILE = "workouts.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sets INTEGER,
            reps INTEGER,
            date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercises', methods=['GET'])
def get_exercises():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT id, name, sets, reps, date FROM exercises ORDER BY date DESC')
    exercises = c.fetchall()
    conn.close()
    return jsonify(exercises)

@app.route('/add', methods=['POST'])
def add_exercise():
    data = request.get_json()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO exercises (name, sets, reps) VALUES (?, ?, ?)',
              (data['name'], data['sets'], data['reps']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM exercises WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

@app.route('/update/<int:id>', methods=['PUT'])
def update_exercise(id):
    data = request.get_json()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE exercises SET name = ?, sets = ?, reps = ? WHERE id = ?',
              (data['name'], data['sets'], data['reps'], id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'updated'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

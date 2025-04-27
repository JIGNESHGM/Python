from flask import Flask, render_template, request, redirect, url_for, send_file
import joblib
import sqlite3
from datetime import datetime
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# Load ML model
model = joblib.load('model/model.pkl')

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS applications
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  income REAL,
                  credit_score INTEGER,
                  employment TEXT,
                  debt REAL,
                  age INTEGER,
                  prediction REAL,
                  approved INTEGER,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    
    features = [
        float(data['income']),
        int(data['credit_score']),
        float(data['debt']),
        int(data['age']),
        1 if data['employment'] == 'employed' else 0
    ]
    
    probability = model.predict_proba([features])[0][1]
    approved = probability > 0.7
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO applications 
                 (name, income, credit_score, employment, debt, age, prediction, approved, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (data['name'], float(data['income']), int(data['credit_score']),
               data['employment'], float(data['debt']), int(data['age']),
               float(probability), int(approved), datetime.now()))
    conn.commit()
    conn.close()
    
    return render_template('result.html', 
                         approved=approved,
                         probability=round(probability*100, 2))

@app.route('/admin')
def admin():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM applications ORDER BY timestamp DESC')
    applications = c.fetchall()
    conn.close()
    return render_template('admin.html', applications=applications)

@app.route('/export')
def export():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM applications", conn)
    conn.close()
    
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    
    return send_file(output, mimetype='text/csv',
                     as_attachment=True,
                     download_name='credit_applications.csv')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
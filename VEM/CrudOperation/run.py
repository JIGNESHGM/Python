from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
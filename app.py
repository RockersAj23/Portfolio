# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print('doctor strange')
    count()
    return 'Hello, this is your Flask backend!'
@app.route('/ajay2')
def count():
    return str(4)

if __name__ == '__main__':
    app.run(debug=True)


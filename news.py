import os
from flask import Flask, render_template, request
import webbrowser
import threading


app = Flask(__name__, template_folder=r'C:\Users\Ajay Mulgir\portfolio project\Portfolio')
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/submit', methods=['POST'])
def submit():
    key = request.form['key']
    text = request.form['text']
    directory = r"C:\Users\Ajay Mulgir\OneDrive\Desktop\WORK\news"
    append_text_to_file(key, text, directory)
    return 'Text appended successfully!'

def append_text_to_file(key, text, directory):
    filename = os.path.join(directory, f"{key}.txt")
    with open(filename, "a") as file:
        file.write(text + "\n")

def open_browser():
    webbrowser.open_new_tab('http://127.0.0.1:5000')



if __name__ == '__main__':
    threading.Timer(1,open_browser).start()
    app.run(debug=True)



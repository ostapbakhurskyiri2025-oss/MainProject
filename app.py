from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HTML.html') # Flask сам шукає цей файл у папці templates

if __name__ == '__main__':
    app.run(debug=True)
    
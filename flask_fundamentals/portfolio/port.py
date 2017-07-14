from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def port():
    return render_template('folio.html')

@app.route('/projects')

def pro():
    return render_template('proj.html')

@app.route('/about')

def me():
    return render_template('about.html')

app.run(debug = True)

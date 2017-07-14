from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')

def word():
    return render_template('word.html')
app.run(debug=True)
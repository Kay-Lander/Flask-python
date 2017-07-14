from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSercet"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter']+=1
    else:
        session['counter']=1
    return render_template('index.html')



@app.route('/counter')
def users():
    session['counter']+=1

    return redirect('/')

@app.route('/reset')
def hacker():
    session['counter']=0

    return redirect('/')

app.run(debug=True)

  
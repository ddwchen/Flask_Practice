from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secretcode923498902'
import random

@app.route('/')
def index():
    if "gold" not in session:
        session['gold']=0
        print("it's working!")
    if "randint" not in session:
        session['randint']=0
        print("it's really working!")
    return render_template('index.html')

@app.route('/find_gold', methods=['POST'])
def find_gold():
    if request.form['property'] == 'farm':
        session['randint'] = random.randint(10,20)
        session['gold'] += session['randint']
    elif request.form['property'] == 'cave':
        session['randint'] = random.randint(5,10)
        session['gold'] += session['randint']
    elif request.form['property'] == 'house':
        session['randint'] = random.randint(2,5)
        session['gold'] += session['randint']
    elif request.form['property'] == 'casino':
        session['randint'] = random.randint(-50,50)
        session['gold'] += session['randint']
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['gold']=0
    print("working")
    session['randint']=0
    print("still working")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
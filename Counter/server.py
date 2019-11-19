from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
app.count=0

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session(): 
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

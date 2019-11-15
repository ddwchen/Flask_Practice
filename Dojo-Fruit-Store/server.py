from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def create_user():
    print("Get Post Info")
    print(request.form)
    strawberries_from_form = request.form['strawberry']
    raspberries_from_form = request.form['raspberry']
    apples_from_form = request.form['apple']
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    return render_template("checkout.html", strawberries_on_template=strawberries_from_form, raspberries_on_template=raspberries_from_form, apples_on_template=apples_from_form, first_name_on_template=first_name_from_form, last_name_on_template=last_name_from_form, student_id_on_template=student_id_from_form) 

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__ == "__main__":
    app.run(debug=True)


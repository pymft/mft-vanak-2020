from flask import Flask, render_template


app = Flask('my app')


@app.route('/')
def index():
    return "<h1>Welcome to Main Page</h1>"


@app.route('/images/<int:number>')
def images(number=1):
    return f"Images No. {number}"


@app.route('/table/<int:rows>/<int:cols>')
def table(rows, cols):
    return render_template('table.html', rows=rows, cols=cols)


@app.route('/bmi/<int:weight>/<int:height>')
def calculate_bmi(weight, height):
    height = height/100
    value = weight / ( height * height)

    if value > 25:
        message = "over weight"
    elif value < 18:
        message = "under weight"
    else:
        message = "Normal"

    return f"<h1>{value}<h1> <h2>{message}</h2>"


app.run(host="0.0.0.0", debug=True)

from flask import Flask, render_template


app = Flask('my app')

@app.route('/')
def index():
    persons = [
        ["John", "Smith", 35],
        ["Jack", "Whatever", 30]
    ]
    return render_template("./index.html", persons=persons)



app.run(debug=True)
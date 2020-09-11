from flask import Flask, render_template, request, redirect


app = Flask('my app')


@app.route('/')
def index():
    # persons = [
    #     ["John", "Smith", 35],
    #     ["Jack", "Whatever", 30]
    # ]
    persons = []
    with open('./people.txt') as f:
        text = f.read()

    for line in text.split('\n'):
        temp = line.split(",")
        persons.append(temp)

    return render_template("./index.html", persons=persons)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("./register.html")
    else:
        with open('./people.txt', 'a') as f:
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            age = request.form["age"]

            f.write(f"\n{first_name},{last_name},{age}")
        return redirect("/")


@app.route('/bmi', methods=["GET", "POST"])
def bmi():
    if request.method == "POST":
        weight = request.form["weight"]
        height = request.form["height"]
        weight = float(weight)
        height = float(height)
        bmi_answer = weight / (height * height)
        answer = f"{bmi_answer:0.2f}"
    else:
        answer = ""

    return render_template("./bmi.html", answer=answer)

app.run(debug=True)
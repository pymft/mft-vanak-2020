from flask import Flask

app = Flask('app')

@app.route('/user')
def index():
    return "Hello User"

@app.route('/new')
def new_fun():
    return "new"


app.run()
from flask import Flask


app = Flask('my app')


@app.route('/')
def index():
    return "<h1>Welcome to Main Page</h1>"


@app.route('/images')
def images():
    return """
    <h1>Images</h1>
    <h2>sub section</h2>
    <p>text text text text text text text </p>
    """


app.run(host="0.0.0.0")
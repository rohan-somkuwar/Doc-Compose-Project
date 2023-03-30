from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    name = request.args.get('name', 'world')
    return f'<h1>Hell, {name}!</h1>\n<p>Welcome to the website.</p>'

app.run(host='localhost', port=8000)
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    name = request.args.get('name', 'Website')
    return f'<h1>Rohan, {name}!</h1>\n<p>Thankyou for visit to the website.</p>'

app.run(host='localhost', port=8000)

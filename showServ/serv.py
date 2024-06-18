from flask import Flask, render_template, request

app = Flask(__name__)

list = {"waiting":0}

@app.route('/')
def index():
    return render_template('index.html.jinja', list=list)

@app.route('/update', methods=['POST'])
def update():
    global list
    list = request.get_json()
    return 'Success'
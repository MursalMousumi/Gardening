from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)#, template_folder='templates', static_folder='static')
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('my_template.html')

@app.route('/regions', methods=['GET'])
def regions():
    return render_template('regions.html')

@app.route('/zone1', methods=['GET'])
def zone1():
    return render_template('zone1.html')

@app.route('/zone2', methods=['GET'])
def zone2():
    return render_template('zone2.html')

@app.route('/zone3', methods=['GET'])
def zone3():
    return render_template('zone3.html')

@app.route('/zone4', methods=['GET'])
def zone4():
    return render_template('zone4.html')

@app.route('/lettuce', methods=['GET'])
def lettuce():
    return render_template('lettuce.html')

@app.route('/broccoli', methods=['GET'])
def broccoli():
    return render_template('broccoli.html')

@app.route('/beans', methods=['GET'])
def beans():
    return render_template('beans.html')

@app.route('/tomato', methods=['GET'])
def tomato():
    return render_template('tomato.html')

@app.route('/chokecherry', methods=['GET'])
def chokecherry():
    return render_template('chokecherry.html')

@app.route('/carrot', methods=['GET'])
def carrot():
    return render_template('carrot.html')
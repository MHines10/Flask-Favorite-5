from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/top5')
def posts():
    mas= ['Karate', 'Muay Thai', 'Capoeria', 'Taekwondo', 'Tang Soo Do']
    return render_template('list.html', mas = mas)
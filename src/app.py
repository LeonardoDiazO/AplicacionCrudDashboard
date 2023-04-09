from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
import mysql.connector 
import mysql 
import requests
import json
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime



from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/crud', methods=['GET', 'POST'])
def crud():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 5 #cantidad de registros por página
    url = "http://127.0.0.1:4000/api/herramientas"
    response = requests.get(url)
    dataGiphy = response.json()
    herramienta = dataGiphy['herramientas']
    total = len(herramienta) #total de registros
    offset = (page-1)*per_page
    herramienta = herramienta[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('auth/crud.html', dataGiphy=dataGiphy, dataTotal=total,
                           listaHerramienta=herramienta, pagination=pagination)


@app.route('/agregarHerramienta', methods=['GET','POST'])
def agregar():
    return render_template('auth/agregar.html')

#Registrando nueva herramient
@app.route('/herramientas', methods=['POST'])
def formAddHerramientas():
    json_string = '{"fecha": "2023-04-09"}'
    data = json.loads(json_string)
    fecha_json = data['fecha']
    fecha_python = datetime.strptime(fecha_json, '%Y-%m-%d').date()
    url = "http://127.0.0.1:4000/api/herramientas"
    data = {
        "articulo": request.json['articulo'],
        "descripcion": request.json['description'],
        "direccion": request.json['direccion'],
        "telefono": request.json['telefono'],
        "precio": request.json['precio'],
        "fecha": request.json['fecha']
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return jsonify({"message": "Herramienta agregada satisfactoriamente"})
    else:
        return jsonify({"message": "Error al agregar la herramienta"})


@app.route('/actualizarHerramientas', methods=['GET','POST'])
def actualizar():
    return render_template('auth/update.html')


    
    

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    url = "http://127.0.0.1:4000/api/herramientas"
    response = requests.get(url)
    dataDash =  response.json()
    total =  len(dataDash)#total de registros    
    return render_template('auth/dashboard.html',dataDash=data)

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


response = requests.get('http://localhost:4000/api/herramientas')
data = response.json()

#Listar los datos de herramientas
@app.route('/lista', methods=['GET'])
def listar_datos():
    return jsonify(datos=data)




if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)
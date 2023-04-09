from flask import Flask, jsonify, request , render_template, redirect, jsonify, session, url_for,flash
from werkzeug.security import  check_password_hash
from flask_mysqldb import MySQL ,  MySQLdb
from flask_cors import CORS
from datetime import timedelta
import mysql.connector 
from flask_cors import CORS, cross_origin


# CORS(app)


app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="crud_python_flask")
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=15)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_python_flask'
mysql = MySQL(app)

def is_loggedin():
    if 'loggedin' in session:
        return True
    else:
        return False


##Api consumida para las herramientas 

# Obtener todas las herramientas
@app.route('/api/herramientas', methods=['GET'])
def get_herramientas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM herramientas')
    result = cur.fetchall()
    cur.close()
     # Transformar los datos en la lista de diccionarios
    herramientas = []
    for row in result:
        herramienta = {
            "id": row[0],
            "articulo": row[1],
            "description": row[2],
            "direccion": row[3],
            "telefono": row[4],
            "precio": row[5],
            "fecha": row[6]
        }
        herramientas.append(herramienta)
    return jsonify({'herramientas': herramientas, 'mensaje': "Herramientas listados."})

# Obtener una herramienta por su id
@app.route('/api/herramientas/<int:herramienta_id>', methods=['GET'])
def get_herramienta(herramienta_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM herramientas WHERE id = %s', [herramienta_id])
    result = cur.fetchone()
    cur.close()
    return jsonify(result)

# Crear una nueva herramienta
@app.route('/api/herramientas', methods=['POST'])
def create_herramienta():
    articulo = request.json['articulo']
    description = request.json['description']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    precio = request.json['precio']
    fecha = request.json['fecha']

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO herramientas (articulo, description, direccion, telefono, precio, fecha) VALUES (%s, %s, %s, %s, %s, %s)', (articulo, description, direccion, telefono, precio, fecha))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Herramienta creada exitosamente'})

# Actualizar una herramienta
@app.route('/api/herramientas/<int:herramienta_id>', methods=['PUT'])
def update_herramienta(herramienta_id):
    articulo = request.json['articulo']
    description = request.json['description']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    precio = request.json['precio']
    fecha = request.json['fecha']

    cur = mysql.connection.cursor()
    cur.execute('UPDATE herramientas SET articulo = %s, description = %s, direccion = %s, telefono = %s, precio = %s, fecha = %s WHERE id = %s', (articulo, description, direccion, telefono, precio, fecha, herramienta_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Herramienta actualizada exitosamente'})

# Eliminar una herramienta
@app.route('/api/herramientas/<int:herramienta_id>', methods=['DELETE'])
def delete_herramienta(herramienta_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM herramientas WHERE id = %s', [herramienta_id])
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Herramienta eliminada exitosamente'})



if __name__ == '__main__':
    app.run(debug=True, port=4000)

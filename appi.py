from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config


app = Flask(__name__)

# CORS(app)
CORS(app)

conexion = MySQL(app)


# @cross_origin
@app.route('/herramientas', methods=['GET'])
def listar_herramientas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT articulo, description, direccion, telefono, precio, fecha FROM herramientas ORDER BY articulo ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        herramientas = []
        for fila in datos:
            herramientas = {'articulo': fila[0], 'description': fila[1], 'direccion': fila[2], 'telefono': fila[3], 'precio': fila[4], 'fecha': fila[5]}
            herramientas.append(herramientas)
        return jsonify({'herramientas': herramientas, 'mensaje': "Herramientas listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def leer_herramientas_bd(articulo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT articulo, description,  direccion, telefono, precio, fecha  FROM herramientas WHERE articulo = '{0}'".format(articulo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            herramientas = {'articulo': datos[0], 'description': datos[1], 'direccion': datos[2], 'telefono': datos[3], 'precio': datos[4], 'fecha': datos[5]}
            return herramientas
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/herramientas/<articulo>', methods=['GET'])
def leer_herramientas(articulo):
    try:
        herramientas = leer_herramientas_bd(articulo)
        if herramientas != None:
            return jsonify({'herramientas': herramientas, 'mensaje': "herramientas encontrada.", 'exito': True})
        else:
            return jsonify({'mensaje': "herramientas no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


@app.route('/cursos', methods=['POST'])
def registrar_herramienta():
    # print(request.json)
    if (validar_articulo(request.json['articulo']) and validar_description(request.json['description']) and validar_direccion(request.json['direccion'])):
        try:
            herramientas = leer_herramientas_bd(request.json['articulo'])
            if herramientas != None:
                return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO herramientas (articulo, description, direccion, telefono, precio, fecha ) 
                VALUES ('{0}', '{1}', {2})""".format(request.json['articulo'],
                                                     request.json['description'], request.json['direccion'],
                                                     request.json['telefono'],
                                                     request.json['precio'], request.json['fecha'],)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de inserción.
                return jsonify({'mensaje': "herramientas registrada.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<articulo>', methods=['PUT'])
def actualizar_curso(articulo):
    if (validar_codigo(articulo) and validar_nombre(request.json['description']) and validar_creditos(request.json['direccion'])):
        try:
            herramientas = leer_curso_bd(articulo)
            if herramientas != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE herramientas SET description = '{0}', direccion = {1} 
                WHERE articulo = '{2}'""".format(request.json['description'], request.json['direccion'], articulo)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "herramientas actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "herramientas no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<articulo>', methods=['DELETE'])
def eliminar_herramientas(articulo):
    try:
        herramientas = leer_herramientas_bd(articulo)
        if herramientas != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM herramientas WHERE articulo = '{0}'".format(articulo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "herramientas eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "herramientas no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
from flask import jsonify, request
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from config.bd import bd, app
from model.User import User

@app.route("/login_without_cookies", methods=["POST"])
def login_without_cookies():
    access_token = create_access_token(identity="example_user")
    return jsonify(access_token=access_token)


@app.route("/login_with_cookies", methods=["POST"])
def login_with_cookies():
    #Obtengo los datos del json
    username = request.json.get("username")
    full_name = request.json.get("full_name")
    password = request.json.get("password")
    #Consulto en la bd
    user=User.query.filter_by(username=username).one_or_none
    #verifico si esta el usuario o tambien si la contrasena conside con la que registre por defecto en el modelo
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401
    
    #sino 
    response = jsonify({"msg": "login successful"})
    #se crea el token con la identidad
    access_token = create_access_token(identity=user.id)
    #Se establece en la cokie 
    set_access_cookies(response, access_token)
    return response


@app.route("/logout_with_cookies", methods=["POST"])
def logout_with_cookies():
    response = jsonify({"msg": "logout successful"})
    #eliminar las cookies del lado del cliente unset_jwt_cookies
    unset_jwt_cookies(response)
    return response

#el token puede ir en cualquier lado
@app.route("/protected", methods=["GET", "POST"])
@jwt_required()
def protected():
   return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )

#el token debe ir en el header
@app.route("/only_headers")
@jwt_required(locations=["headers"])
def only_headers():
     return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )

if __name__ == '__main__':
    # Corregir typo en el argumento "debug"
    app.run(debug=True, host='0.0.0.0', port=9566)

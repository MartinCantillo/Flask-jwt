from datetime import timedelta
from flask import jsonify, request
from model.Rol import Rol , RolSchema
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from config.bd import bd, app

from model.User import User ,UserSchema

Rol_schema = RolSchema()
rols_schema = RolSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

#Authenticate without send  the cookies to the frontend , it wont be used for now
@app.route("/login_without_cookies", methods=["POST"])
def login_without_cookies():
    access_token = create_access_token(identity="example_user")
    return jsonify(access_token=access_token)

#Authenticate  send them to the frontend , it will be used  
@app.route("/login_with_cookies", methods=["POST"])
def login_with_cookies():

    #Consulto en la bd
    try:
     #Obtengo los datos del json
     username = request.json["username"]
     password = request.json["password"]
     print(username)
     user = User.query.filter_by(username=username, password=password).one_or_none()
     #verifico si esta el usuario o tambien si la contrasena conside con la que registre por defecto en el modelo
     if not user or user.password !=password :
        return jsonify("Wrong username or password incorrect "), 401
    
    #sino 
    # Crear un token con un tiempo de expiración de 1 hora
     expires = timedelta(hours=1)
    #se crea el token con la identidad , la identidad se crea con el id del usuario
     access_token = create_access_token(identity= user.id , expires_delta=expires)
     response = jsonify({"msg": "login successful"} , 'Acces_token ='+access_token)
    #Se establece en la cokiee 
     set_access_cookies(response, access_token)
     print("token"+access_token)
     return response
    except Exception as e:
     print(f"Error: {e}")
     return jsonify({"error": "Internal Server Error"}), 500
    
    
   


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

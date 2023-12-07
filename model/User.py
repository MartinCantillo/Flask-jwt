
from hmac import compare_digest

from config.bd import bd,app,ma
class User(bd.Model):
   __tablename__="tbUser"
   id = bd.Column(bd.Integer, primary_key=True)
   username = bd.Column(bd.Text, nullable=False, unique=True)
   full_name = bd.Column(bd.Text, nullable=False)
   

with app.app_context():
    bd.create_all()
#Se personzaliza automaticamente cuando se crea la identidad en la api
#Aqui se ejecuta directmanete cuando se crea el token access_token = create_access_token(identity=user)
#@jwt.user_identity_loader
#def user_identity_lookup(user):
 #   return user.id

#Se personaliza utomaticamente como se carga un usuario a partir de la identidad almacenada en el token 
#Se ejecuta directamente cuando se carga current_user = get_jwt_identity() el get_jwt_identity()
#@jwt.user_lookup_loader
#def user_lookup_callback(_jwt_header, jwt_data):
 #   identity = jwt_data["sub"]
  #  return User.query.filter_by(id=identity).one_or_none()
#Descerializacion
class UserSchema(ma.Schema):
    class Meta:
        fields=("id","username","full_name")
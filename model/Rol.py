from config.bd import bd , app, ma

#Entity Rol
class Rol(bd.Model):
 __tablename__="tblRol"
 id_rol=bd.Column(bd.Integer, primary_key=True)
 nombre_usuario=bd.Column(bd.String(50))


with app.app_context():
    bd.create_all()

    
#Descerializacion
class RolSchema(ma.Schema):
    class Meta:
        fields=("id_rol","nombre_usuario")
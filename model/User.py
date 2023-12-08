from config.bd import bd,app,ma

#Entity User
class User(bd.Model):
   __tablename__="tblUser"
   id = bd.Column(bd.Integer, primary_key=True)
   username = bd.Column(bd.Text, nullable=False, unique=True)
   full_name = bd.Column(bd.String(50),  nullable=False)
   password = bd.Column(bd.String(50),  nullable=False)
   rol_id = bd.Column(bd.Integer, bd.ForeignKey('tblRol.id_rol'), nullable=False)
   


with app.app_context():
    bd.create_all()

#Descerializacion
class UserSchema(ma.Schema):
    class Meta:
        fields=("id","username","full_name","password","rol_id","rol")
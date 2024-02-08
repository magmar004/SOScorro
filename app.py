from flask import Flask, render_template, request, redirect, url_for
from Instanciar_bd import db, Datos_usuario
from send_sms import crear_mensaje
#intrucciones un objeto a partir de la clase Flask
app = Flask(__name__)

#configuraciones de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializamos la base de datos
db.init_app(app)
#with app.app_context():
#    db.create_all()

#RUTAS
@app.route('/')
def bienveni2():
    #ESTIRAR DATOS DE LA BASE DE DATOS
    usuarios = Datos_usuario.query.all()
    return render_template('bienveni2.html', usuarios_html = usuarios)


@app.route('/registro',methods = ['POST', 'GET'])
def registro():
    if request.method == 'POST':
        #OBTENER DATOS DESDE EL FROM (DESDE UN FORMULARIO)
        nombre = request.form.get('nombre')
        cedula_de_identidad = request.form.get("cedula_de_identidad")
        tipo_de_sangre = request.form.get("tipo_de_sangre")
        donante_de_organos = request.form.get("donante_de_organos")
        alergia_a = request.form.get("alergia_a")

        #creamos el objeto tipo participante
        usuario = Datos_usuario(nombre=nombre, 
        cedula_de_identidad=cedula_de_identidad, tipo_de_sangre=tipo_de_sangre, 
        donante_de_organos=donante_de_organos, alergia_a=alergia_a)

        #añadimos a la base de datos
        db.session.add(usuario)
        db.session.commit()
        return render_template('pantalla_principal.html',usuario=usuario)
    return render_template('registro.html')

@app.route("/pantalla_principal")
def pantalla_principal():
    
    return render_template("pantalla_principal.html")

@app.route("/iniciar_sesion", methods = ["GET", "POST"] )
def iniciar_sesion():
    if request.method == 'POST':
        #OBTENER DATOS DESDE EL FROM (DESDE UN FORMULARIO)
        cedula_de_identidad = request.form["cedula_de_identidad"]
        cedula_de_identidad_bd = Datos_usuario.query.filter_by(cedula_de_identidad=cedula_de_identidad).first()
        if cedula_de_identidad_bd :
            return render_template('pantalla_principal.html',usuario=cedula_de_identidad_bd)
        else:
            return redirect(url_for('registro'))

    return render_template("iniciar_sesion.html")


#Pagimna donde se visualiza el perfil
@app.route('/perfil/<id>', methods=['GET','POST'])
def perfil(id):
    participante = Datos_usuario.query.get(id)
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        cedula_de_identidad = request.form.get("cedula_de_identidad")
        tipo_de_sangre = request.form.get("tipo_de_sangre")
        donante_de_organos = request.form.get("donante_de_organos")
        alergia_a = request.form.get("alergia_a")

        return redirect(url_for('bienveni2'))
    return render_template('perfil.html',usuario = participante)

#Pagina donde se edita/modifica el perfil
@app.route('/modificar_perfil/<id>', methods=['GET','POST'])
def modificar_perfil(id):
    participante = Datos_usuario.query.get(id)
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        cedula_de_identidad = request.form.get("cedula_de_identidad")
        tipo_de_sangre = request.form.get("tipo_de_sangre")
        donante_de_organos = request.form.get("donante_de_organos")
        alergia_a = request.form.get("alergia_a")
        
        #cargar la info al objeto
        
        participante.nombre=nombre
        participante.cedula_de_identidad=cedula_de_identidad
        participante.tipo_de_sangre=tipo_de_sangre
        participante.donante_de_organos=donante_de_organos
        participante.alergia_a=alergia_a
        
        db.session.commit()
        print('usuario modificado con exito')
        return redirect(url_for('bienveni2'))
    return render_template('modificar_perfil.html',usuario = participante)

@app.route("/send_message", methods=["GET","POST"])
def send_message():
    if request.method == 'POST':
        latitud = request.form.get("latitud")
        longitud = request.form.get("longitud")
        google_map = f"https://maps.google.com/?q={latitud},{longitud}"
        message=crear_mensaje(google_map)
        print(message.sid)
    return render_template('enviado.html')


if __name__ == '__main__':
    app.run(debug = True)
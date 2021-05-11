import flask
from typing import List

#incializamos la aplicacion de flask
app = flask.Flask(__name__)
#para ver cuando hay errores en nuestra app
app.config['DEBUG'] = True 

#creamos la ruta de la pagina inicial. 
@app.route('/', methods = ['GET'])
def homepage():
	return 'Hola'

#ejecutamos y lanzamos la aplicacion
app.run()	
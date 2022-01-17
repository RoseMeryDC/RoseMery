#Llamar a la libreria
from flask import Flask, render_template
#A partir del objeto app, puede crear el servidor y abrir rutas de internet
app = Flask(__name__)

#Creación de ruta para página principal
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
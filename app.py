from flask import Flask 
app = Flask(__name__)

@app.route('/saludo/<nombre>') 
def home(nombre):     
 return f"Hola, {nombre.capitalize()}! Bienvenido a tu app personalizada"

if __name__ == "__main__":
    app.run()

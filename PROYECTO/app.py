from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

# Crear la aplicación Flask y definir la carpeta de plantillas
app = Flask(__name__, template_folder="templates")

# Cargar modelo y escalador
modelo_path = os.path.join(os.path.dirname(__file__), "knn_regressor_model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

with open(modelo_path, "rb") as model_file:
    modelo = pickle.load(model_file)
with open(scaler_path, "rb") as scaler_file:
    escalador = pickle.load(scaler_file)

# Ruta principal para renderizar la página HTML
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para hacer predicciones con el modelo
@app.route("/predict", methods=["POST"])
def predict():
    datos = request.get_json()
    if "features" not in datos:
        return jsonify({"error": "Falta la clave 'features' en el JSON."}), 400
    
    if len(datos["features"]) != 11:
        return jsonify({"error": "Se esperaban 11 valores."}), 400

    try:
        datos_np = np.array(datos["features"]).reshape(1, -1)
        datos_escalados = escalador.transform(datos_np)
        prediccion = modelo.predict(datos_escalados)
        return jsonify({"prediction": int(round(prediccion[0]))})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify  # Importamos Flask y funciones necesarias
import pickle  # Para cargar el modelo entrenado
import numpy as np  # Para manejar arreglos numéricos
import os  # Para manejar rutas de archivos de forma compatible con cualquier sistema operativo

# Crear la aplicación Flask y definir la carpeta donde están las plantillas HTML
app = Flask(__name__, template_folder="templates")

# Obtener las rutas absolutas de los archivos del modelo y el escalador
modelo_path = os.path.join(os.path.dirname(__file__), "knn_regressor_model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

# Cargar el modelo de predicción desde el archivo
with open(modelo_path, "rb") as model_file:
    modelo = pickle.load(model_file)  # Se carga el modelo KNN previamente entrenado

# Cargar el escalador para normalizar los datos antes de hacer predicciones
with open(scaler_path, "rb") as scaler_file:
    escalador = pickle.load(scaler_file)  # Se carga el StandardScaler

# Ruta principal para renderizar la interfaz web
@app.route("/")
def home():
    return render_template("index.html")  # Carga la página principal desde "templates/index.html"

# Ruta para hacer predicciones con el modelo
@app.route("/predict", methods=["POST"])
def predict():
    # Obtener datos en formato JSON desde la solicitud
    datos = request.get_json()

    # Validar si la clave "features" está presente en la solicitud
    if "features" not in datos:
        return jsonify({"error": "Falta la clave 'features' en el JSON."}), 400  # Código 400: solicitud incorrecta
    
    # Validar si se enviaron exactamente 11 valores
    if len(datos["features"]) != 11:
        return jsonify({"error": "Se esperaban 11 valores."}), 400  # Código 400: solicitud incorrecta

    try:
        # Convertir los datos en un array de NumPy y darles la forma correcta
        datos_np = np.array(datos["features"]).reshape(1, -1)

        # Normalizar los datos con el mismo escalador usado en el entrenamiento
        datos_escalados = escalador.transform(datos_np)

        # Hacer la predicción con el modelo KNN cargado
        prediccion = modelo.predict(datos_escalados)

        # Devolver la predicción en formato JSON, redondeando el resultado a un número entero
        return jsonify({"prediction": int(round(prediccion[0]))})

    except Exception as e:
        # En caso de error, devolver un mensaje de error en formato JSON
        return jsonify({"error": str(e)}), 400  # Código 400: solicitud incorrecta

# Ejecutar la aplicación Flask en modo depuración para ver errores en tiempo real
if __name__ == "__main__":
    app.run(debug=True)  # Ejecutar la aplicación en http://127.0.0.1:5000

# Predicción de Calidad del Vino 🍷

Este proyecto es una aplicación web que permite predecir la calidad del vino utilizando modelos de Machine Learning basados en K-Nearest Neighbors (KNN). La aplicación está construida con **Flask** y presenta una interfaz interactiva desarrollada con **Bootstrap** y **Swiper.js**.

## 📌 Características
- **Predicción de calidad del vino** a partir de sus características químicas.
- **Modelo KNN de Clasificación y Regresión** entrenado con un conjunto de datos de vinos tintos.
- **Interfaz interactiva** con un diseño moderno y responsivo.
- **Validación de datos** en tiempo real para evitar valores fuera de los rangos permitidos.
- **Visualización de modelos** con enlaces a Google Colab.

## 📂 Estructura del Proyecto
```
PROYECTO/
│── static/               # Archivos estáticos (imágenes, estilos)
│   ├── imagen.png        # Imagen de la primera tarjeta
│── templates/            # Plantillas HTML
│   ├── index.html        # Página principal
│── app.py                # Aplicación Flask
│── knn_regressor_model.pkl  # Modelo KNN de regresión
│── scaler.pkl            # Escalador de datos
│── README.md             # Documentación del proyecto
|── requirements.txt      # Requerimientos del proyecto
```

## 🚀 Instalación y Configuración
### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/usuario/proyecto-vino.git
cd proyecto-vino
```

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación
```sh
python app.py
```
Accede a la aplicación en `http://127.0.0.1:5000`.

## 🛠 Tecnologías Utilizadas
- **Python & Flask** - Backend y API
- **Scikit-Learn** - Modelos de Machine Learning
- **Bootstrap** - Estilización de la interfaz
- **Swiper.js** - Navegación entre secciones

## 📊 Modelos de Machine Learning
- **KNN Clasificación:** [🔗 Ver en Colab](https://colab.research.google.com/drive/1og35DNNZV0GsskWG3cl_hFj-092Y3h_T?usp=sharing)
- **KNN Regresión:** [🔗 Ver en Colab](https://colab.research.google.com/drive/1Ql28cVc5iZ-dnH6KpBCQ6KYNrtjxsog8?usp=sharing)

## 👥 Colaboradores
- Hamm Hernández, Erich Leonardo
📧 erich.hamm.hernandez@gmail.com
- Toro Morales, Daniel
📧 danieltoromorales08@gmail.com

## 📜 Licencia
Libre


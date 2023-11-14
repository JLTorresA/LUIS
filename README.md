# Evaluacion
Proyecto de envaluación Q system
# Diseñado con Fastapi
# Version Python superior : 3.10 

# 1.- Creando entorno virtual posteriormente activar el entorno.
- python -m venv venv   
# window : venv\Script\activate
# linux : source\bin\activate

# 2.- Instalar paquetes.
- python -m pip install --upgrade pip
- pip install -r requirements.txt

# 3.- Crear variable de entorno .env y configurar parametros de la BD, se toma el ejemplo de  .env.example 

# 4.- Una vez configurado la bd, ubicarse en la app. y correr el aplicativo .
- cd .\app
- uvicorn main:app --reload
# Esto con el fin de crear el servicio el servicio REST API, ya que FastAPI utiliza la herramienta Swagger UI para proporcionar una interfaz de usuario dinámica y fácil de usar que permite explorar y probar los endpoints de la API. La URL es http://127.0.0.1:8000/docs

# 5.- Como último paso correr el script (upload-data.sql) en el gestor de base de datos.
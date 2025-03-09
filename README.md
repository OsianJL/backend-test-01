backend-test-01 API
Esta API fue desarrollada utilizando Flask y varias extensiones para manejar autenticación, base de datos, migraciones y más. La API utiliza PostgreSQL como base de datos, la cual se levanta mediante Docker, y permite gestionar usuarios, confirmación de email, recuperación de contraseña, perfiles, mensajes públicos y chat.

Tecnologías Utilizadas
Flask: Framework web para Python.
Flask-SQLAlchemy: ORM para interactuar con la base de datos.
Flask-Migrate: Manejo de migraciones de base de datos.
Flask-JWT-Extended: Autenticación basada en JSON Web Tokens (JWT).
Flask-Bcrypt: Para el hash de contraseñas.
Flask-Mail: (Opcional) Envío de correos electrónicos.
Flask-RESTful: Para construir endpoints RESTful.
Flask-Admin: Panel de administración para la API.
python-dotenv: Carga variables de entorno desde un archivo .env.
psycopg2-binary: Driver para conectar con PostgreSQL.
itsdangerous: Generación y verificación de tokens de seguridad.
Clonar el Proyecto desde GitHub
Para clonar el repositorio, ejecuta en la terminal:

bash
Copiar
git clone https://github.com/tu_usuario/backend-test-01.git
cd backend-test-01
(Reemplaza tu_usuario por tu nombre de usuario en GitHub y la URL por la de tu repositorio.)

Instalación de Dependencias
Crea y activa un entorno virtual:

En Windows (usando Bash):

bash
Copiar
python -m venv venv
source venv/Scripts/activate
Instala las dependencias usando pip:

bash
Copiar
pip install -r requirements.txt
Configuración de la Base de Datos con Docker
La API utiliza una base de datos PostgreSQL que se levanta mediante Docker. Si no tienes la base de datos corriendo, puedes utilizar el siguiente comando:

bash
Copiar
docker run --name postgres_backend_test_01 -e POSTGRES_USER=osidev -e POSTGRES_PASSWORD=osidev25 -e POSTGRES_DB=backend_test_01_db -p 5433:5432 -d postgres:16
Este comando levanta un contenedor PostgreSQL en el puerto 5433 de tu máquina.
Asegúrate de que la variable DATABASE_URL en el archivo .env esté configurada correctamente:
bash
Copiar
DATABASE_URL=postgresql://osidev:osidev25@localhost:5433/backend_test_01_db
Si necesitas reiniciar o eliminar el contenedor, puedes utilizar:

bash
Copiar
docker rm -f postgres_backend_test_01
o, si usas docker-compose, configura el archivo docker-compose.yml y usa:

bash
Copiar
docker-compose down -v
docker-compose up -d
Levantar el Servidor
Con la base de datos corriendo y las dependencias instaladas, levanta la API ejecutando:

bash
Copiar
python run.py
La aplicación se iniciará en modo desarrollo (debug=True) y podrás acceder a ella en http://127.0.0.1:5000/.
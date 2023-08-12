# Instrucciones

Hay unas pequeñas indicaciones para correr el proyecto

## Django

Para poder correr el proyecto es recomendable crear un entorno virtual para descargar las dependencias de nuestro proyecto.

Para crear un entorno virtual se tiene que ejecutar el comando 

### `python3 -m venv [nombre-env]`

Una vez creado se deberán activar el entorno virtual
### `source nombre-env/bin/activate`

Ya activado se deberan instalar las dependencias del archivo requeriments.txt
### `pip3 install -r requeriments`

## Base de datos

Dentro del proyecto hay un archivo de docker compose que contiene la base de datos y el usuario necesaria para el proyecto.

Para levantar el contenedor hay que introducir el siguiente comando:

### `docker compose up -d`

ya levantado nuestra base de datos se harán las migraciones con los siguientes comandos: 

### `python3 manage.py makemigrations`
### `python3 manage.py migrate`


## backup

también cuenta con un archivo llamado backup.txt, el contenido se deberá pegar dentro de su sistema gestor de base datos preferido y ejecutarlo (el cliente utilizado es postgresql).

o si no cuenta con uno se puede acceder directamente al contenedor con el comando: 

### `docker exec -it postgres_edificio psql db_edificio usr_edificio`

Con este comando podremos acceder a terminal de postgresql y pegaremos las lineas de código.

### `Es importante que para este paso aun no se haya creado ningún otro usuario`

## Cambios de contraseña
por ultimo se creara una cuenta de súper usuario de django para poder acceder al administrador y cambiar las contraseñas de los 3 usuarios registrados.

Para crear una cuenta de super usuario se usara el siguiente comando:
### `python3 manage.py createsuperuser`
y una vez creado cambiaremos la contraseña de los 3 usuarios creados.

correremos la aplicación con el comando:

### `python manage.py runserver`
Entraremos a la dirección :

### `http://127.0.0.1:8000/admin/`

pondremos nuestro correo y contraseña que acabamos de registrar. Dentro del lado izquierdo estan las tablas de nuestra base.

Daremos click al menu de usuario en users y al seleccionar el campo username, te llevara a sus datos, en el segundo apartado viene la password, donde nos indicara que no tenemos una contraseña y el siguiente texto:

### Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using `this form.`

En el apartado this form se puede cambiar la contraseña.

Para borrar el contenedor y lo relacionado use el comando.

### `docker compose down -v`

Tambien se añadio swagger para que pueda ver los endpoints generados en el proyecto y pueda probarlos desde ahi. Se encuentra en la ruta: 

### `http://127.0.0.1:8000/docs/`

para porbar los post, patch, put debera pasar el token de acceso en el authorized.
# Instrucciones

Hay unas pequeñas indicaciones para correr el proyecto

## Django

Para poder correr el proyecto es recomendable crear un entorno virtual para descragar las dependencias de nuestro proyecto.

Para crear un entorno virtual se tiene que ejecutar el comando 

### `python3 -m venv [nombre-env]`

Una vez creado se deberan activar el entorno virtual
### `source nombre-env/bin/activate`

Ya activado se deberan instalar las dependencias del archivo requeriments.txt
### `pip3 install -r requeriments`

## Base de datos

Dentro del proyecto hay un archivo de docker compose que contiene la base de datos y el usuario necesaria para el proyecto.

Para levantar el contenedor hay que introducir el siguiente comando:

### `docker compose up -d`

ya levantado nuestra base de datos se haran las migraciones con los siguientes comandos: 


### `python3 manage.py makemigrations`
### `python3 manage.py migrate`



## backup

tambien cuenta con un archivo llamado backup.txt, el contenido se debera pegar dentro de su manegador de base datos preferido y ejecutarlo.

o si no cuenta con uno se puede acceder directamente al contenedor con el comando: 

### `docker exec -it postgres_edificio psql db_edificio usr_edificio`

Con este comando podremos acceder a terminal de postgrest y pegaremos las lienas de codigo.

### `Es importante que para este paso aun no se haya creado ningun otro usuario`

## Cambios de contraseña
por ultimo se creara una cuenta de superusuario de django para poder acceder al administrador y cambiar las contraseñas de los 3 usuarios registrados.

Para crear una cuenta de super usuario se usara el siguiente comando:
### `python3 manage.py createsuperuser`
y una vez creado cambiaremos la contraseña de los 3 usuarios creados.

Entraremos a la direccion :

### `http://127.0.0.1:8000/admin/`

pondremos nuestro correo y contraseña que acabamos de registar.Dentro del lado izquierdo estan las tablas de nuestra base.

Daremos click al menu de usuario en users y al seleccionar el campo username, te llebara a sus datos, en el seguno apartado viene la password, donde nos indicara que no tenemos una contraseña y el siguiente texto:

### Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using `this form.`

En el apartado this form se puede cambiar la contraseña.

Por ultimo correremos la aplicacion con el comando 

### `python manage.py runserver`
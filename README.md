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

Despues correremos la aplicacion con el comando 

### `python manage.py runserver`

## Base de datos

Dentro del proyecto hay un archivo de docker compose que contiene la base de datos y el usuario necesaria para el proyecto.

### `docker compose up -d`

Dentro del repositorio esta un archivo llamado backup, el contenido se debera pegar dentro de su manegador de base datos preferido y ejecutarlo 

una vez lenvantada haremos las migraciones con

### `python3 manage.py migrate`

tambien crearemos un super usuario con el comando 

### `python3 manage.py createsuperuser`
y una vez creado cambiaremos la contraseña de los 3 usuarios creados.

Entrando al admin y de ahi al menu de usuario y al seleccionar un campo te llebara a sus datos, en el seguno apartado viene la contraseña se va modificar a contraseñas de su preferencia

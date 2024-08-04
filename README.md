# FoodPlease - CRUD de Productos

FoodPlease es una aplicación web que permite gestionar productos a través de operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Este proyecto está construido utilizando Django como framework backend y MySQL como base de datos.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.12
- MySQL
- pip (el gestor de paquetes de Python)
- Django

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Javierinc/foodplease.git
```

### 2. Crear y Activar un Entorno Virtual

Navega a la carpeta del proyecto y crea un entorno virtual:

```bash
cd foodplease
python -m venv env
```

Activa el entorno virtual:

- En Windows:

```bash
env\Scripts\activate
```

- En Linux/Mac:

```bash
source env/bin/activate
```

### 3. Instalar las Dependencias

Instala las dependencias necesarias con pip:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe incluir las siguientes dependencias:

```
django
pymysql
mysqlclient
```

### 4. Configurar la Base de Datos

Crea una base de datos MySQL llamada `bd1`. Puedes hacerlo desde la línea de comandos de MySQL:

```sql
CREATE DATABASE bd1;
```

Si deseas usar otro nombre de base de datos, debes modificar el archivo `settings.py` en la carpeta `FoodPlease` para reflejar el cambio:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd1',
        'USER': 'root',
        'PASSWORD': ''
    }
}
```

### 5. Aplicar las Migraciones

Aplica las migraciones para crear las tablas necesarias en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```



### 7. Ejecutar el Servidor de Desarrollo

Finalmente, ejecuta el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Abre tu navegador y navega a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Uso

Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes características:

- **CRUD de Productos**: Crear, leer, actualizar y eliminar productos.
## Personalización
### Cambiar el Nombre de la Base de Datos

Si deseas utilizar una base de datos con un nombre diferente, actualiza la configuración de la base de datos en el archivo `settings.py` de la carpeta `FoodPlease` como se mencionó anteriormente.










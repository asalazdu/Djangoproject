# Djangoproject

Este es un proyecto de Django llamado **Djangoproject** que gestiona reservas de citas en una IPS.

## Requisitos

Asegúrate de tener instalado lo siguiente en tu máquina:

- [Python](https://www.python.org/downloads/) (versión 3.6 o superior)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

## Configuración del entorno local

1. **Clona el repositorio:**
   - git clone https://github.com/asalazdu/Djangoproject.git

2. **Navega a la carpeta del proyecto:**
    - cd Djangoproject

3. **Crea un entorno virtual:**
    - En la terminal ejecuta el siguiente comando instalar la libreria virtualenv:
      pip install virtualenv
    - En la terminal ejecuta el siguiente comando para crear un entorno virtual:
    - En Windows:
      python -m venv venv
    1. **Ativa el entorno en windows:**
        .\venv\Scripts\activate
    1. **Ativa el entorno en macOS/Linux:**
        .python3 -m venv venv
4. **Instala las totas las librerias que necesita el proyecto:**
    - En la terminal ejecuta el siguiente comando instalar django:
      pip install -r requirements.txt


## Ejecución del proyecto

1. **Ejecuta el servidor de desarrollo:**
    - python manage.py runserver

2. **Accede a la aplicación:**
    - Abre tu navegador y visita http://127.0.0.1:8000/

## NOTAS
- Asegúrate de que el entorno virtual esté activo cada vez que trabajes en el proyecto.
- El entorno virtual (venv) está ignorado en el repositorio y no se debe subir a GitHub.

## CONTRIBUCIONES
- Si deseas contribuir a este proyecto, por favor crea una rama nueva para tus cambios y envía un pull request.

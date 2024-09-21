# Djangoproject

Este es un proyecto de Django llamado **Djangoproject** que gestiona reservas de citas en una IPS.

## Requisitos

Asegúrate de tener instalado lo siguiente en tu máquina:

- [Python](https://www.python.org/downloads/) (versión 3.6 o superior)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

## Configuración del entorno local

1. **Clona el repositorio:**
   git clone https://github.com/asalazdu/Djangoproject.git

2. **Navega a la carpeta del proyecto:**
    cd Djangoproject

3. **Crea un entorno virtual:**
    En la terminal ejecuta el siguiente comando para crear un entorno virutal:
    En Windows:
      python -m venv venv
    1. **Ativa el entorno:**
        .\venv\Scripts\activate
    En macOS/Linux:
        python3 -m venv venv
    1. **Activa el entorno:**
        source venv/bin/activate

## Ejecución del proyecto

1. **Aplica las migraciones:**
    python manage.py migrate

2. **Ejecuta el servidor de desarrollo:**
    python manage.py runserver

3. **Accede a la aplicación:**
    Abre tu navegador y visita http://127.0.0.1:8000/

## NOTAS
- Asegúrate de que el entorno virtual esté activo cada vez que trabajes en el proyecto.
- El entorno virtual (venv) está ignorado en el repositorio y no se debe subir a GitHub.

## CONTRIBUCIONES
- Si deseas contribuir a este proyecto, por favor crea una rama nueva para tus cambios y envía un pull request.
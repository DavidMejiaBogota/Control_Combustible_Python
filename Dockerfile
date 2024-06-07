#Este código establece que se utilizará una imagen de Python versión 3.10.4, 
#con una versión reducida ("slim") y basada en el sistema operativo Debian 11 ("bullseye")
#como base para construir la nueva imagen Docker.
FROM python:3.10.4-slim-bullseye

#Setear variables de entorno

#configura una variable de entorno para desactivar la comprobación de la versión de pip al
#instalar paquetes de Python dentro del contenedor Docker
ENV PIP_DISALBE_PIP_VERSION_CHECK 1

#desactiva la generación de archivos de bytecode de Python al
#compilar módulos dentro del contenedor Docker.
ENV PYTHONDONTWRITEBYCODE 1

#asegura que la salida de Python se muestre inmediatamente en tiempo real
#en lugar de almacenarse en búfer, lo que puede ser útil para ver la salida de manera más
#rápida y precisa al ejecutar aplicaciones Python dentro del contenedor Docker.
ENV PYTHONUNBUFFERED 1

#asegura de que cualquier instrucción que siga después en el archivo se ejecute dentro del
#directorio /code dentro del contenedor. Esto es útil para organizar el entorno de trabajo y
#facilitar la ejecución de comandos relacionados con el código de la aplicación.
WORKDIR /code

RUN python -m pip install --upgrade pip

#instalar todas las dependencias de la aplicación
COPY ./requirements.txt .

#asegura de que todas las dependencias requeridas por la 
#aplicación se instalen correctamente en el contenedor durante la creación de la imagen
RUN pip install -r requirements.txt

#copia todos los archivos y directorios del directorio de contexto (de la raiz) del Docker build al
#directorio de trabajo (.code/) del contenedor.
COPY . .
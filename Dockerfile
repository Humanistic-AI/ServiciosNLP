
#  "Máquina virtual" que tiene instalado pytho 3.12, sobre un Linux ligero.
FROM python:3.12  

WORKDIR /code

# COPY     archivo_local     ruta_en_el_contenedor
COPY ./requirements.txt      /code/requirements.txt

# Esto se ejecuta dentro del contenedor, no en la máquina local.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install "fastapi[standard]"

# Copiamos el código
COPY ./app /code/app

# Este comando es el que se ejecutará cuando se inicie el contenedor.
#CMD ["fastapi", "run", "app/main.py", "--port", "80"]
WORKDIR /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
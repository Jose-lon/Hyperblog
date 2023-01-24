FROM python:3.10.6

WORKDIR /Proyectos-Python
COPY requirements.txt /Proyectos-Python/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /Proyectos-Python/requirements.txt

COPY . /Proyectos-Python

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
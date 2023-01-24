FROM python:3.8

WORKDIR /Proyectos-Python
COPY requirements.txt /Proyectos-Python/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Proyectos-Python/requirements.txt

COPY . / Proyectos-Python/

CMD bash -c "while true; do sleep 1; done"
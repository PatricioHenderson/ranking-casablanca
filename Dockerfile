FROM python:3.9.5
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/back_end
COPY . /opt/back_end

# Dejamos las variables definidas para un entorno de desarrollo, 
# debemos remplazarlas para un entorno productivo
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_HOST=db
# Dejamos DEBUG=True para hacer los retoques antes de pasarlo a False para producción.
ENV DEBUG=True

ENV SECRET_KEY=django-insecure-t25m+n5yijf1vz7f$1v6-##x##l^e3(+sem-gj&o7cycv9@n=c
RUN python ranking_padel/manage.py collectstatic --noinput
CMD gunicorn --chdir /opt/back_end/ranking_padel ranking_padel.wsgi:application --bind 0.0.0.0:$PORT

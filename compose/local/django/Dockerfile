FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update --no-cache \
  # psycopg2 dependencies
  && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  && apk add --no-cache postgresql-dev \
  # Pillow dependencies
  && apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add --no-cache libffi-dev py-cffi \
  # Translations dependencies
  && apk add --no-cache gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add --no-cache postgresql-client

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /requirements/local.txt

COPY ./compose/production/django/entrypoint /entrypoint
COPY ./compose/local/django/start /start

RUN sed -i 's/\r$//g' /entrypoint \
    && chmod +x /entrypoint \
    && sed -i 's/\r$//g' /start \
    && chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

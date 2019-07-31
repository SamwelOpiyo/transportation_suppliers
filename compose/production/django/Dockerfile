FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" \
    >> /etc/apk/repositories \
    && echo "@edgecommunity http://nl.alpinelinux.org/alpine/edge/community" \
    >> /etc/apk/repositories \
    && echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" \
    >> /etc/apk/repositories \
    && apk update --no-cache \
    # psycopg2 dependencies
    && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
    geoip-dev postgresql-dev \
    # Pillow dependencies
    && apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
    tiff-dev tk-dev tcl-dev \
    # CFFI dependencies
    && apk add --no-cache libffi-dev py-cffi \
    && apk add --no-cache libcrypto1.1@edge geos-dev@testing gdal-dev@testing

RUN addgroup -S django \
    && adduser -S -G django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY ./compose/production/django/entrypoint /entrypoint
COPY ./compose/production/django/start /start

RUN sed -i 's/\r$//g' /entrypoint \
    && chmod +x /entrypoint \
    && chown django /entrypoint \
    && sed -i 's/\r$//g' /start \
    && chmod +x /start \
    && chown django /start

COPY . /app

RUN mkdir /var/log/app/ && chown -R django /app /var/log/app/

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

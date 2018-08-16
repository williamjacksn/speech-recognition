FROM python:3.7.0-alpine3.8

ENV AUDIO_FILE /data/audio_file.wav

COPY requirements.txt /app/requirements.txt

RUN apk --no-cache add --virtual .deps gcc musl-dev pulseaudio-dev swig \
 && apk --no-cache add alsa-lib-dev flac \
 && /usr/local/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
 && /usr/local/bin/pip install --no-cache-dir --requirement /app/requirements.txt \
 && apk del .deps

COPY run.py /app/run.py

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["/app/run.py"]

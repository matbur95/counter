FROM python:3.7-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        texlive-latex-base \
        imagemagick \
        ghostscript \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR /code/web
CMD ./run-gunicorn.sh
#CMD python server.py $PORT

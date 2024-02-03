# Utilisez une image de base appropriée
FROM python:3

# Définissez le répertoire de travail
ENV PYTHONBUFFERD 1

ENV PYTHONDONTWRTEBYTECODE 1

RUN mkdir /app

WORKDIR /app

COPY . /app/

# RUN python -m venv/bin/
RUN python -m venv venv


ENV PATH="/env/bin/:$PATH"

COPY entrypoint.sh /app/entrypoint.sh
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY requirements.txt /app/
# RUN python -m spacy download en_core_web_sm

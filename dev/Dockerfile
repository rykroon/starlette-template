FROM python:3.9-slim

WORKDIR /app
COPY app .

RUN apt-get update -y && \ 
	apt-get upgrade -y && \
	python -m pip install --upgrade pip && \
	pip install -r requirements.txt

EXPOSE 8000
CMD [ "gunicorn", "--config", "./gunicorn.conf.py", "main:app" ]
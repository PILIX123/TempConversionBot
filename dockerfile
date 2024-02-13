FROM python:alpine
ENV LANG C.UTF-8
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./converters /app/converters
COPY ./utils /app/utils
COPY ./vault /app/vault

WORKDIR /app
COPY ./main.py .
COPY .env .

CMD [ "python3","-OO","main.py" ]
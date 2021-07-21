FROM python:3.8.10

RUN mkdir -p /usr/src/main/
WORKDIR /usr/src/main/

COPY . /usr/src/main/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
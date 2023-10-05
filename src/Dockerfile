FROM python:3.9

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x startapp.sh

CMD [ "python", "-u", "app.py" ]
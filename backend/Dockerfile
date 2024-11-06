FROM python:3.11-slim

WORKDIR /backend-fiatmanagement

COPY requirements.txt /backend/
RUN pip3 install -r /backend/requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8015"]
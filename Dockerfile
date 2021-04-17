FROM python:3.8-slim

WORKDIR /app
EXPOSE 5001
COPY requirements*.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-b", ":5001", "--log-level", "info", "config.wsgi:application", "-t", "150"]
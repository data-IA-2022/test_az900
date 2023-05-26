FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=test_flask.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host", "0.0.0.0"]
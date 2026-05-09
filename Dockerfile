FROM python:3.14

WORKDIR /app
ENV TZ=Europe/Berlin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 71

CMD ["python", "main.py"]
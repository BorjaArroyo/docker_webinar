FROM alpine
WORKDIR /usr/src/app
COPY . .
RUN apk add --no-cache python3 py3-pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py", "--host", "0.0.0.0", "--port", "80"]
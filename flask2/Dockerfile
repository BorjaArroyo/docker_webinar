FROM alpine
WORKDIR /usr/src/app
COPY . .
RUN apk add --no-cache python3 py3-pip
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT "run.sh"
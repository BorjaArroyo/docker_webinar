FROM alpine
WORKDIR /usr/src/app
COPY . .
RUN apk add --no-cache python3 py3-pip dos2unix
RUN pip install --no-cache-dir -r requirements.txt
RUN dos2unix run.sh
RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
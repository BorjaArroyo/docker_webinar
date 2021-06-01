FROM alpine
WORKDIR /usr/src/app
COPY . .
RUN apk add --no-cache python3 py3-pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["chmod", "+x", "./run.sh"]
ENTRYPOINT ["./run.sh"]

FROM alpine:latest
RUN apk update && \
    apk add --no-cache python3-dev musl-dev libffi-dev && \
    apk add py-pip
RUN pip install --upgrade pip --break-system-packages
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt --break-system-packages
CMD ["python3", "app.py"]


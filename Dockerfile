FROM python:3.12-alpine

WORKDIR /api/rest_api

COPY . /api/rest_api/

RUN apk update && \
    apk add --no-cache bash && \
    pip install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh

EXPOSE 5000

CMD ["./run.sh"]

# To build container: docker build -t rest-api-app .
# To run the container: docker run -p 5000:5000 rest-api-app
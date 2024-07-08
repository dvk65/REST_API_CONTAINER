FROM python:3.12-alpine

WORKDIR /api/rest_api

COPY . /api/rest_api/

RUN apk update && \
    apk add --no-cache bash && \
    pip install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh

EXPOSE 5000

CMD ["./run.sh"]

# To push new image to rest_api repository
# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# v3 probably when working on workflow

# To build container: docker build -t rest-api-app .
# To run the container: docker run -p 5000:5000 rest-api-app
# pull official base image
FROM python:3.9.6-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache gcc python2-dev libc-dev && rm -rf /var/cache/apk/*
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

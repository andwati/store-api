FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv install

COPY . /app/

EXPOSE 8000

COPY ./docker-entrypoint.sh /docker-entrypoirnt.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]

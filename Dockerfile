FROM python:2.7

WORKDIR /usr/local/honeybee_anvil

RUN apt-get update

RUN pip install pipenv

COPY ./Pipfile* ./
RUN pipenv install

COPY ./*.py ./
COPY ./proto ./proto
COPY ./anvilCore ./anvilCore
COPY ./ladybug ./ladybug
COPY ./honeybee ./honeybee
COPY ./radiance /usr/local/radiance


EXPOSE 50001

ENTRYPOINT ["pipenv", "run", "python", "server.py"]

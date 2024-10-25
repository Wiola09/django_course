# Use Python 3.12.2 image based on Debian Bullseye in its slim variant as the base image
FROM python:3.12-bullseye

# Set an environment variable to unbuffer Python output, aiding in logging and debugging
ENV PYTHONBUFFERED=1

RUN mkdir /code

# Set the working directory within the container to /code for any subsequent commands
WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

COPY . .

ENTRYPOINT [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
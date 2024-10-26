# Use Python 3.12.2 image based on Debian Bullseye in its slim variant as the base image
FROM python:3.12-bullseye

# Set an environment variable to unbuffer Python output, aiding in logging and debugging
ENV PYTHONBUFFERED=1

RUN mkdir /code

# Set the working directory within the container to /code for any subsequent commands
WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .
# Define a build argument for CSRF_TRUSTED_ORIGINS
ARG CSRF_TRUSTED_ORIGINS
ARG SECRET_KEY
ARG ALLOWED_HOSTS
ARG DEBUG

# Set the CSRF_TRUSTED_ORIGINS environment variable using the build argument
ENV CSRF_TRUSTED_ORIGINS=${CSRF_TRUSTED_ORIGINS}
ENV SECRET_KEY=${SECRET_KEY}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DEBUG=${DEBUG}
RUN poetry run python manage.py migrate

ENTRYPOINT [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
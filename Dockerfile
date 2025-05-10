FROM python:3.14.0b1-alpine3.21
LABEL maintainer="@yourusernam"
LABEL description="LLM-Wrapper"
LABEL version="1.0"
LABEL license="MIT"

ENV PIPENV_VENV_IN_PROJECT=/app
ENV LANG="en_US.UTF-8"

# Copy requirements.txt into the container
COPY Pipfile .

# Install Python and pip
RUN apk add --no-cache python3 py3-pip && \
    pip install pipenv --root-user-action ignore && \
    pipenv install --quiet



# Set the working directory
WORKDIR /app

# Copy application files
COPY /app/*.py /app/


# Default command (run your Python script directly)
CMD ["pipenv", "run", "python", "test.py"]



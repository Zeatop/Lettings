FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

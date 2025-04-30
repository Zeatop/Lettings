FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . .
RUN pip install setuptools
RUN pip install --no-cache-dir -r requirements.txt
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

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
ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "oc_lettings_site.asgi:application"]

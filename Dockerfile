FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV APP_DIR=/app
ENV PROJECT_DIR=$APP_DIR/zpr
ENV VENV_DIR=$APP_DIR/env
ENV PATH="$VENV_DIR/bin:$PATH"

ENV DJANGO_SETTINGS_MODULE=zpr.settings

RUN mkdir -p $APP_DIR

COPY app/requirements.txt $APP_DIR/requirements.txt

RUN python -m venv $VENV_DIR
ENV PATH="$VENV_DIR/bin:$PATH"
RUN pip install --upgrade pip && pip install -r $APP_DIR/requirements.txt

WORKDIR $PROJECT_DIR

FROM python:3.14.6-alpine3.24

LABEL description="API endpoints with FastAPI and sqlite DB"
LABEL maintainer="kaoksn <foreversmiling@example.com>"
LABEL version="v1.0"

WORKDIR /app

RUN apk update && apk add curl

RUN addgroup -S appuser && adduser -S -h /home/appuser -G appuser appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

USER appuser
COPY --chown=appuser:appuser requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --chown=appuser:appuser ./app ./app
COPY --chown=appuser:appuser ./info.db .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11

RUN pip install fastapi uvicorn pydantic joblib pandas

COPY "./HR_API" "./api"

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]
CMD [ "HR_API:app", "--host", "0.0.0.0" ]
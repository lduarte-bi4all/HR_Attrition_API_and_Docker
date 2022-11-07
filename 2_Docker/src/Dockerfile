FROM python:3.9.13

WORKDIR /api
ADD requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY "./1_FastAPI/src/HR_API" "/api"

EXPOSE 5000

ENTRYPOINT [ "uvicorn", "HR_API:app", "--host", "0.0.0.0", "--port", "5000" ]
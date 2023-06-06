FROM python:3

RUN pip install mlflow fastapi pydantic requests uvicorn

COPY . .

EXPOSE 80

CMD [ "uvicorn" , "api:app", "--host", "0.0.0.0", "--port", "80"]


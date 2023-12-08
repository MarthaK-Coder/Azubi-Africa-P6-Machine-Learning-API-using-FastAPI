FROM python:3.11.6

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 900

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "900"]
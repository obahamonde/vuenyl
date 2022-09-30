FROM python:3.8-slim-buster
WORKDIR /app
COPY /api/ /app/
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000:80

# Language: dockerfile
# Path: dockerfile
FROM python:3.9-slim

# Set the working dir
WORKDIR /app
COPY . .

# Install package requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-dotenv

# Make port 80 available
EXPOSE 80

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

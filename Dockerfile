# 1. Use an official Python runtime as a parent image
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /code

# 4. Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# 5. Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy project
COPY . /code/

# 7. Expose port
EXPOSE 8000
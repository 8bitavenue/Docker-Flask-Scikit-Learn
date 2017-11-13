# Base image
FROM python:3.6.3

# Where API server lives
WORKDIR /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

# API server
COPY api.py /app/
EXPOSE 7777
ENTRYPOINT python ./api.py


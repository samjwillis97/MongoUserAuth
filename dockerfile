from python:3.9-slim

# Install Python Requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy python source code
COPY ./app/ /app

COPY ./start_server.py ./
RUN chmod +x ./start_server.py

EXPOSE 8000

CMD ["python","start_server.py"]
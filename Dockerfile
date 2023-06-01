FROM python:3.7-slim
WORKDIR /app
COPY inference.py api.py requirements.txt   .
COPY checkpoint/ ./checkpoint/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV FLASK_APP=api.py
CMD ["flask","run","--host=0.0.0.0"]

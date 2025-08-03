FROM python:3.10-slim
WORKDIR /app
COPY ./app /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=80", "--server.enableCORS=false"]
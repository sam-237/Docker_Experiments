# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

WORKDIR /app

COPY pythonapp.py pythonapp.py

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
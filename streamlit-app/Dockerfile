FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install pip, streamlit, and other dependencies explicitly
RUN pip install --upgrade pip && \
    pip install streamlit && \
    pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["python", "-m", "streamlit", "run", "streamlit-app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# © 2026 Mohammad Subhan Pasha. All Rights Reserved.
# ™ Deploy Ops Docker™ - Author: Mohammad Subhan Pasha
FROM python:3.11-slim
WORKDIR /app
COPY 01-fieldmitra-voice-ops/requirements.txt .
RUN pip install -r requirements.txt
COPY 01-fieldmitra-voice-ops/ .
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

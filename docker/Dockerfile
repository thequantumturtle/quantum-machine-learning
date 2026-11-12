FROM python:3.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 HOME=/home/student
RUN useradd --create-home --uid 1000 --shell /bin/bash student
WORKDIR /opt/qml
COPY docker/requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY scripts/smoke_test.py smoke_test.py
USER student
WORKDIR /workspace
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.root_dir=/workspace"]

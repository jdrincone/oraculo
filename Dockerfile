FROM python:3.11-slim

RUN pip install uv

WORKDIR /app
COPY . .

# Usar archivo de requerimientos explícitamente
RUN uv pip install --system --requirements requirements.txt

ENTRYPOINT ["python", "-m", "main"]

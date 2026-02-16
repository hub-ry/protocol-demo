# Stage 1: build Svelte frontend
FROM node:22-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci --omit=optional 2>/dev/null || npm install --omit=optional
COPY frontend/ .
RUN npm run build

# Stage 2: run FastAPI backend + serve built frontend
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY --from=frontend-build /app/frontend/.svelte-kit/output/client ./frontend/.svelte-kit/output/client
RUN mkdir -p data

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

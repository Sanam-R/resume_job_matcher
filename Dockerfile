# 1️⃣ Base image
FROM python:3.12-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copy requirements
COPY requirements.txt /app/

# 5️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy model
RUN python -m spacy download en_core_web_sm

# 6️⃣ Copy project code
COPY . /app

# 7️⃣ Expose port
EXPOSE 8000

# 8️⃣ Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

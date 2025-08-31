# Use slim Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Ensure Streamlit has a writable directory
ENV STREAMLIT_CONFIG_DIR=/tmp/.streamlit
ENV STREAMLIT_CACHE_DIR=/tmp/.streamlit-cache
RUN mkdir -p /tmp/.streamlit /tmp/.streamlit-cache

# Expose Streamlit port
EXPOSE 8503
CMD ["streamlit", "run", "app.py", "--server.port=8503", "--server.address=0.0.0.0"]

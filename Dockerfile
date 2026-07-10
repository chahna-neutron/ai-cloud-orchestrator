# Use a slim, production-ready base image to keep the container lightweight
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependency files first (Leverages Docker layer caching)
COPY requirements.txt .

# Install dependencies without saving local cache chunks (shrinks image size)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your FastAPI server runs on (7860 for Hugging Face Spaces)
EXPOSE 7860

# Run the server module
CMD ["python", "-m", "server.app"]
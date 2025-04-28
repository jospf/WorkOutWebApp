# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (if you had one)
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# --- Since we have very few dependencies, just install Flask directly ---
RUN pip install flask

# Now copy the application code
COPY app.py ./
COPY templates/ ./templates/

# Expose the app's port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

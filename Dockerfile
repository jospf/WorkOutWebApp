# Use an official Python runtime
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements (later optional) and app code
COPY app.py ./

# Install Flask
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

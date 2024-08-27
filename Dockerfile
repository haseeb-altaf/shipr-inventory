# Use an official Python runtime as a base image
FROM python:3.9.19-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the main application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

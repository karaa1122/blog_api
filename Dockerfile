
FROM python:3.11


WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your Django app runs (adjust if needed)
EXPOSE 8000

# Define the command to run your Django app when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

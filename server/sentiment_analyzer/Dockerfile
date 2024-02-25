# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m textblob.download_corpora

RUN apt update && apt upgrade -y && apt install curl -y

# Make port available to the world outside this container
EXPOSE 5001


# Run app.py when the container launches
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port","5001"]
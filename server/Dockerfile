    FROM python:3.12.0-slim-bookworm

    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYTECODE 1

    ENV APP=/app

    # Change the workdir.
    WORKDIR $APP

    # Install the requirements
    COPY requirements.txt $APP

    RUN pip3 install -r requirements.txt


    # Copy the rest of the files
    COPY . $APP

    EXPOSE 8001

    RUN chmod +x /app/entrypoint.sh

    RUN apt update && apt upgrade -y && apt install curl -y

    ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

    CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "djangoproj.wsgi"]
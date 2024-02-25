# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
import logging
load_dotenv()


logger = logging.getLogger("dealership") # Use the module's `__name__` to get a namespaced logger.


backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5001/"
)


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    logger.info(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        logger.info(response)
        return response.json()
    except Exception as e:
        logger.error(e)
        # If any error occurs
        print("Network exception occurred")


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "/analyze/" + text
    logger.info(f"analyze_review_sentiments from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# def post_review(data_dict):
# Add code for posting review

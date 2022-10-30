import logging
import os
import sys
from urllib.parse import quote_plus

import azure.functions as func
from pymongo import MongoClient

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

from entity import Subscriber


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Adding a new user to newsletter subscription")
    data = req.get_json()
    name = data["name"]
    email = data["email"]
    new_subscriber = Subscriber(name=name, email=email, is_subscribed=True)

    # TODO: Move this to env driven
    user = "admin"
    password = "password"
    host = "localhost"
    port = 27017

    uri = f"mongodb://{user}:{password}@{host}:{port}"


    client = MongoClient(uri)

    subscribers_collections = client["newsletter-subscriber"]["subscribers"]

    subscribers_collections.insert_one(new_subscriber.__dict__)
    
    return func.HttpResponse (status_code=200)

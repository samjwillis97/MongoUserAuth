from mongoengine import connect
from server.env_config import (
  MONGO_DB, MONGO_CLUSTER_URL, MONGO_USERNAME, MONGO_PASSWORD
)

connection_url = \
  f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER_URL}/{MONGO_DB}?retryWrites=true&w=majority"

connect(
  host=connection_url,
)
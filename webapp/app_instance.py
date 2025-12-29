from flask import Flask
import os

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv(
    "MONGO_URI",
    "mongodb://mongo:27017/Tripedia" 
)

app.secret_key = "mysecretkey"
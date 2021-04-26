from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
from barkylib.adapters.orm import start_mappers, metadata
from barkylib.domain import commands
from barkylib.api import views
from barkylib import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()


@app.route('/')
def index(self):
    return f'Hello World'


def delete(self, bookmark):
    pass


def update(self, bookmark):
    pass


if __name__ == "__main__":
    app.run()

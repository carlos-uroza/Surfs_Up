# Import python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the Flask dependency
from flask import Flask

# Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Set up automap
Base = automap_base()

# Reflect the database into our classes
Base.prepare(engine, reflect=True)

# Create classes variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Create a new Flask app instance
app = Flask(__name__)

# Create first Flask route
@app.route('/')
def hello_world():
    return 'Hello world of Bananas'

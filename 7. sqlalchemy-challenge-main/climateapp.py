import numpy as np
import pandas as pd
import datetime as dt
 # Statistical analysis
from scipy import stats

 # Python SQL toolkit and Object Relational Mapper
 # Import SQLAlchemy `automap` and other dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect,func
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import reflection

# Create Database Connection
engine = create_engine('sqlite:///../Resources/hawaii.sqlite')

#INSPECT
# Create inspection
inspector= inspect(engine)

 # reflect an existing database into a new model
BaseReflect= automap_base()
# reflect the tables
BaseReflect.prepare(engine,reflect=True)
# View all of the classes that automap found
BaseReflect.classes.keys
 # Save references to each table
    
measurement= BaseReflect.classes.measurement
station= BaseReflect.classes.station

# Create our session (link) from Python to the DB
from sqlalchemy.orm import Session
session = Session(bind=engine)

# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
active_station= session.query(measurement.station,measurement.date, measurement.prcp,measurment.tobs).\
    filter(measurement.date < '2011-01-01').\
    filter(measurement.station == 'USC00513117').\
    order_by(measurement.date).all()

date_plot_station= [result[1] for result in active_station]
prcp_plot_station= [result[2] for result in active_station]

tobs_plot_station= [result[3] for result in active_station]

# Filter out null values from lists
active_station_list = []
for prcp in prcp_plot_station:
    if type(prcp) == float:
        active_station_list.append(prcp)

# Filter out null values from lists
tobs_station_list = []
active_station_list = []
for tobs in tobs_plot_station:
    if type(tobs) == float:
        tobs_station_list.append(prcp)

 # Close Session
session.close()


####FLASK
from flask import Flask, jsonify
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
    return "Climate App"


#route for the precipitation of the most active station
@app.route("/api/v1.0/stations")
def precipitation_active_station():
    """Return station data as json"""

    return jsonify(active_station_list)

@app.route("/api/v1.0/tobs")
def tobs_active_station():
    """Return the tobs data in json"""

    return jsonify(tobs_station_list)


if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, redirect
import json
import flask_pymongo import PyMongo
import time
import mission_mars


#flask instance
app = Flask(__name__)

# Database connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    #find one record of data from mongo database
    mars = mongo.db.mars.find_one()
    #return template and data
    return render_template("index.html",mars=mars)

@app.route("/scrape")
def scraper():
    #run the scrape function
    mars = mongo.db.mars
    mars_data = mission_mars.scrape_news()
    mars_data = mission_mars.scrape_images()
    mars_data = mission_mars.scrape_facts()
    mars_data = mission_mars.scrape_hemispheres()

    #update mongo database
    mars.update({}, mars_data, upsert=True)
    return "yes!!!"

if __name__ == "__main__":
    app.run(debug=True)
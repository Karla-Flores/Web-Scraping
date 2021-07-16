# Import dependencies and set up
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Using flask_pymongo to set up mongo coneection



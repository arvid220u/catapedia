#!/usr/bin/env python3

import requests

from flask import *
app = Flask(__name__)
app.config["PREFERRED_URL_SCHEME"] = "https"

import config


@app.route("/")
def index():
    return render_template('index.html',    
                                            api_url = config.API_URL,
                                            css_filename  = config.CSS_FILENAME
    )



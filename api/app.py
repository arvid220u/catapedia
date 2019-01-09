#!/usr/bin/env python3


from flask import *
app = Flask(__name__)
app.config["PREFERRED_URL_SCHEME"] = "https"

from crossdomain import crossdomain

from flask import Response




@app.before_first_request
def logging_init():
    import logging
    logging.basicConfig(level=logging.DEBUG)



@app.route("/sampleapi/<string:text>")
@crossdomain(origin='*')
def sampleapi(text):
    """
    converts string to latex using wolfram API
    error is returned as \text{Error}

    parameters:
        text: the spoken string to be converted into latex code

    returns:
        latex code
    """

    return "sampleapi: " + text

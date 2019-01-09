#!/usr/bin/env python3


from flask import *
app = Flask(__name__)
app.config["PREFERRED_URL_SCHEME"] = "https"

from crossdomain import crossdomain

from flask import Response







# DATABASE
app.config["DATABASE"] = rlpt("app.db")

def connect_db():
    # use detect_types for easy datetime
    rv = sqlite3.connect(app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
    rv.row_factory = sqlite3.Row
    return rv

# get database
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# tear down database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()








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

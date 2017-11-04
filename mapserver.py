import flask
import data
import json
import config


#Flask server functionality sourced mostly from previous projects
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.api_key = CONFIG.API_KEY

@app.route("/")
@app.route("/index")
def index():
	#calls function that processes data from text file with locations and their info
	#and sends this via flask g object
	
	flask.g.datadict = data.process('venues.txt')
	#sends google maps api key via flask here
	flask.g.api_key = app.api_key
	
	
	return flask.render_template('geotest.html')


if __name__ == "__main__":
    # Standalone (not running under green unicorn or similar)
    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
    app.logger.info("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
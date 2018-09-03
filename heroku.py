from sys import argv

from bottle import *

@route("/")
def index():
	return """
<h2>heroku<h2>
"""


bottle.run(host='0.0.0.0', port=argv[1])

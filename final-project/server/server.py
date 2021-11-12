from config import app, FLASK_PORT

# import endpoints
from endpoint import *

app.run(port = FLASK_PORT, debug = True)
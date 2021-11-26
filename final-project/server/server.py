from config import app, db, FLASK_PORT

# import endpoints
from endpoint import *

# create all db tables
#db.create_all();

app.run(port = FLASK_PORT, debug = True)
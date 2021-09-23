# importações 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os 
 
# configurações 
app = Flask(__name__) 

# caminho do arquivo de banco de dados 
path = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(path, 'pessoas.db') 

# sqlalchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_FILE

# remover warnings 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from models.user import UserModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remove flask mofification use SQLAlchemy tracking
app.config['PROPAGATE_EXCEPTIONS'] = True  # use code error handling not flask's
app.secret_key = 'guiseppe'  #OAuth for this
api = Api(app)
db = SQLAlchemy(app) 


# SQLAlchemy creates tables before requests
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

# endpoints
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# on start
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

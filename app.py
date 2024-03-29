
from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from db import db
from resources.store import Store,StoreList
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLACLCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = "secretkey"
api = Api(app)

jwt = JWT(app, authenticate, identity) # create new endpoint /auth
# using flask restful we need not use jsonify as it does that for us behind the scene.
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=9000,debug=True)

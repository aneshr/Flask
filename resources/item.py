from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type= float,
    required=True,
    help="REQUIRED FIELD"
    )
    parser.add_argument('store_id',
    type= int,
    required=True,
    help="REQUIRED FIELD: Store ID"
    )

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message:': 'Item not found'}, 404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': 'Item with name {} already exist'.format(name)}, 400 # Bad request
        #req_data = request.get_json() # force=True-> donot look at header... silent=True -> return none, not give error
        req_data = Item.parser.parse_args()
        item= ItemModel(name,**req_data)
        try:
            item.save_to_db()
        except:
            return {"message:": "ERROR INSERTING"}, 500 #Internal Server ERROR
        return item.json(), 201 # code for created, 202  is for accepted the request.
    
    def delete(self,name):
        '''conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "delete from items where name=?"
        
        cur.execute(query, (name,))
        conn.commit()
        conn.close()
        return {'message': 'Item Deleted !!!'}'''
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message: ': 'Item Deleted'}
        return {'message: ' : 'Item not found'},404

    def put(self,name):
        data = Item.parser.parse_args() # other argument than price will not be used.

        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel( name, data['price'])
        if item is None:
            #try:
            #    updated_item.insert()
            #except:
            #    return {"message:": "error sds"}
            item = ItemModel(name,**data)
        else:
            '''try:
                updated_item.update()
            except:
                return {"message:": "error updating"}'''
            item.price = data['price']

        item.save_to_db()
        return item.json()
    

class ItemList(Resource):
    def get(self):
        return {'items:': list(map(lambda x: x.json(), ItemModel.query.all()))}
        #return {'items' : [item.json() for item in ItemModel.query.all()]}
        """conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "Select * from items"
        
        result = cur.execute(query)
        items = []

        for row in result:
            items.append({'name':row[0],'price':row[1]})
        conn.commit()
        conn.close()
        return {'ITEM': items}"""

        
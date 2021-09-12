import sqlite3
from db import db
class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    items = db.relationship('ItemModel', lazy='dynamic')
    

    def __init__(self,name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls,name):
        """conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "select * from items where name=?"

        result = cur.execute(query,(name,))
        row = result.fetchone()

        conn.close()

        if row:
            return cls(row[0], row[1]) # or *row"""
        return StoreModel.query.filter_by(name=name).first() # select * from items where name=name LIMTI 1
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        '''conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "update items SET price=? where name=?"
        
        cur.execute(query, (self.price,self.name))
        conn.commit()
        conn.close()'''
        

         
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        """conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "insert into items values (?,?)"

        cur.execute(query, (self.name,self.price))
        conn.commit()
        conn.close()"""
        
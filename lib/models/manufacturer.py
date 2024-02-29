# lib/models/manufacturer.py

# WHY not from models.__init__ ?
from models.__init__ import CURSOR, CONN

class Manufacturer:

    all = {}

    def __init__(self, name, industry, id = None):
        self.id = id
        self._name = name
        self._industry = industry

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                'Manufacturer name must be a non-empty string'
            )
    
    @property
    def industry(self):
        return self._industry
    
    @industry.setter
    def industry(self, industry):
        if isinstance(industry, str) and len(industry):
            self._industry = industry
        else:
            raise ValueError(
                'Industry must be a non-empty string'
            )
        
    @classmethod
    def create_table(cls):
        '''create a new table to persist the attributes of Manufacturer instances'''
        sql = '''
            CREATE TABLE IF NOT EXISTS manufacturers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            industry TEXT)
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        '''drop the table that persists the Manufacturer instances'''
        sql = '''
            DROP TABLE IF EXISTS manufacturers;
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def __repr__(self):
        return f"<Manufacturer {self.id}: {self.name}, {self.industry}>"
    
    def save(self):
        '''insert a new row with the name and location vaues of the current Manufacturer instance. 
        update object id attribute using the primary key value of new row.
        save the object in local dictionary using table row's primary key as dictionary key'''
        sql = '''
            INSERT INTO manufacturers (name, industry)
            VALUES (?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.industry))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, industry):
        '''initialize a new Manufacturer instance and save the object to the database'''
        manufacturer = cls(name, industry)
        manufacturer.save()
        return manufacturer
    
    def update(self):
        '''update the table row corresponding to the current Manufacturer instance'''
        sql = '''
            UPDATE manufacturers
            SET name = ?, industry = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.name, self.industry, self.id))
        CONN.commit()
    
    def delete(self):
        '''delete the table row corresponding to the current Manufacturer instance, 
        delete the dictionary entry, and reassign id attribute'''
        sql = '''
            DELETE FROM manufacturers
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        
        # Set the id to None
        self.id = None

    

    
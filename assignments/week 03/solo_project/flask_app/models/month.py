from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Month:
    db = 'jouleERD'
    def __init__(self, data):
        self.id = data['id']
        self.year = data['year']
        self.month = data['month']
        self.gas = data['gas']
        self.electric = data['electric']
        self.milesDriven = data['milesDriven']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM monthData;'
        results = connectToMySQL(cls.db).query_db(query)
        print (results)
        months = []
        for row in results:
            months.append(cls(row))
        return months

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM monthData WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM monthData WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO monthData (year, month, gas, electric, milesDriven, user_id) VALUES (%(year)s, %(month)s, %(gas)s, %(electric)s, %(milesDriven)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update monthData set year=%(year)s, month=%(month)s, gas=%(gas)s, electric=%(electric)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM monthData WHERE monthData.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
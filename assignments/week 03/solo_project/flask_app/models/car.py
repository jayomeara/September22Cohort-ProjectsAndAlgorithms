from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Car:
    db = 'jouleERD'
    def __init__(self, data):
        self.id = data['id']
        self.carName = data['carName']
        self.carMPG = data['carMPG']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM car;'
        results = connectToMySQL(cls.db).query_db(query)
        cars = []
        for row in results:
            cars.append(cls(row))
        return cars

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM car WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM car WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO car (carName, carMPG, user_id) VALUES (%(carName)s, %(carMPG)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update car set carName=%(carName)s, carMPG=%(carMPG)s, WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM car WHERE car.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
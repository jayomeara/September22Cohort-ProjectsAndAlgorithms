from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Asset:
    db = 'jouleERD'
    def __init__(self, data):
        self.id = data['id']
        self.homeName = data['homeName']
        self.homeSQft = data['homeSQft']
        self.zipCode = data['zipCode']
        self.vehicleName = data['vehicleName']
        self.vehicleMPG = data['vehicleMPG']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM asset;'
        results = connectToMySQL(cls.db).query_db(query)
        assets = []
        for row in results:
            assets.append(cls(row))
        return assets

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM asset WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM asset WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO asset (homeName, homeSQft, zipCode, vehicleName, vehicleMPG, user_id) VALUES (%(homeName)s, %(homeSQft)s, %(zipCode)s, %(vehicleName)s, %(vehicleMPG)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update asset set homeName=%(homeName)s, homeSQft=%(homeSQft)s, zipCode=%(zipCode)s, vehicleName=%(vehicleName)s, vehicleMPG=%(vehicleMPG)s, WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM asset WHERE asset.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
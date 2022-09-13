from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, month, car, asset

class Score:
    db = 'jouleERD'
    def __init__(self, data):
        self.id = data['id']
        self.currentScore = data['currentScore']
        self.gasTotal = data['gasTotal']
        self.gasMonths = data['gasMonths']
        self.gasScore = data['gasScore']
        self.electricMonths = data['electricMonths']
        self.electricityScore = data['electricityScore']
        self.vehicleMiles = data['vehicleMiles']
        self.vehicleMonths = data['vehicleMonths']
        self.vehicleScore = data['vehicleScore']
        self.placeholder = data['placeholder']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM score;'
        results = connectToMySQL(cls.db).query_db(query)
        print (results)
        scores = []
        for row in results:
            scores.append(cls(row))
        return scores

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM score WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM score WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def create(cls):
        query = 'INSERT INTO score (currentScore,`gasTotal`,`gasMonths`,`gasScore`,`electricTotal`,`electricMonths`,`electricityScore`,`vehicleMiles`,`vehicleMonths`,`vehicleScore`,placeholder,user_id) VALUES (0,0,0,0,0,0,0,0,0,0,0, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query)

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO score (currentScore, gasTotal, gasMonths, gasScore, electricTotal, electricMonths, electricityScore, vehicleMiles, vehicleMonths, vehicleScore, placeholder, user_id) VALUES (%(currentScore)s, %(gasTotal)s, %(gasMonths)s, %(electricTotal)s, %(gasScore)s, %(electricMonths)s, %(electricityScore)s, %(vehicleMiles)s, %(vehicleMonths)s, %(vehicleScore)s, %(placeholder)s, %(placeholder)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update score set currentScore=%(currentScore)s, gasTotal=%(gasTotal)s, gasMonths=%(gasMonths)s, gasScore=%(gasScore)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM score WHERE score.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def updateGasScore(cls):
        query = 'SELECT gas FROM monthData;'
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        gas = []
        for row in results:
            gas.append(cls(row))
        if len(gas) < 1:
            return False
        list_length = len(gas)
        sumOfElements = 0
        for i in range(list_length):
            sumOfElements=sumOfElements+gas[i]
        gasScore = sumOfElements/list_length
        query = 'update score set gasTotal = %(sumOfElements)s, gasScore= %(gasScore)s;'
        return query
        
    @classmethod
    def updateElectricScore(cls):
        query = 'SELECT electric FROM monthData;'
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        electric = []
        for row in results:
            electric.append(cls(row))
        if len(electric) < 1:
            return False
        list_length = len(electric)
        sumOfElements = 0
        for i in range(list_length):
            sumOfElements=sumOfElements+electric[i]
        electricScore = sumOfElements/list_length
        query = 'update score set electricTotal = %(sumOfElements)s, electricityScore= %(electricScore)s;'
        return query

    def updateVehicleScore(cls):
        query = 'SELECT milesDriven FROM monthData;'
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        miles = []
        for row in results:
            miles.append(cls(row))
        if len(miles) < 1:
            return False
        list_length = len(miles)
        sumOfElements = 0
        for i in range(list_length):
            sumOfElements=sumOfElements+miles[i]
        vehicleScore = sumOfElements/list_length
        query = 'update score set vehicleMiles = %(sumOfElements)s, vehicleScore= %(vehicleScore)s;'
        return query

# gas = [100, 150, 125] length = 3
# sum[list]/length == Score.Update(gasScore)



    #     query = 'SELECT * FROM score;'
    #     results = connectToMySQL(cls.db).query_db(query)
    #     print (results)
    #     newScores = []
    #     for row in results:
    #         newScores.append(cls(row))

        # pull in month, car, and asset data
        # convert string to FLOAT
        # do some math
        # run the update on the score
        # = newScores
        # update(newScores)

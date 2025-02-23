from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.month import Month
from flask_app.models.asset import Asset
from flask_app.models.car import Car
from flask_app.models.score import Score

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect('/dashboard/')

@app.route('/register/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        newUser = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash('Something went wrong')
            return redirect('/')
        else:
            Score.create()
            session['user_id'] = id
            flash("You are now logged in")
            return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash('That email is not in our database')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password')
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("You are now logged in, Welcome back")
        return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash("Please Login")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    Score.updateGasScore()
    Score.updateElectricScore()
    Score.updateVehicleScore()
    # Score.updateJoule()
    theUser = User.getOne(data)
    months = Month.getAll()
    assets = Asset.getAll()
    cars = Car.getAll()
    scores = Score.getAll()
    return render_template('dashboard.html', user=theUser, months=months, assets=assets, cars=cars, scores=scores)

@app.route('/addMonth/')
def addMonth():
    if 'user_id' not in session:
        flash("Please login in")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('addMonth.html', user=theUser)

@app.route('/createMonth/', methods=['post'])
def createMonth():
    data = {
        'year': request.form['year'],
        'month': request.form['month'],
        'gas': request.form['gas'],
        'electric': request.form['electric'],
        'milesDriven': request.form['milesDriven'],
        'user_id': request.form['user_id'],
    }
    Month.save(data)
    flash("Month Saved")
    return redirect('/dashboard/')

@app.route('/updateMonth/<int:monthID>/')
def updateMonth(monthID):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        monthData = {
            'id': monthID
        }
        month = Month.getOne(monthID)
        return render_template('editAsset.html', user=theUser, month=month)

@app.route('/editMonth/<int:monthID>/', methods=['post'])
def updatedMonth(monthID):
    data = {
        'year': request.form['year'],
        'month': request.form['month'],
        'gas': request.form['gas'],
        'electric': request.form['electric'],
        'milesDriven': request.form['milesDriven'],
        'user_id': request.form['user_id'],
    }
    Month.save(data)
    flash("Month Saved")
    return redirect('/dashboard/')

@app.route('/addAsset/')
def addAsset():
    if 'user_id' not in session:
        flash("Please login in")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('addAsset.html', user=theUser)

@app.route('/createAsset/', methods=['post'])
def createAsset():
    data = {
        'homeName': request.form['homeName'],
        'homeSQft': request.form['homeSQft'],
        'zipCode': request.form['zipCode'],
        'user_id': request.form['user_id'],
    }
    Asset.save(data)
    flash("Asset Saved")
    return redirect('/dashboard/')

@app.route('/createCar/', methods=['post'])
def createCar():
    data = {
        'carName': request.form['carName'],
        'carMPG': request.form['carMPG'],
        'user_id': request.form['user_id'],
    }
    Car.save(data)
    flash("Vehicle Saved")
    return redirect('/dashboard/')

@app.route('/deleteMonth/<int:monthID>/')
def deleteMonth(monthID):
    if 'user_id' not in session:
        return redirect('/')
    else:
        month = {
            'id': monthID
        }
    Month.delete(month)
    return redirect('/')

@app.route('/deleteHome/<int:homeID>/')
def deleteHome(homeID):
    if 'user_id' not in session:
        return redirect('/')
    else:
        month = {
            'id': homeID
        }
    Month.delete(homeID)
    return redirect('/')
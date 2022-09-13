from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.month import Month
from flask_app.models.asset import Asset
from flask_app.models.car import Car

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
            session['user_id'] = id
            flash("You are now logged in")
            return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data) # check if the email is in the database
    if not user: # if not let them know
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
    theUser = User.getOne(data)
    months = Month.getAll()
    assets = Asset.getAll()
    cars = Car.getAll()
    return render_template('dashboard.html', user=theUser, months=months, assets=assets, cars=cars)

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
        'vehicleName': request.form['vehicleName'],
        'vehicleMPG': request.form['vehicleMPG'],
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
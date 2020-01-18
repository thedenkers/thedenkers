'''
Routes Module
All the routes to the app are defined here.
'''
import os
from flask import render_template, flash, redirect, request, url_for
from flask import jsonify

from app import app, mongo
from app.forms import LoginForm

from model_test import predict_image

ALLOWED_EXTENSIONS = { 'jpg', 'png', 'jpeg' }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_place_detail(id):
    cursor = mongo.db.places.find({"id":id})
    print(cursor)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password{}, remember_me={}'.format(
            form.username.data, form.password.data,form.remember_me.data),'info')
        return redirect('/index')
    return render_template('admin_login.html', title='Admin Login', form=form)

@app.route('/admin_dashboard')
# @login_required
def admin_dashboard():
    return render_template('admin_dashboard.html', title='Admin Dashboard')

@app.route('/extras')
def extras():
    return render_template('extras.html', title='Jaadu')

@app.route('/events')
def events():
    return render_template('events.html', title='Events',mongo=mongo)

@app.route('/add_event', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1].lower()
            filename = "abcd" + '.' + ext
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/explore')
def explore():
    return render_template('explore.html', title='Explore')

@app.route('/place/<id>')
def place(id):
    return render_template('place.html', title='Explore', place=place)





# -----  API Part Begins Here ------

@app.route('/api/places')
def api_get_places():
    return jsonify({"data":['a','b']})

@app.route('/api/place/<id>')
def api_get_place(id):
    user = mongo.db.places.find({"id": 1 })
    print("printd")
    return "ufbalj"
    # return jsonify(response)

@app.route('/api/get_detected_place')
def get_detected_place():
    id = 1
    user = mongo.db.places.find_one({"id": 1})
    print(type(user))
    user = dict(user)
    return user

@app.route('/api/send_image', methods = ['POST','GET'])
def send_image():
    if request.method == 'POST':
        imag=request.form['imageString']
        x=predict_image(imag)
        print(x,"Base64\n\n\n\n\n",x,imag)

    return x


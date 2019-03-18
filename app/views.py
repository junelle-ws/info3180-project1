"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.forms import MyForm
import os
import datetime
# from app import app
from app.models import UserProfile
from werkzeug.utils import secure_filename



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Junelle Wilmot-Simpson")
    
    
    

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    myform = MyForm()
    """Render the website's  add profile page"""
    
    if request.method == 'POST':

        if myform.validate_on_submit() :
         
            first = myform.firstname.data
            last = myform.lastname.data
            emal = myform.email.data
            location = myform.location.data
            photo = myform.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gender = myform.Gender.data
            des = myform.description.data
            x  = datetime.datetime.now()
            date = x.strftime("%x")
            photograph = str(photo)
            user = UserProfile(first_name = first ,last_name = last , email= emal, location = location, description = des, gender= gender , date = date ,photo = filename)
            db.session.add(user)
            db.session.commit()
            flash('New user was successfully added')
            return redirect(url_for('profiles'))
            
            
 
    return render_template('profile.html', forms = myform)





###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profiles', methods=['POST', 'GET'])
def profiles():
    users = db.session.query(UserProfile).all()
    if request.method == 'GET':
        return render_template('profiles.html', users = users)
   


@app.route('/profile/<userid>', methods=['POST', 'GET'])
def user(userid):
    user = UserProfile.query.filter_by(id = userid ).first()
    if request.method=='GET':
        return render_template('user.html', user =user )

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger' )
            
            
            
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
    
    
def get_uploaded_images():
    lst=[]
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
                lst.append(file)
    return lst

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

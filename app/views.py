"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime
i = datetime.date(2019, 2, 7)
from app.forms import ProfileForm
from app.models import User
from . import db
import os
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
    return render_template('about.html', name="Mary Jane")
    

def format_date_joined(time):
    return time.strftime("%B, %Y")
    
    

@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
                firstname = form.firstname.data
                lastname = form.lastname.data
                gender = form.gender.data
                email = form.email.data
                location = form.location.data
                biography = form.biography.data
                created_on = str(datetime.datetime.now()).split()[0]
                photo = form.fileupload.data
                photo_name = secure_filename(photo.filename)
                
                user = User(firstname, lastname, gender, email, location, biography, created_on, photo_name)
                
                db.session.add(user)
                db.session.commit()
                
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
                flash("Profile Added", "success")
                return redirect(url_for("profiles"))
    return render_template('profile.html', form=form)

    
@app.route("/profiles")
def profiles():
    users = User.query.all()
    profiles = []
    
    for user in users:
        profiles.append({"pic": user.photo, "f_name":user.firstname, "l_name": user.lastname, "gender": user.gender, "location":user.location, "id":user.id})
    
    return render_template("profiles.html", profiles = profiles)


    






@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

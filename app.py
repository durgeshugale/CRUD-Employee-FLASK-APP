from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    email = db.Column(db.String(100))
    maritalstatus = db.Column(db.String(100))
    bloodgroup = db.Column(db.String(100))

    def __init__(self, id, firstname,lastname, gender,dob,phone,branch,email,maritalstatus,bloodgroup):
        self.id =id
        self.firstname =firstname
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.branch = branch
        self.email = email
        self.maritalstatus = maritalstatus
        self.bloodgroup =bloodgroup


# This is the index route where we are going to
# query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees=all_data)

@app.route('/add')
def add():
    return render_template("add.html")


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['fn']
        lastname = request.form['ln']
        gender = request.form['gender']
        dob = request.form['dob']
        phone = request.form['mobile']
        branch = request.form['br']
        email = request.form['email']
        maritalstatus = request.form['ms']
        bloodgroup = request.form['bg']

        my_data = Data(id,firstname,lastname,gender,dob,phone,branch,email,maritalstatus,bloodgroup)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


# This route is for deleting our employee
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


# this is our update route where we are going to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        id = request.form['id']
        firstname = request.form['fn']
        lastname = request.form['ln']
        gender = request.form['gender']
        dob = request.form['dob']
        phone = request.form['mobile']
        branch = request.form['br']
        email = request.form['email']
        maritalstatus = request.form['ms']
        bloodgroup = request.form['bg']
        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))


# This route is for viewing our employee
# @app.route('/view/<id>/')
# def view(id):
#     all_data = Data.query.get(id).all()
#
#     return render_template("view.html", employee=all_data)

if __name__ == "__main__":
    app.run(debug=True)

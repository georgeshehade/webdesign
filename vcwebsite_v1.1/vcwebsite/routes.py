import os
import secrets

from flask.templating import render_template_string
from vcwebsite.models import User, Values
from vcwebsite.datahandler import Datahandler
from flask import render_template, url_for, flash, redirect, request
from vcwebsite.forms import RegistrationForm, LoginForm, UpdateAccountForm,ValuesForm, AdminForm
from vcwebsite import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from vcwebsite.clustering.clusterhandler import ClusterHandler

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    
    handler = Datahandler()
    form = AdminForm()
    if form.is_submitted():
        flash(f"got into submit", "success")
        if form.backup_db.data:
            handler.make_backup()

        elif form.create_db.data:
            handler.create_database()
        
        elif form.remove_db.data:
            handler.remove_database()

        elif form.drop_db.data:
            handler.drop_database()

        elif form.get_centroids.data:
            handler.get_cluster_centroids()

        elif form.train_cluster_model:
            try:
                handler.train_cluster_model()
            except:
                flash(f"Add more indices to the database!", "danger")

        elif form.update_user_clusters:
            handler.update_user_clusters()
    return render_template("admin.html", form=form)

@app.route("/explore", methods=['GET', 'POST'])
def explore():
    form = ValuesForm()
    if form.validate_on_submit():
        
        clusterhandler = ClusterHandler(db, Values, User, current_user)

        values = [form.value1.data, form.value2.data, form.value3.data]
        clusterhandler.store_values(values)
        datapoint = clusterhandler.create_datapoint(form.value1.data, form.value2.data, form.value3.data)
        clusterhandler.store_datapoint(datapoint)
        flash(f"{datapoint}", "success")
        clusterhandler.One_cluster_no(datapoint, current_user)

        flash(f"Your values are stored and your results can be accessed at the result page", "success")
        
        return redirect(url_for('results'))
    return render_template("explore.html", form=form)

@app.route("/results")
def results():
    
    query = db.session.execute("SELECT user.username, user.cluster FROM User")
    data = query.fetchall()
    return render_template("results.html", data=data)


@app.route("/about")
def about():
    return render_template("aboutus.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created you are now able to log in", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title="Account",form=form)
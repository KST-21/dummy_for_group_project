from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from .password_encrypter import hash_password, verify_password
from flask_login import login_user, login_required, logout_user, current_user
from email_verification import EmailVerifier


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        name = request.form.get("name")
        salary = request.form.get("salary")
        
        if email and len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif password1 and len(password1) < 8:
            flash("Password must have at least 8 characters.", category="error")
        elif name and len(name) < 2:
            flash("Name must be greater than 2 characters.", category="error")
        else:
            return redirect(url_for("auth.verification"))
            # flash("Account created!", category="success")
            # new_user = User(email=email, password=hash_password(password1), fullname=name, salary=salary)
            # db.session.add(new_user)
            # db.session.commit()

    return render_template("register.html")

email_verifier = EmailVerifier()
user_email = "www.kst21112002@gmail.com"

@auth.route("/verification", methods=["GET", "POST"])
def verification():
    # if send again should send new code
    if request.method == "POST":
        print("post")
        verification_code = request.form.get("verification_code")
        if verification_code and email_verifier.is_same_code(verification_code):
            print("equal")
            return redirect(url_for("views.home"))
        # if verification_code == correct_verification_code: -> create account -> redirect to home
        
        return render_template("verification.html")
    else:
        print("get")
        email_verifier.send_email(user_email)

        return render_template("verification.html")

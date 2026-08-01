from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, User
from forms import RegisterForm

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        # Check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("Email already exists!", "danger")
            return render_template("register.html", form=form)

        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data
        )

        # Hash password
        user.set_password(form.password.data)

        # Save to database
        db.session.add(user)
        db.session.commit()

        flash("Account created successfully!", "success")

        return redirect(url_for("home"))

    return render_template("register.html", form=form)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
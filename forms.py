from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import FloatField, SelectField, TextAreaField


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match.")
        ]
    )

    submit = SubmitField("Create Account")

class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Login")

class ExpenseForm(FlaskForm):

    amount = FloatField(
        "Amount (₹)",
        validators=[DataRequired()]
    )
    category = SelectField(
        "Category",
        choices=[
            ("Food", "🍔 Food"),
            ("Groceries", "🛒 Groceries"),
            ("Travel", "🚗 Travel"),
        ("Fuel", "⛽ Fuel"),
        ("Shopping", "🛍 Shopping"),
        ("Bills", "💡 Bills"),
        ("Electricity", "⚡ Electricity"),
        ("Water", "💧 Water"),
        ("Internet", "🌐 Internet"),
        ("Mobile Recharge", "📱 Mobile Recharge"),
        ("Rent", "🏠 Rent"),
        ("Education", "📚 Education"),
        ("Healthcare", "🏥 Healthcare"),
        ("Medicine", "💊 Medicine"),
        ("Entertainment", "🎬 Entertainment"),
        ("Subscription", "🎵 Subscription"),
        ("Clothing", "👕 Clothing"),
        ("Gym", "🏋️ Gym"),
        ("Gifts", "🎁 Gifts"),
        ("Investment", "📈 Investment"),
        ("Savings", "💰 Savings"),
        ("Pet", "🐶 Pet"),
        ("Family", "👨‍👩‍👧 Family"),
        ("Office", "💼 Office"),
        ("Miscellaneous", "📦 Miscellaneous")
        ]
    )

    description = TextAreaField("Description")

    submit = SubmitField("Add Expense")
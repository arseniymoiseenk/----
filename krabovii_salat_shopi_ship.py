from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
orders = {}

Dict = {}
prices = []
List = []
List1 = []


@app.route("/Chosen")
def choosen():
    if orders != {}:
        prices.append(int(orders['Цена']))
        List.append(orders["Количество"])
        List1.append(orders["Название"])
        return render_template("Choosen.html",amount=List, name=List1, price=sum(prices))
    else:
        return render_template("Choosen.html")


@app.route("/buy_krabovii_salat", methods=['GET','POST'])
def buy_krabovii_salat():
    amount = request.form.get("amount")
    name = request.form.get("name")
    if name == 'Звичайний':
        orders["Количество"] = amount
        orders["Название"] = name
        orders['Цена'] = int(amount) * 90

    if name == 'Крутой':
        orders["Количество"] = amount
        orders["Название"] = name
        orders['Цена'] = int(amount) * 734

    if name == 'Красавчик':
        orders["Количество"] = amount
        orders["Название"] = name
        orders['Цена'] = int(amount) * 993
    return render_template("index.html")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(40), nullable=False)


@app.route("/")
def register():
    users = User.query.all()
    users = []
    return render_template("register.html", users=users)


@app.route("/h")
def index():
    return render_template("index.html")


@app.route("/Things")
def things():
    return render_template("Things_to_buy.html")


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    new_user = User(
        name=name,
        surname=surname,
        email=email,
        username=username,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
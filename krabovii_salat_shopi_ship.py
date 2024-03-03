from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/vibor_svyatkovi")
def vibor_svyatkovih():
    return render_template("krabovii_salati_vibor_svyatkovi.html")
@app.route("/vibor_salati_every_day")
def vibor_salatov_every_day():
    return render_template("salati_every_day.html")
@app.route("/vibor_premium")
def vibor_premium():
    return render_template("premium_salati.html")
@app.route("/korzina")
def korzina():
    return render_template("krabovii_salat_korzina.html")
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
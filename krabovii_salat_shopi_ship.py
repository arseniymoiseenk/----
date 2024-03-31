from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)
class LiteraryFormat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100))
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    books = db.relationship("Book", backref="author")
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    published_year = db.Column(db.Integer)
    format_id = db.Column(db.Integer, db.ForeignKey("literary_format.id"))
    format = db.relationship("LiteraryFormat", backref="books")
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))


@app.route("/get_books_by_author/<author_name>", methods=["GET"])
def get_books_by_author(author_name):
    author = Author.query.filter_by(name=author_name).first()
    if author:
        books = [book.title for book in author.books]
        return jsonify(books)
    return "lol"
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
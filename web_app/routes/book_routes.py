# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
#from web_app.models import db, Book, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
# joson format book list
def list_books_json():
    print("Requested books in JSON format")
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    #book_records = Book.query.all()
    #book_response = parse_records(book_records)
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
# note this match the <form action in new_book.html
def create_book():
    print("New form entry:", dict(request.form))
    return jsonify({"message":"Book created successfully", "book":dict(request.form)})
    # new_book = Book(genre=request.form["genre"], title=request.form["title"], author=request.form["author_name"])
    # print(new_book)

    # db.session.add(new_book)
    # db.session.commit()

    # flash(f"Book '{new_book.title}' created successfully!", "success")
    # return redirect(f"/books")
from flask import Flask, jsonify, request
import json

create_app = Flask(__name__)
books = [{'id': 1, 'title': 'Green Beans', 'author': 'Farmer'}, {'id': 2, 'title': 'Slurp', 'author': 'Barista'}]

nextID = 3
4

@create_app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@create_app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id: int):
    book = get_book(id)
    if book is None:
        return jsonify({ 'error': 'No book'}), 404
    return jsonify(book)

def get_book(id):
 return next((b for b in books if b['id'] == id), None)

def book_exists(book):
    for key in book.keys():
        if key == 'title' or key == 'author' or key =='id':
            return True
    return False

@create_app.route('/books', methods=['POST']) #add
def post_book():
    global nextID
    book = request.json
    if not book_exists(book):
        return jsonify({'error': 'Ivalid book'}), 400
    book['id'] = nextID
    nextID += 1
    books.append(book)
    return jsonify({ 'location': f'/books/{book["id"]}' }), 200

@create_app.route('/books/<int:id>', methods=['PUT']) #update
def put_book(id: int):
    new_book = request.json
    if not book_exists(new_book):
        return jsonify({'error': 'Invalid book'}), 400
    return jsonify(new_book), 200

@create_app.route('/books/<int:id>', methods=['DELETE'])
def delete_books(id: int):
    global books
    book = request.json
    if book is None:
        return jsonify({'error': 'No book'}), 404
    books = [b for b in books if b['id'] != id]
    return jsonify(book), 200

if __name__ == '__main__':
    create_app.run(debug=True)
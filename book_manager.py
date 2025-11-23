
import random

BOOKS = {}
used_ids = set()

def generate_book_id():#will generate a id for the recieved book
    while True:
        book_id = random.randint(1000, 9999)
        if book_id not in used_ids:
            used_ids.add(book_id)
            return book_id

def add_book(title, author):
    book_id = generate_book_id()
    BOOKS[book_id] = {'title': title, 'author': author}
    print(f"Book '{title}' added with ID: {book_id}")
    return book_id

def get_book_details(book_id):
    return BOOKS.get(book_id)

def get_all_books():
    # will show all the books added
    return BOOKS

def delete_book(book_id):
    if book_id in BOOKS:
        del BOOKS[book_id]
        used_ids.discard(book_id)
        print(f"Book ID {book_id} deleted successfully.")
        return True
    return False

def search_books(search_term):
    results = {}
    search_term = search_term.lower()
    for book_id, details in BOOKS.items():
        if (search_term in details['title'].lower() or 
            search_term in details['author'].lower()):
            results[book_id] = details
    return results

if __name__ == '__main__':
    add_book("The Coder's Journey", "A. Developer")
    print(get_book_details(1000))
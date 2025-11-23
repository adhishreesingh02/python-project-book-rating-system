import random
from book_manager import get_book_details

RATINGS = {}
used_user_ids = set()

def generate_user_id():
    #generate the user id in which you want to store your added book
    while True:
        user_id = random.randint(100, 999)
        if user_id not in used_user_ids:
            used_user_ids.add(user_id)
            return user_id

def submit_rating(book_id, user_id=None, rating=None):
    # give the ratings for the book you want 
    if user_id is None:
        user_id = generate_user_id()
    
    if rating is None:
        try:
            rating = int(input(f"Enter rating for book ID {book_id} (1-5): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            return False
    
    if not 1 <= rating <= 5:
        print("Error: Rating must be between 1 and 5.")
        return False
        
    if get_book_details(book_id) is None:
        print(f"Error: Book ID {book_id} not found.")
        return False
        
    if book_id not in RATINGS:
        RATINGS[book_id] = []
    
    for existing_rating in RATINGS[book_id]:
        if existing_rating['user_id'] == user_id:
            print(f"User {user_id} has already rated this book.")
            return False
        
    RATINGS[book_id].append({'rating': rating, 'user_id': user_id})
    print(f"Rating {rating}/5 submitted for Book ID {book_id} by User {user_id}.")
    return True

def calculate_average_rating(book_id):
    # it will add average and give you result
    book_ratings = RATINGS.get(book_id, [])
    
    if not book_ratings:
        return 0.0
        
    total_rating = sum(item['rating'] for item in book_ratings)
    average = total_rating / len(book_ratings)
    return round(average, 2)

def get_ratings_data():
    return RATINGS

def get_book_ratings_summary():
    # will give summary for the complete data
    from book_manager import get_all_books
    all_books = get_all_books()
    summary = {}
    
    for book_id, book_details in all_books.items():
        avg_rating = calculate_average_rating(book_id)
        ratings_list = RATINGS.get(book_id, [])
        total_ratings = len(ratings_list)
        
        distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for rating_item in ratings_list:
            distribution[rating_item['rating']] += 1
        
        summary[book_id] = {
            'title': book_details['title'],
            'author': book_details['author'],
            'average_rating': avg_rating,
            'total_ratings': total_ratings,
            'distribution': distribution
        }
    
    return summary

def get_popular_books(limit=5):
    books_with_ratings = []
    for book_id, ratings in RATINGS.items():
        book_details = get_book_details(book_id)
        if book_details:
            books_with_ratings.append({
                'book_id': book_id,
                'title': book_details['title'],
                'author': book_details['author'],
                'total_ratings': len(ratings),
                'average_rating': calculate_average_rating(book_id)
            })
    
    books_with_ratings.sort(key=lambda x: x['total_ratings'], reverse=True)
    return books_with_ratings[:limit] # give rating

if __name__ == '__main__':
    print("Testing ratings manager...")
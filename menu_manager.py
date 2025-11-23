import book_manager
import ratings_manager
import random

def display_menu():
#     here the menu will come in which we have to select the option for which we want to get reslt
    print("\n" + "="*50)
    print(" BOOK RATING SYSTEM")
    print("="*50)
    print("1. Add a new book")
    print("2. Submit a rating")
    print("3. View average rating for a book")
    print("4. View all books with ratings")
    print("5. View ratings summary")
    print("6. Search books")
    print("7. View popular books")
    print("8. Delete a book")
    print("9. Exit")
    print("="*50)

def add_book_interaction():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    
    if title and author:
        book_id = book_manager.add_book(title, author)
        print(f" Book added successfully with ID: {book_id}")
    else:
        print(" Error: Title and author cannot be empty.")

def submit_rating_interaction():
#     the user is asked to give rating to the selected book
    try:
        book_id = int(input("Enter book ID to rate: "))
        book_details = book_manager.get_book_details(book_id)
        
        if not book_details:
            print(f" Book ID {book_id} not found.")
            return
            
        print(f" Rating: '{book_details['title']}' by {book_details['author']}")
        
        use_random = input("Use random user ID? (y/n): ").strip().lower()
        user_id = None
        
        if use_random == 'y':
            user_id = ratings_manager.generate_user_id()
            print(f" Assigned random User ID: {user_id}")
        else:
            try:
                user_id = int(input("Enter your user ID: "))
            except ValueError:
                print(" Error: Please enter a valid user ID.")
                return
        
        try:
            rating = int(input("Enter rating (1-5): "))
        except ValueError:
            print(" Error: Please enter a valid rating.")
            return
            
        if ratings_manager.submit_rating(book_id, user_id, rating):
            print(" Rating submitted successfully!")
        else:
            print(" Failed to submit rating.")
            
    except ValueError:
        print(" Error: Please enter valid numbers.")

def view_average_rating_interaction():
#      here we can see ratings 
    try:
        book_id = int(input("Enter book ID to view average rating: "))
        avg_rating = ratings_manager.calculate_average_rating(book_id)
        book_details = book_manager.get_book_details(book_id)
        
        if book_details:
            print(f"\n Book: '{book_details['title']}' by {book_details['author']}")
            print(f" Average Rating: {avg_rating}/5")
            total_ratings = len(ratings_manager.get_ratings_data().get(book_id, []))
            print(f" Total Ratings: {total_ratings}")
            
            ratings_data = ratings_manager.get_ratings_data().get(book_id, [])
            if ratings_data:
                distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
                for rating_item in ratings_data:
                    distribution[rating_item['rating']] += 1
                
                print(" Rating Distribution:")
                for stars in range(5, 0, -1):
                    count = distribution[stars]
                    bar = "█" * count
                    print(f"   {stars} stars: {bar} ({count})")
        else:
            print(f" Book ID {book_id} not found.")
            
    except ValueError:
        print(" Error: Please enter a valid book ID.")

def view_all_books_interaction():
#    ccan see the book and ratings 
    all_books = book_manager.get_all_books()
    if all_books:
        print("\n" + "="*70)
        print("                      ALL BOOKS")
        print("="*70)
        for book_id, details in all_books.items():
            avg_rating = ratings_manager.calculate_average_rating(book_id)
            total_ratings = len(ratings_manager.get_ratings_data().get(book_id, []))
            rating_display = f"{avg_rating}/5 ({total_ratings} ratings)" if total_ratings > 0 else "No ratings yet"
            print(f" ID: {book_id} - '{details['title']}' by {details['author']} - {rating_display}")
        print(f"\nTotal books in system: {len(all_books)}")
    else:
        print(" No books in the system. Add some books first!")

def view_ratings_summary_interaction():
# here we can see the whole results with the input given by the user the output which the user wants
    summary = ratings_manager.get_book_ratings_summary()
    if summary:
        print("\n" + "="*80)
        print("                          RATINGS SUMMARY")
        print("="*80)
        for book_id, data in summary.items():
            print(f" ID: {book_id}")
            print(f"   Title: {data['title']}")
            print(f"   Author: {data['author']}")
            print(f"   Average Rating: {data['average_rating']}/5")
            print(f"   Total Ratings: {data['total_ratings']}")
            
            if data['total_ratings'] > 0:
                print("   Rating Distribution:")
                for stars in range(5, 0, -1):
                    count = data['distribution'][stars]
                    percentage = (count / data['total_ratings']) * 100
                    bar = "█" * max(1, int(percentage / 10))
                    print(f"      {stars} stars: {bar} {count} ({percentage:.1f}%)")
            print("-" * 50)
    else:
        print("No books available for summary.")

def search_books_interaction(): 
    search_term = input("Enter book title or author to search: ").strip()
    if search_term:
        results = book_manager.search_books(search_term)
        if results:
            print(f"\n Found {len(results)} book(s) matching '{search_term}':")
            for book_id, details in results.items():
                avg_rating = ratings_manager.calculate_average_rating(book_id)
                total_ratings = len(ratings_manager.get_ratings_data().get(book_id, []))
                rating_display = f"{avg_rating}/5 ({total_ratings} ratings)" if total_ratings > 0 else "No ratings yet"
                print(f"   ID: {book_id} - '{details['title']}' by {details['author']} - {rating_display}")
        else:
            print(f" No books found matching '{search_term}'.")
    else:
        print(" Please enter a search term.")

def view_popular_books_interaction():
#     if we want to see top ratings among many books
    try:
        limit = int(input("How many popular books to show? (default 5): ") or 5)
    except ValueError:
        limit = 5
    
    popular_books = ratings_manager.get_popular_books(limit)
    if popular_books:
        print(f"\n TOP {len(popular_books)} POPULAR BOOKS")
        print("="*60)
        for i, book in enumerate(popular_books, 1):
            print(f"{i}. '{book['title']}' by {book['author']}")
            print(f"   ID: {book['book_id']} | Avg Rating: {book['average_rating']}/5 | Total Ratings: {book['total_ratings']}")
            print()
    else:
        print(" No books with ratings yet.")

def delete_book_interaction():
#     if we want to delete some books from the library
    try:
        book_id = int(input("Enter book ID to delete: "))
        if book_manager.delete_book(book_id):
            print(" Book deleted successfully!")
        else:
            print(f" Book ID {book_id} not found.")
    except ValueError:
        print(" Error: Please enter a valid book ID.")

def main():
    print("Welcome to the Book Rating System!")
    print("Manage your book collection and ratings efficiently.")
    print("Features: Random ID generation, Rating analytics, Book search")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            add_book_interaction()
        elif choice == '2':
            submit_rating_interaction()
        elif choice == '3':
            view_average_rating_interaction()
        elif choice == '4':
            view_all_books_interaction()
        elif choice == '5':
            view_ratings_summary_interaction()
        elif choice == '6':
            search_books_interaction()
        elif choice == '7':
            view_popular_books_interaction()
        elif choice == '8':
            delete_book_interaction()
        elif choice == '9':
            print("\nThank you for using the Book Rating System! ")
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1-9.")
main()
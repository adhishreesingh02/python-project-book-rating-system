import book_manager
import ratings_manager

def delete_book_interaction():
    
    try:
        book_id = int(input("Enter book ID to delete: "))
        
        if book_manager.delete_book(book_id):
            ratings_manager.clean_ratings_on_delete(book_id)
            print(" Book deleted successfully and ratings removed!")
        else:
            print(f" Book ID {book_id} not found.")
    except ValueError:
        print(" Error: Please enter a valid book ID.")

def main():
    pass 
if __name__ == "__main__":
    main() # call the function 
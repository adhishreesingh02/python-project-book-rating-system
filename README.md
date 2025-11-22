#  Book Rating and Analytics System

## Project Title
**Book Rating and Analytics System** 

## Overview of the Project
This project is a modular, command-line application designed to simulate a fundamental component of a modern book review platform. It provides a structured environment for managing book records, collecting user ratings, and generating real-time analytical reports.

The system was developed as part of a flipped course evaluation to apply core subject concepts in **modular architecture**, **data processing**, and **error handling**.

## Features
The application is built around three major functional modules:

* **Book Management (CRUD):** Allows for adding, retrieving, and deleting book records.
* **Rating Processing:** Handles user submission of ratings (1-5) and calculates the average rating for each book.
* **Reporting & Analytics:** Generates reports, including top-rated book lists and detailed statistics for individual books (e.g., average rating and total submissions).

## Technologies/Tools Used
* **Core Language:** Python 3
* **Version Control:** Git & GitHub 
* **Data Storage:** In-memory Python Dictionaries (simulating a database schema)

## Steps to Install & Run the Project
1.  **Clone the Repository:**
    ```bash
    git clone [Your-GitHub-Repo-URL]
    cd book-rating-system
    ```
2.  **Ensure Python is Installed:** This project requires Python 3.x.
3.  **Run the Main Script:** Execute the interactive command-line interface.
    ```bash
    python menu_manager.py
    ```
4.  **Interaction:** Follow the on-screen main menu (1-9) to add books, submit ratings, and view reports.

## Instructions for Testing
The system includes built-in validation to ensure reliability:

* **Functional Testing:** Select option **3 (View Reports)** to confirm that average ratings are correctly calculated and top-rated lists are accurately sorted.
* **Validation Testing:** Attempt to submit a rating outside the 1-5 range (e.g., 0 or 6) to verify that the system correctly displays an "Error: Rating must be between 1 and 5" message.

---

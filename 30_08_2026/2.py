class LibraryBook:
    # Class Variable: Shared by all instances
    total_books = 0
    
    def __init__(self, title, author):
        # Instance Variables: Unique to each object
        self.title = title
        self.author = author
        self.is_issued = False
        
        # Increment the class variable when a new book is created
        LibraryBook.total_books += 1

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"Book '{self.title}' issued to user.")
        else:
            print(f"Book '{self.title}' was already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"Book '{self.title}' returned by user.")
        else:
            print(f"Book '{self.title}' is not currently issued.")

    # Destructor: Called when object is deleted or garbage collected
    def __del__(self):
        print(f"Object for book '{self.title}' destroyed.")

# Main Program Execution
if __name__ == "__main__":
    print("Creating books...")
    
    # Create 3 books
    b1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald")
    b2 = LibraryBook("1984", "George Orwell")
    b3 = LibraryBook("To Kill a Mockingbird", "Harper Lee")

    print(f"Total books created so far: {LibraryBook.total_books}") # Output: 3
    
    print("\n--- Issuing and Returning Books ---")
    
    # Issue one book
    b1.issue_book() 
    # Output: Book 'The Great Gatsby' issued to user.

    # Return the same book
    b1.return_book()
    # Output: Book 'The Great Gatsby' returned by user.

    print(f"\nFinal Total Books Count (Class Variable): {LibraryBook.total_books}") 
    # Output: 3 (Shows class variable persists across instances)
    
    # Delete objects to demonstrate destructor
    del b1, b2, b3
    
    # Note: In some environments/destructors order varies, but __del__ will run.
    # Expected output near end: Object for book 'The Great Gatsby' destroyed... etc.

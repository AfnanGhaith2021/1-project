class Library:
    def init(self):
        self.books = [
            {"title": "C++ Primer", "author": "Stanley Lippman", "status": "Available"},
            {"title": "Clean Code", "author": "Robert Martin", "status": "Borrowed"},
            {"title": "Data Structures", "author": "Ellis Horowitz", "status": "Available"},
        ]

    def display_books(self):
        print("\n" + "="*35)
        print("   Library Book List")
        print("="*35)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book['title']} | Author: {book['author']} | Status: {book['status']}")
        print("="*35)

    def search_book(self):
        query = input("\nEnter book title to search: ")
        found = False
        for book in self.books:
            if query.lower() in book['title'].lower():
                print(f"✅ Found: {book['title']} by {book['author']}")
                found = True
                break
        if not found:
            print("❌ Sorry, book not found.")

    def add_new_book(self):
        print("\nAdd New Book:")
        title = input("Title: ")
        author = input("Author: ")
        new_book = {"title": title, "author": author, "status": "Available"}
        self.books.append(new_book)
        print("✨ Book added successfully!")

def main():
    system = Library()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Display All Books")
        print("2. Search for a Book")
        print("3. Add New Book")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            system.display_books()
        elif choice == '2':
            system.search_book()
        elif choice == '3':
            system.add_new_book()
        elif choice == '4':
            print("Closing system...")
            break
        else:
            print("Invalid choice, try again.")

if name == "main":
    main()

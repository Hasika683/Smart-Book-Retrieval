import time

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
    {"title": "Animal Farm", "author": "George Orwell"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"title": "Jane Eyre", "author": "Charlotte Bronte"},
    {"title": "Wuthering Heights", "author": "Emily Bronte"},
    {"title": "Great Expectations", "author": "Charles Dickens"},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "Don Quixote", "author": "Miguel de Cervantes"},
    {"title": "War and Peace", "author": "Leo Tolstoy"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy"},
    {"title": "The Odyssey", "author": "Homer"},
    {"title": "Hamlet", "author": "William Shakespeare"},
    {"title": "Macbeth", "author": "William Shakespeare"},
    {"title": "Romeo and Juliet", "author": "William Shakespeare"},
    {"title": "Othello", "author": "William Shakespeare"},
    {"title": "Moby Dick", "author": "Herman Melville"},
    {"title": "Frankenstein", "author": "Mary Shelley"},
    {"title": "Dracula", "author": "Bram Stoker"},
    {"title": "Alice in Wonderland", "author": "Lewis Carroll"},
    {"title": "Little Women", "author": "Louisa May Alcott"},
    {"title": "Gone with the Wind", "author": "Margaret Mitchell"},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck"},
    {"title": "Of Mice and Men", "author": "John Steinbeck"},
    {"title": "The Old Man and the Sea", "author": "Ernest Hemingway"},
    {"title": "A Farewell to Arms", "author": "Ernest Hemingway"},
    {"title": "Catch-22", "author": "Joseph Heller"},
    {"title": "The Bell Jar", "author": "Sylvia Plath"},
    {"title": "Beloved", "author": "Toni Morrison"},
    {"title": "Invisible Man", "author": "Ralph Ellison"},
    {"title": "The Color Purple", "author": "Alice Walker"},
]

sorted_books = sorted(books, key=lambda b: b["title"].lower())

def linear_search(book_list, query, search_by):
    def normalize(text):
        return text.lower().replace(".", "").replace(" ", "")
    
    for book in book_list:
        if normalize(book[search_by]) == normalize(query):
            return book
    return None

def binary_search(sorted_list, query):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_title = sorted_list[mid]["title"].lower()
        if mid_title == query.lower():
            return sorted_list[mid]
        elif mid_title < query.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None

print("=" * 50)
print("      📚 Smart Book Retrieval System")
print("=" * 50)
print("\nSearch by:")
print("  1. Book Title")
print("  2. Author Name")
choice = input("\nEnter choice (1 or 2): ").strip()

if choice == "1":
    search_by = "title"
    query = input("Enter book title: ").strip()
elif choice == "2":
    search_by = "author"
    query = input("Enter author name: ").strip()
else:
    print("Invalid choice!")
    exit()

# Linear Search
start = time.perf_counter()
result1 = linear_search(books, query, search_by)
linear_time = (time.perf_counter() - start) * 1000

# Binary Search (title only)
if search_by == "title":
    start = time.perf_counter()
    result2 = binary_search(sorted_books, query)
    binary_time = (time.perf_counter() - start) * 1000
else:
    result2 = None
    binary_time = None

print("\n" + "=" * 50)
print("        Search Results")
print("=" * 50)

if result1:
    print(f"\n✅ Book found!")
    print(f"   Title  : {result1['title']}")
    print(f"   Author : {result1['author']}")
else:
    print(f"\n❌ No match found for '{query}'")

print("\n--- Time Taken ---")
print(f"  Linear Search  : {linear_time:.6f} ms  | O(n)")

if binary_time is not None:
    print(f"  Binary Search  : {binary_time:.6f} ms  | O(log n)")
else:
    print(f"  Binary Search  : N/A               | O(log n) | title search only")


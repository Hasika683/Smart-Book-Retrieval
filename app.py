import time
from flask import Flask, render_template, request

app = Flask(__name__)

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
    {"title": "Smart Book Retrieval", "author": "Sravya & Hasika"},
]

sorted_books = sorted(books, key=lambda b: b["title"].lower())

def normalize(text):
    return text.lower().replace(".", "").replace(" ", "")

def linear_search(book_list, query, search_by):
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

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    linear_time = None
    binary_time = None
    conclusion = None
    query = ""
    search_by = "title"

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        search_by = request.form.get("search_by", "title")

        start = time.perf_counter()
        result = linear_search(books, query, search_by)
        linear_time = round((time.perf_counter() - start) * 1000, 6)

        if search_by == "title":
            start = time.perf_counter()
            binary_search(sorted_books, query)
            binary_time = round((time.perf_counter() - start) * 1000, 6)

        if binary_time is not None:
            if binary_time < linear_time:
                conclusion = "Binary Search is faster!"
            else:
                conclusion = "Linear Search is faster this time!"
        else:
            conclusion = "Only Linear Search works for author search."

    return render_template("index.html",
        result=result,
        linear_time=linear_time,
        binary_time=binary_time,
        conclusion=conclusion,
        query=query,
        search_by=search_by
    )

if __name__ == "__main__":
    app.run(debug=True)
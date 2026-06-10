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
    {"title": "Moby Dick", "author": "Herman Melville"},
    {"title": "Smart Book Retrieval", "author": "Sravya & Hasika"}
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
    low = 0
    high = len(sorted_list) - 1

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


def bubble_sort_books(book_list, sort_by):
    arr = book_list.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j][sort_by].lower() > arr[j + 1][sort_by].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def merge_sort_books(book_list, sort_by):

    if len(book_list) <= 1:
        return book_list

    mid = len(book_list) // 2

    left = merge_sort_books(book_list[:mid], sort_by)
    right = merge_sort_books(book_list[mid:], sort_by)

    return merge(left, right, sort_by)


def merge(left, right, sort_by):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i][sort_by].lower() <= right[j][sort_by].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    linear_time = None
    binary_time = None
    conclusion = None

    bubble_time = None
    merge_time = None
    sort_conclusion = None

    query = ""
    search_by = "title"

    if request.method == "POST":

        action = request.form.get("action", "search")

        # SORTING COMPARISON
        if action == "compare_sorts":

            sort_by = request.form.get("sort_by", "title")

            start = time.perf_counter()
            bubble_sort_books(books, sort_by)
            bubble_time = round(
                (time.perf_counter() - start) * 1000,
                6
            )

            start = time.perf_counter()
            merge_sort_books(books, sort_by)
            merge_time = round(
                (time.perf_counter() - start) * 1000,
                6
            )

            if merge_time < bubble_time:
                sort_conclusion = "Merge Sort is faster!"
            else:
                sort_conclusion = "Bubble Sort is faster!"

        # SEARCH COMPARISON
        else:

            query = request.form.get("query", "").strip()
            search_by = request.form.get("search_by", "title")

            start = time.perf_counter()
            result = linear_search(
                books,
                query,
                search_by
            )

            linear_time = round(
                (time.perf_counter() - start) * 1000,
                6
            )

            if search_by == "title":

                start = time.perf_counter()

                binary_search(
                    sorted_books,
                    query
                )

                binary_time = round(
                    (time.perf_counter() - start) * 1000,
                    6
                )

            if binary_time is not None:

                if binary_time < linear_time:
                    conclusion = "Binary Search is faster!"
                else:
                    conclusion = "Linear Search is faster this time!"

            else:
                conclusion = "Only Linear Search works for author search."

    return render_template(
        "index.html",
        result=result,
        linear_time=linear_time,
        binary_time=binary_time,
        conclusion=conclusion,
        query=query,
        search_by=search_by,
        bubble_time=bubble_time,
        merge_time=merge_time,
        sort_conclusion=sort_conclusion
    )


if __name__ == "__main__":
    app.run(debug=True)
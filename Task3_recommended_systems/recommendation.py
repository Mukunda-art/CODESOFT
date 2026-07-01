books = [
    {
        "name": "The Alchemist",
        "genre": "Fiction",
        "author": "Paulo Coelho",
        "year": 1988,
        "language": "English",
        "pages": 208,
        "publisher": "HarperOne",
        "rating": 4.7,
        "price": "₹399",
        "available": "Yes",
        "description": "A story about following dreams."
    },
    {
        "name": "Harry Potter",
        "genre": "Fantasy",
        "author": "J.K. Rowling",
        "year": 1997,
        "language": "English",
        "pages": 320,
        "publisher": "Bloomsbury",
        "rating": 4.9,
        "price": "₹499",
        "available": "Yes",
        "description": "A young wizard's magical journey."
    },
    {
        "name": "Atomic Habits",
        "genre": "Self-Help",
        "author": "James Clear",
        "year": 2018,
        "language": "English",
        "pages": 320,
        "publisher": "Avery",
        "rating": 4.8,
        "price": "₹550",
        "available": "Yes",
        "description": "Build good habits and break bad ones."
    },
    {
        "name": "Rich Dad Poor Dad",
        "genre": "Finance",
        "author": "Robert Kiyosaki",
        "year": 1997,
        "language": "English",
        "pages": 336,
        "publisher": "Plata Publishing",
        "rating": 4.7,
        "price": "₹450",
        "available": "Yes",
        "description": "Learn financial education and investing."
    },
    {
        "name": "The Hobbit",
        "genre": "Fantasy",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "language": "English",
        "pages": 310,
        "publisher": "George Allen & Unwin",
        "rating": 4.8,
        "price": "₹420",
        "available": "Yes",
        "description": "Adventure in a magical world."
    },
    {
        "name": "Think and Grow Rich",
        "genre": "Finance",
        "author": "Napoleon Hill",
        "year": 1937,
        "language": "English",
        "pages": 238,
        "publisher": "The Ralston Society",
        "rating": 4.6,
        "price": "₹350",
        "available": "Yes",
        "description": "Success principles and mindset."
    }
]

print("=" * 65)
print("            BOOK RECOMMENDATION SYSTEM")
print("=" * 65)
print("Available Genres:")
print("• Fiction")
print("• Fantasy")
print("• Self-Help")
print("• Finance")

user_choice = input("\nEnter your favorite genre: ").strip().lower()

found = False
count = 0

print("\nRecommended Books")
print("=" * 65)

for book in books:
    if book["genre"].lower() == user_choice:
        count += 1
        found = True

        print(f"""
Book Name   : {book['name']}
Author      : {book['author']}
Genre       : {book['genre']}
Published   : {book['year']}
Language    : {book['language']}
Pages       : {book['pages']}
Publisher   : {book['publisher']}
Rating      : ⭐ {book['rating']}/5
Price       : {book['price']}
Available   : {book['available']}
Description : {book['description']}
-----------------------------------------------------------------
""")

if found:
    print(f"Total Books Found : {count}")
    print("Thank you for using the Book Recommendation System!")
else:
    print("Sorry! No books found in this genre.")
    print("Please try Fiction, Fantasy, Self-Help, or Finance.")
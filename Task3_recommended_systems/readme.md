# 📚 Book Recommendation System

A simple **Book Recommendation System** developed using Python. This project recommends books to users based on their preferred genre using a **content-based filtering** approach. It displays detailed information about each recommended book, including the author, publication year, language, rating, price, and description.

## 📌 Project Overview

The Book Recommendation System helps users discover books by matching their favorite genre with a predefined collection of books. It demonstrates the fundamentals of recommendation systems using a simple rule-based content filtering technique.

## ✨ Features

* Recommends books based on user-selected genre
* Displays detailed information for each recommended book
* Supports multiple genres
* Shows author, publication year, language, pages, publisher, rating, price, and availability
* User-friendly command-line interface
* Handles invalid genre input gracefully

## 🛠️ Technologies Used

* Python 3
* Built-in Python Features

  * Lists
  * Dictionaries
  * Loops
  * Conditional Statements

## 📂 Project Structure

```text
Book-Recommendation-System/
│── recommendation.py
│── README.md
│── requirements.txt
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/book-recommendation-system.git
```

2. Navigate to the project folder:

```bash
cd book-recommendation-system
```

3. Run the program:

```bash
python recommendation.py
```

## 📖 Available Genres

* Fiction
* Fantasy
* Self-Help
* Finance

## 💬 Sample Output

```text
=============================================================
            BOOK RECOMMENDATION SYSTEM
=============================================================

Available Genres:
• Fiction
• Fantasy
• Self-Help
• Finance

Enter your favorite genre: Fantasy

Recommended Books

Book Name   : Harry Potter
Author      : J.K. Rowling
Genre       : Fantasy
Published   : 1997
Language    : English
Pages       : 320
Publisher   : Bloomsbury
Rating      : ⭐ 4.9/5
Price       : ₹499
Available   : Yes
Description : A young wizard's magical journey.
```

## 🧠 How It Works

1. Stores book information in a list of dictionaries.
2. Accepts the user's preferred genre as input.
3. Compares the selected genre with the available books.
4. Displays matching books along with their details.
5. Shows a message if no matching books are found.

## 🎯 Learning Outcomes

* Python programming fundamentals
* Lists and dictionaries
* Conditional statements
* Loops
* Basic recommendation systems
* Content-based filtering concept

## 🔮 Future Enhancements

* Add more books and genres
* Search by author or book title
* Sort books by rating or publication year
* Store data in a database
* Build a graphical user interface (GUI)
* Develop a web application using Flask or Django

## 👨‍💻 Author

**JEJJI MUKUNDA**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

## 📄 License

This project is developed for educational and learning purposes.


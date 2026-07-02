import datetime
import random

print("=" * 50)
print("         WELCOME TO SMART CHATBOT")
print("Type 'bye' to exit the chatbot")
print("=" * 50)

greetings = [
    "Hello! How can I help you today?",
    "Hi there! Nice to meet you.",
    "Hey! What can I do for you?"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It caught a virus!",
    "Why was the Java developer sad? Because he didn't get Python."
]

while True:
    user = input("\nYou: ").lower().strip()

    # Exit
    if user == "bye":
        print("ChatBot: Goodbye! Have a wonderful day.")
        break

    # Greeting
    elif any(word in user for word in ["hi", "hello", "hey"]):
        print("ChatBot:", random.choice(greetings))

    # How are you
    elif "how are you" in user:
        print("ChatBot: I'm doing great! Thanks for asking.")

    # Name
    elif "your name" in user:
        print("ChatBot: My name is Smart ChatBot.")

    # Age
    elif "your age" in user:
        print("ChatBot: I don't have an age like humans.")

    # Creator
    elif "who created you" in user or "developer" in user:
        print("ChatBot: I was created using Python programming.")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("ChatBot: Current time is", current_time)

    # Date
    elif "date" in user or "today" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("ChatBot: Today's date is", current_date)

    # Python
    elif "python" in user:
        print("ChatBot: Python is a popular programming language.")
        print("ChatBot: It is used for AI, Machine Learning, Web Development, Automation, and Data Science.")

    # AI
    elif "artificial intelligence" in user or user == "ai" or "what is ai" in user:
        print("ChatBot: AI stands for Artificial Intelligence.")
        print("ChatBot: It enables machines to think, learn, and solve problems like humans.")

    # Machine Learning
    elif "machine learning" in user:
        print("ChatBot: Machine Learning is a branch of Artificial Intelligence.")
        print("ChatBot: It helps computers learn from data without explicit programming.")

    # College
    elif "college" in user:
        print("ChatBot: A college is an educational institution where students pursue higher education.")

    # Internship
    elif "internship" in user:
        print("ChatBot: An internship provides practical work experience and helps improve your skills.")

    # Course
    elif "course" in user or "courses" in user:
        print("ChatBot: Popular courses include:")
        print("- Python")
        print("- Java")
        print("- AI")
        print("- Machine Learning")
        print("- Data Science")
        print("- Web Development")
        print("- Cloud Computing")

    # Motivation
    elif "motivate me" in user or "motivation" in user:
        quotes = [
            "Success comes from consistency, not perfection.",
            "Never stop learning.",
            "Small progress every day leads to big success.",
            "Believe in yourself and keep moving forward."
        ]
        print("ChatBot:", random.choice(quotes))

    # Joke
    elif "joke" in user:
        print("ChatBot:", random.choice(jokes))

    # Favorite Color
    elif "favorite color" in user:
        print("ChatBot: I like every color!")

    # Weather
    elif "weather" in user:
        print("ChatBot: I cannot check live weather without internet.")

    # Calculator
    elif user.startswith("calculate"):
        try:
            expression = user.replace("calculate", "").strip()
            result = eval(expression)
            print("ChatBot: The answer is", result)
        except:
            print("ChatBot: Please enter a valid mathematical expression.")

    # Skills
    elif "what can you do" in user:
        print("ChatBot: I can:")
        print("• Tell date and time")
        print("• Answer simple questions")
        print("• Tell jokes")
        print("• Motivate you")
        print("• Perform calculations")
        print("• Explain Python, AI, ML")
        print("• Suggest courses")

    # Help
    elif "help" in user:
        print("\n===== AVAILABLE COMMANDS =====")
        print("hello / hi")
        print("how are you")
        print("your name")
        print("your age")
        print("who created you")
        print("time")
        print("date")
        print("python")
        print("ai")
        print("machine learning")
        print("college")
        print("internship")
        print("courses")
        print("motivate me")
        print("tell me a joke")
        print("weather")
        print("calculate 10+20")
        print("what can you do")
        print("bye")

    # Unknown
    else:
        print("ChatBot: Sorry, I don't understand that.")
        print("ChatBot: Type 'help' to see available commands.")
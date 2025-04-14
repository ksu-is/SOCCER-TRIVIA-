import requests
import random

# Your API key from football-data.org
API_KEY = '03b251cd3ca04fe08ed670333f21c9a9'
# The endpoint to fetch recent matches
URL = 'https://api.football-data.org/v4/matches'
# Set up the header with the API key for authorization
HEADERS = { 'X-Auth-Token': API_KEY }

# List of diverse football trivia questions and answers
TRIVIA = [
    {"question": "Which football club did Lionel Messi join in 2021?", "answer": "Paris Saint-Germain", "options": ["Barcelona", "Paris Saint-Germain", "Manchester City"]},
    {"question": "How often is the FIFA World Cup held?", "answer": "Every 4 years", "options": ["Every 2 years", "Every 4 years", "Every 6 years"]},
    {"question": "How long is a standard football match?", "answer": "90 minutes", "options": ["80 minutes", "90 minutes", "100 minutes"]},
    {"question": "Which country is known as the birthplace of football?", "answer": "England", "options": ["Brazil", "England", "Germany"]},
    {"question": "Who won the UEFA Champions League in 2020?", "answer": "Bayern Munich", "options": ["Paris Saint-Germain", "Bayern Munich", "Liverpool"]},
    {"question": "Which player is known as 'CR7'?", "answer": "Cristiano Ronaldo", "options": ["Cristiano Ronaldo", "Carlos Tevez", "Raul"]},
    {"question": "What is the standard size of a football pitch?", "answer": "125 m x 85 m", "options": ["100 m x 60 m", "110 m x 70 m", "125 m x 85 m"]},
    {"question": "Which team has won the most FIFA World Cup titles?", "answer": "Brazil", "options": ["Brazil", "Germany", "Italy"]},
    {"question": "In which year was the first FIFA World Cup held?", "answer": "1930", "options": ["1920", "1930", "1940"]},
    {"question": "Who holds the record for the most goals in a single World Cup tournament?", "answer": "Just Fontaine", "options": ["Pele", "Just Fontaine", "Gerd Muller"]}
]

# Shuffle the trivia questions to ensure randomness
random.shuffle(TRIVIA)

score = 0  # Keeps track of the user's score

# Loop through the trivia questions and ask each one
for trivia in TRIVIA:
    question = trivia['question']
    correct_answer = trivia['answer']
    options = trivia['options']

    # Shuffle options to randomize their order
    random.shuffle(options)

    # Ask the user the trivia question
    print(f"\n{question}")
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")

    user_input = input("Your answer (1-3): ")

    # Check if the input is a digit and within the valid range
    if user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= 3:
            selected = options[choice - 1]
            if selected == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Nope. Correct answer was: {correct_answer}")
        else:
            print("Invalid number. Skipping...")
    else:
        print("Invalid input. Skipping...")

# Show the final score after all questions
print(f"\nYour final score: {score}/{len(TRIVIA)}")

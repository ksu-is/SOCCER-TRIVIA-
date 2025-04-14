import requests
import random

# Your API key from football-data.org
API_KEY = '03b251cd3ca04fe08ed670333f21c9a9'
# The endpoint to fetch recent matches
URL = 'https://api.football-data.org/v4/matches'
# Set up the header with the API key for authorization
HEADERS = { 'X-Auth-Token': API_KEY }

# Make a GET request to fetch match data
response = requests.get(URL, headers=HEADERS)

# Get the list of matches from the API response if the request was successful
if response.status_code == 200:
    matches = response.json().get('matches', [])
else:
    matches = []
    print("Failed to fetch match data.")

score = 0  # Keeps track of the user's score

# Loop through the first 5 matches and ask a trivia question for each
for match in matches[:5]:
    home = match['homeTeam']['name']  # Home team name
    away = match['awayTeam']['name']  # Away team name
    score_home = match['score']['fullTime']['homeTeam']  # Home team's final score
    score_away = match['score']['fullTime']['awayTeam']  # Away team's final score

    # Skip the match if it hasn't been played yet (scores are None)
    if score_home is None or score_away is None:
        continue

    # Determine the winner or if it was a draw
    if score_home > score_away:
        winner = home
    elif score_home < score_away:
        winner = away
    else:
        winner = "Draw"

    # Create multiple choice options and shuffle them
    options = [home, away, "Draw"]
    random.shuffle(options)

    # Ask the user the trivia question
    print(f"\nWho won the match between {home} and {away}?")
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")

    # Get the user's answer
    try:
        choice = int(input("Your answer (1-3): "))
        selected = options[choice - 1]

        # Check if the answer is correct
        if selected == winner:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Nope. Correct answer was: {winner}")
    except:
        print("Invalid input. Skipping...")

# Show the final score after all questions
print(f"\nYour final score: {score}/5")

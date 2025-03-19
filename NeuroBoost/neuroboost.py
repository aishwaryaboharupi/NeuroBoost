import random
import markovify
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Sample training text (We will later replace this with real conversations)
training_text = """
    Keep pushing forward, even when things feel tough.
    Every challenge makes you stronger.
    Take small steps every day toward your goal.
    You are capable of amazing things.
    Hard work and patience lead to success.
    Stay consistent, and progress will follow.
    Remember, your struggles today will shape your strength tomorrow.
    What’s stopping you? Let's break through it together.
    Small efforts over time lead to big achievements.
    How can you take a step toward progress today?
"""

# Train a Markov Chain model on sample motivation text
text_model = markovify.Text(training_text)

# Memory for storing past user inputs
conversation_history = []

def analyze_mood(user_input):
    """Analyze user's mood and generate a dynamic response."""
    sentiment_score = sia.polarity_scores(user_input)["compound"]
    print(f"DEBUG: Sentiment Score = {sentiment_score}")  # Debugging

    # Remember what the user said
    conversation_history.append(user_input)

    # Generate a response dynamically
    response = ""

    # Special handling for specific moods
    if sentiment_score > 0.5:
        response = "🔥 You're feeling great! Keep riding that momentum! What’s something exciting you're working on?"
    elif sentiment_score > 0.2:
        response = "💡 You seem to be in a good space! Let’s channel that energy. What's something productive you want to do today?"
    elif sentiment_score < -0.5:
        response = "😞 It sounds like you’re struggling. What’s weighing on your mind? Let’s talk about it."
    elif sentiment_score < -0.2:
        response = "💙 I hear you. Taking care of yourself is important. When was the last time you did something for yourself?"
    else:
        response = "⚖️ Let’s make today meaningful! What’s one small thing you can accomplish right now?"

    # Follow-up question to keep the conversation going
    follow_ups = [
        "Can you tell me more about that?",
        "How does that make you feel?",
        "What’s your plan for today?",
        "Is there anything holding you back?",
        "What’s a small step you can take right now?"
    ]
    
    response += " " + random.choice(follow_ups)

    # Add a motivational sentence from the Markov model
    markov_response = text_model.make_sentence()
    if markov_response:
        response += " " + markov_response

    return response

# Chatbot Loop
print("🤖 NeuroBoost: Your AI Motivation Companion! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("NeuroBoost: Stay strong! Talk soon! 💙")
        break
    response = analyze_mood(user_input)
    print("NeuroBoost:", response)

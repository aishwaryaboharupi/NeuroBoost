import markovify
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Sample training text (we will replace this with real conversations later)
training_text = """
    You can do this! Keep going and don't give up.
    Every step you take is progress. Be proud of yourself.
    Challenges make you stronger. Face them with confidence.
    Feeling down? Take a deep breath and restart.
    Remember why you started. Keep moving forward!
    Success comes from consistency, not motivation alone.
    Small wins lead to big victories. Focus on one step at a time.
"""

# Train a Markov Chain model on sample motivation text
text_model = markovify.Text(training_text)

def analyze_mood(user_input):
    """Analyze user's mood based on text sentiment."""
    sentiment_score = sia.polarity_scores(user_input)["compound"]
    print(f"DEBUG: Sentiment Score = {sentiment_score}")  # Debugging

    # Special handling for boredom
    if "bored" in user_input.lower():
        return text_model.make_sentence() or "Try something new! A small change can refresh your mind. 🚀"

    # Response based on sentiment
    if sentiment_score > 0.5:
        return text_model.make_sentence() or "🔥 You're feeling pumped! Keep riding that momentum!"
    elif sentiment_score > 0.2:
        return text_model.make_sentence() or "💡 Sounds like you're in a good space! What’s your next move?"
    elif sentiment_score < -0.5:
        return text_model.make_sentence() or "😞 It sounds like you're struggling. Remember, tough days don’t last."
    elif sentiment_score < -0.2:
        return text_model.make_sentence() or "💙 I hear you. Maybe take a break and reset?"
    else:
        return text_model.make_sentence() or "⚖️ Let’s make today meaningful! What’s one thing you can do right now?"

# Chatbot Loop
print("🤖 NeuroBoost: Your AI Motivation Companion! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("NeuroBoost: Stay strong! Talk soon! 💙")
        break
    response = analyze_mood(user_input)
    print("NeuroBoost:", response)

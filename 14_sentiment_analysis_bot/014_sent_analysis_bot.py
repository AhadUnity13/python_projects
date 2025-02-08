from textblob import TextBlob
from dataclasses import dataclass

#Define a Data Class for Mood
@dataclass
class Mood:
    emoji: str
    sentiment: float

#Define the get_mood Function
def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    """
    Analyze the mood of a given text and return a Mood object containing the emoji and sentiment polarity.

    :param input_text: The input text to be analyzed
    :param sensitivity: 0.0 (super sensitive) - 1.0 (ultra nonsensitive)
    :return: A Mood object containing the emoji representing the mood and the sentiment polarity value
    """

#Compute Sentiment Polarity
    polarity: float = TextBlob(input_text).sentiment.polarity

#Define Sentiment Thresholds
    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)
    else:
        return Mood('😐', polarity)

#Define the run_bot() Function
def run_bot():
    print('Bot: Enter some text and I will perform a sentiment analysis on it.')
    while True:
        user_input: str = input('You: ') 
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')


if __name__ == '__main__':
    run_bot()
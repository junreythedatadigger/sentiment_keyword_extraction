from nltk.sentiment import SentimentIntensityAnalyzer
from responses import responses

# Sample Code (assuming 'responses' is a list of survey responses)
sia = SentimentIntensityAnalyzer()

# sentiment = []
for response in responses:
    sentiment_score = sia.polarity_scores(response)
    print(f"Sentiment: {sentiment_score['compound']} : {response}")
    print("")
    # sentiment.append(f"Sentiment: {sentiment_score['compound']} : {response}")

# print(sentiment)
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from responses import responses

# Sample Code (assuming 'responses' is a list of survey responses)
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

all_words = []
for response in responses:
    words = word_tokenize(response.lower())
    words = [ps.stem(word) for word in words if word.isalnum() and word not in stop_words]
    all_words.extend(words)

word_freq = Counter(all_words)
print(word_freq.most_common(10))  # Print the top 10 keywords

print(stop_words)
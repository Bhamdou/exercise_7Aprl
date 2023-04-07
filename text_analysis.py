import spacy
from collections import Counter

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Input text for analysis
text = """Apple Inc. is an American multinational technology company headquartered in Cupertino, California.
It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."""

# Process the text with spaCy
doc = nlp(text)

# Tokenize the text and display basic statistics
tokens = [token.text for token in doc]
word_freq = Counter(tokens)
print(f"Number of tokens: {len(tokens)}")
print(f"Unique tokens: {len(word_freq)}")
print(f"Word frequency: {word_freq}")

# Named Entity Recognition
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")

import whisper
import string
from rapidfuzz import fuzz
from collections import Counter

# Load the model
model = whisper.load_model("base")

# Transcribe test file
result = model.transcribe("C:/Users/SM_Ga/Documents/Sound Recordings/Test.m4a", language="en")
# language will transcript different languages, "de" = german, "ar" = arabic, "it" = italian, etc.
# translate is meant to translate it back to english, but it kinda sucks

no_punc = str.maketrans("", "", string.punctuation)
# "maketrans" creates a mapping to remove all punctuation
wordset = result["text"]
words = wordset.translate(no_punc)
# now all the punctuation is removed
words = words.lower().split()

# name = "Kurtis Pykes"
# altered = "Kurtis Pykes K D"
# print(f"Similarity: {fuzz.ratio(name, altered)}")
# print(f"Partial Similarity: {fuzz.partial_ratio(name, altered)}")
# print(f"Sort Similarity: {fuzz.token_sort_ratio(name, altered)}")
# print(f"Set Similarity: {fuzz.token_set_ratio(name, altered)}")


dictionary = ["toffee", "i am", "yo", "proudly"]


count = 0
# Comparing every transcribed word with dictionary and applying fuzz ratio
for word in range(len(words)):
    for dict in range(len(dictionary)):
        accuracy = fuzz.ratio(words[word], dictionary[dict])
        if accuracy > 50:
            count = count + 1
            # prints transcribed word with its dictionary counterpart
            print(f"{words[word]} and {dictionary[dict]}")

unique_frequency = Counter(words).most_common(2)
# and a separate counter for fuzz ratio-ed words

# Prints how many words within transcription are similar to dictionary
print(count)
# Print transcription
print(words)

# Currently prints the two most common used words
print(unique_frequency)
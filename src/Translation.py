import whisper
import string
from rapidfuzz import fuzz
from collections import Counter
from pyphonetics import Metaphone
from pyphonetics import Soundex
from pyphonetics import RefinedSoundex

# Load the model
model = whisper.load_model("base")

# Transcribe test file
result = model.transcribe("C:/Users/SM_Ga/Documents/Sound Recordings/Test_7.m4a", language="en")
# result = model.transcribe("C:/Users/SM_Ga/Documents/Projects/Translation/tests/Mac_Miller_Audio_Test.m4a", language="en")
# language will transcript different languages, "de" = german, "ar" = arabic, "it" = italian, etc.
# translate is meant to translate it back to english, but it kinda sucks

no_punc = str.maketrans("", "", string.punctuation)
# "maketrans" creates a mapping to remove all punctuation
wordset = result["text"]
words = wordset.translate(no_punc)
# now all the punctuation is removed
words = words.lower().split()

metaphone = Metaphone()
sound = Soundex()
refined = RefinedSoundex()



pure_dict = open("cleaned_wordlist.txt")
pure = pure_dict.read().split()
dict_counter = []

# print refine check all of these, then remove duplicates
hesitations = ["um","uh","umm","uhh","erm","err"]
confused = ["huh", "ehh", "excuse me"]


count = 0
# Comparing every transcribed word with dictionary and applying fuzz ratio
for word in range(len(words)):
    for dict in range(len(pure)):
        # if metaphone.phonetics(words[word])== metaphone.phonetics(pure[dict])
        if refined.phonetics(words[word]) == refined.phonetics(pure[dict]):
            count = count + 1
            # prints transcribed word with its dictionary counterpart
            dict_counter.append(pure[dict])
            print(f"{words[word]} and {pure[dict]}")

unique_frequency = Counter(words).most_common(3)
second_pot = Counter(dict_counter).most_common(10)
# and a separate counter for fuzz ratio-ed words






# Prints how many words within transcription are similar to dictionary
print(count)
# Print transcription
print(words)

# Currently prints the two most common used words
print(unique_frequency)
print(second_pot)

print(refined.phonetics('hmm'))
print(refined.phonetics('hmmm'))
print(refined.phonetics('eh'))
print(refined.phonetics('huh'))
print(refined.phonetics('um'))
print(refined.phonetics('err'))
print(refined.phonetics('excuse me'))
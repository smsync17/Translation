import whisper
import string
# from rapidfuzz import fuzz
from collections import Counter
from pyphonetics import RefinedSoundex
from deep_translator import MyMemoryTranslator
import requests
import json

# Load the model
model = whisper.load_model("base")

# Transcribe test file
# result = model.transcribe("C:/Users/SM_Ga/Documents/Sound Recordings/Test_7.m4a", language="en")
result = model.transcribe("C:/Users/SM_Ga/Documents/Sound Recordings/Mac_Miller_Trimmed.m4a", language="en")
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

ref_hes = []
ref_con = []

for hes in hesitations:
    ref_hes.append(refined.phonetics(hes))
for con in confused:
    ref_con.append(refined.phonetics(con))

check = 0
count = 0
# Comparing every transcribed word with dictionary and applying fuzz ratio
for word in range(len(words)):
    for dict in range(len(pure)):
        # if metaphone.phonetics(words[word])== metaphone.phonetics(pure[dict])
        try:
            ref_word = refined.phonetics(words[word])
            ref_dict = refined.phonetics(pure[dict])
            if ref_word == ref_dict:
                count = count + 1
                if ref_word in ref_hes:
                    dict_counter.append("*hesitation*")
                    check = 1
                else:
                    if ref_word in ref_con:
                        dict_counter.append("*confused*")
                    else:
                        # prints transcribed word with its dictionary counterpart
                        dict_counter.append(pure[dict])
                # print(f"{words[word]} and {pure[dict]}")
        except:
            pass

temp_count = []
bi_gram = []
filtered_counts = {word: count for word, count in Counter(words).items() if count >= 5}
for source in filtered_counts:
    for word in range(len(words)):
        if source == words[word]:
            try:
                temp_count.append(source + " " + words[word+1])
            except:
                pass
    filtered_bi_gram = {word: count for word, count in Counter(temp_count).items() if count >= 3}
    temp_count = []
    if filtered_bi_gram:
        bi_gram.append(filtered_bi_gram)


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

# print(refined.phonetics('hmm'))
# print(refined.phonetics('hmmm'))
# print(refined.phonetics('eh'))
# print(refined.phonetics('huh'))
# print(refined.phonetics('um'))
# print(refined.phonetics('err'))
# print(refined.phonetics('excuse me'))
# if check:
#     print("we in")

print(f"the filtered {filtered_counts}")
print(f"the bigrams {bi_gram}")



def translate_text(text: str, langpair: str = "en|ar") -> str:
    url = "https://api.mymemory.translated.net/get"

    params = {"q": text, "langpair": langpair, "de": "smsync17@gmail.com"}
    # "de": "your.email@example.com"

    try:
        # Send HTTP GET request
        response = requests.get(url, params=params, timeout=30)

        # Check if the HTTP request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Safely extract the translated text from the nested JSON object
        translate = data.get("responseData", {}).get("translatedText")

        if translate:
            return translate
        else:
            return "Error: Translation field not found in response"
        
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"An error occurred: {err}"

trans = {}

for dictionary in bi_gram:
    for key in dictionary:
        print(f"{key} translates to {translate_text(key)}")
        trans[key] = translate_text(key)


translated_json  = json.dumps(trans)


with open("translated.json", "w") as f:
    f.write(translated_json)


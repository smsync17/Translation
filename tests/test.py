from pyphonetics import RefinedSoundex
import string
from collections import Counter

refined = RefinedSoundex()

print(refined.phonetics('the'))
print(refined.phonetics('tie'))
print(refined.phonetics('ti'))
print(refined.phonetics('ta'))
print(refined.phonetics('toe'))
print(refined.phonetics('thy'))
print(refined.phonetics('too'))


no_punc = str.maketrans("", "", string.punctuation)
# "maketrans" creates a mapping to remove all punctuation
words = ["yo","gang","yo","son","bro","yo","yo","son"]


refined = RefinedSoundex()



pure_dict = open("../cleaned_wordlist.txt")
pure = pure_dict.read().split()

d = {}

for sound in pure:
    key = refined.phonetics(sound)
    if key not in d:
        d[key] = [sound]
    else:
        d[key].append(sound)

print(f"you come look at this {len(d)}")

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

word_counts = Counter(words)

count = 0
# Comparing every transcribed word with dictionary and applying fuzz ratio
for word, occurrences in word_counts.items():
    ref_word = refined.phonetics(word)
    if ref_word == "":
        continue
    else:
        if ref_word in d:
            count = count + occurrences
            if ref_word in ref_hes:
                dict_counter.extend(["*hesitation*"] * occurrences)
            elif ref_word in ref_con:
                dict_counter.extend(["*confused*"] * occurrences)
            else:
                # prints transcribed word with its dictionary counterpart
                dict_counter.extend([d] * occurrences)
            # print(f"{words[word]} and {pure[dict]}")

temp_count = []
bi_gram = []
filtered_counts = {word: count for word, count in Counter(words).items() if count >= 2}
for source in filtered_counts:
    for word in range(len(words) - 1):
        if source == words[word]:
            temp_count.append(source + " " + words[word+1])
    filtered_bi_gram = {word: count for word, count in Counter(temp_count).items() if count >= 2}
    temp_count = []
    if filtered_bi_gram:
        bi_gram.append(filtered_bi_gram)


unique_frequency = Counter(words).most_common(3)
second_pot = Counter(dict_counter).most_common(15)

print(count)
print(words)

print(unique_frequency)
print(f"Second pot {second_pot}")

print(f"the filtered {filtered_counts}")
print(f"the bigrams {bi_gram}")

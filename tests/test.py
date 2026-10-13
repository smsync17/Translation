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
wordset = []
words = wordset.translate(no_punc)
# now all the punctuation is removed
words = words.lower().split()


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

count = 0
# Comparing every transcribed word with dictionary and applying fuzz ratio
for word in range(len(words)):
    for dict_idx in range(len(pure)):
        # if metaphone.phonetics(words[word])== metaphone.phonetics(pure[dict])
        try:
            ref_word = refined.phonetics(words[word])
            ref_dict = refined.phonetics(pure[dict_idx])
            if ref_word == ref_dict:
                count = count + 1
                if ref_word in ref_hes:
                    dict_counter.append("*hesitation*")
                else:
                    if ref_word in ref_con:
                        dict_counter.append("*confused*")
                    else:
                        # prints transcribed word with its dictionary counterpart
                        dict_counter.append(pure[dict_idx])
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
second_pot = Counter(dict_counter).most_common(15)
from pyphonetics import RefinedSoundex

refined = RefinedSoundex()

print(refined.phonetics('the'))
print(refined.phonetics('tie'))
print(refined.phonetics('ti'))
print(refined.phonetics('ta'))
print(refined.phonetics('toe'))
print(refined.phonetics('thy'))
print(refined.phonetics('too'))
import whisper

# Load the model
model = whisper.load_model("base")

# Transcribe test file
result = model.transcribe("C:/Users/SM_Ga/Documents/Sound Recordings/Test_6.m4a", language="de")
# language will transcript different languages, "de" = german, "ar" = arabic, "it" = italian, etc.
# translate is meant to translate it back to english, but it kinda sucks

# Print transcription
print(result["text"])
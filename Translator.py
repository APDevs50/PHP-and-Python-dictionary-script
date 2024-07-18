import pandas as pd
from googletrans import Translator
import time
import os

# Initialize the translator
translator = Translator()

# Define the batch size
BATCH_SIZE = 1000

# Load the dictionary
df = pd.read_excel('words.xlsx')

# Function to translate a word
def translate_word(word):
    try:
        translation = translator.translate(word, src='en', dest='fr')
        return translation.text
    except Exception as e:
        print(f"Error translating {word}: {e}")
        return word  # Return the original word in case of an error

# Check if translated_words.xlsx exists and load it if it does
if os.path.exists('translated_words.xlsx'):
    translated_df = pd.read_excel('translated_words.xlsx')
    translated_words = translated_df['TranslatedWords'].tolist()
else:
    translated_words = []

# Translate words in batches
for i in range(len(translated_words), len(df), BATCH_SIZE):
    batch = df['Englishdict'][i:i + BATCH_SIZE]
    translated_batch = [translate_word(word) for word in batch]
    translated_words.extend(translated_batch)
    
    # Save to translated_words.xlsx every 1000 lines
    if (i + BATCH_SIZE) % BATCH_SIZE == 0:
        translated_df = pd.DataFrame({'TranslatedWords': translated_words})
        translated_df.to_excel('translated_words.xlsx', index=False)
        print(f"Saved {len(translated_words)} translated words to translated_words.xlsx")

# Save any remaining translations
translated_df = pd.DataFrame({'TranslatedWords': translated_words})
translated_df.to_excel('translated_words.xlsx', index=False)
print(f"Final save: {len(translated_words)} translated words to translated_words.xlsx")

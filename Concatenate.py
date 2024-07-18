import pandas as pd

# File paths
original_file = 'words.xlsx'
translated_file = 'translated_words.xlsx'
output_file = 'final_translated_words.xlsx'

# Load the original and translated data
df_original = pd.read_excel(original_file)
df_translated = pd.read_excel(translated_file, header=None, names=['French'])

# Ensure the original file has the 'Englishdict' column
if 'Englishdict' not in df_original.columns:
    raise ValueError("The original file must contain a column named 'Englishdict'.")

# Concatenate the original and translated data
df_combined = pd.concat([df_original, df_translated], axis=1)

# Save the combined data to a new Excel file
df_combined.to_excel(output_file, index=False)

print(f"Concatenated file saved as {output_file}.")

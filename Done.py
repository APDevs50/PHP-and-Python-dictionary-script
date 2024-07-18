import pandas as pd

# File paths
input_file = 'final_translated_words.xlsx'
output_file = 'final_translated_words.csv'

# Load the Excel file
df = pd.read_excel(input_file)

# Save the DataFrame to a CSV file with UTF-8 encoding
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Excel file {input_file} has been converted to CSV file {output_file} with UTF-8 encoding.")

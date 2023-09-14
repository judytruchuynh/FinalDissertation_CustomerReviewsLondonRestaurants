import pandas as pd

# Replace 'path/to/no_dup_combined_all.xlsx' with the actual path to your Excel file
excel_file_path = '/Users/macbookpro/Desktop/DISSERTATION/DATA/no_dup_combined_all.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Function to extract the two words before "United Kingdom"
def extract_words(address):
    if "United Kingdom" in address:
        words = address.split("United Kingdom")[0].strip().split()[-2:-1]
        return " ".join(words)
    else:
        return None

# Apply the function to the "Address" column and create a new column "Extracted Words"
df["Postal Code"] = df["Address"].apply(extract_words)

# Save the updated DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)

print("Extraction completed and saved to the Excel file.")

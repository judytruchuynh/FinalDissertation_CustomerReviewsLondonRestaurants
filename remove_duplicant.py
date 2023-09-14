import pandas as pd

filename = '/Users/macbookpro/Desktop/DISSERTATION/DATA/combined_all.xlsx'
no_dup_filename = '/Users/macbookpro/Desktop/DISSERTATION/DATA/no_dup_combined_all.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(filename)

# Remove rows with duplicate values in the specified columns
df_no_dup = df.drop_duplicates(subset=['Restaurant', 'Address', 'User', 'Review'], keep='first')

# Save the DataFrame with no duplicate rows as a new Excel file
df_no_dup.to_excel(no_dup_filename, index=False)

print(f"No duplicate rows. Data saved as '{no_dup_filename}'")

import pandas as pd

# Read each Excel file into separate DataFrames
df1 = pd.read_excel('/Users/macbookpro/Desktop/DISSERTATION/DATA/no_dup_combined_reviews_general_postal.xlsx')
df2 = pd.read_excel('/Users/macbookpro/Desktop/DISSERTATION/DATA/no_dup_combined_reviews_general_querry.xlsx')

# Concatenate the DataFrames into a single DataFrame
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined_filename = '/Users/macbookpro/Desktop/DISSERTATION/DATA/combined_all.xlsx'
combined_df.to_excel(combined_filename, index=False)
print(f"Combined data saved as '{combined_filename}'")



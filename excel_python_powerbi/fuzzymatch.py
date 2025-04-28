import pandas as pd
import os

# --- Configuration ---
excel_file_path = 'productivity_tracker_2023.xlsx'

data_sheet_name = 'data_cleanedup'
categories_sheet_name = 'activity_categories'

common_column = 'Activity'

column_to_join = 'Activity Category'

# Define the output file name
output_file_name = 'productivity_tracker_merged.xlsx' 

# --- Data Loading ---
try:
    # Read the Excel file
    xls = pd.ExcelFile(excel_file_path)

    # Read the specific worksheets into pandas DataFrames
    df_data = xls.parse(data_sheet_name)
    df_categories = xls.parse(categories_sheet_name)

    print(f"Successfully loaded '{data_sheet_name}' with {len(df_data)} rows.")
    print(f"Successfully loaded '{categories_sheet_name}' with {len(df_categories)} rows.")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
    # Exit the script if the file is not found
    exit()
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")
    # Exit the script if there's an error reading the file
    exit()

# --- Exact Keyword Matching and Merging ---

# Create a dictionary mapping activity keywords to their categories for quick lookup
# Ensure keywords are treated case-insensitively if needed, or handle case appropriately
category_lookup = df_categories.set_index(common_column)[column_to_join].to_dict()

# Get the list of keywords from the categories sheet
category_keywords = df_categories[common_column].tolist()

# Initialize a list to store the matched category for each row in df_data
matched_categories = []

print(f"Starting exact keyword matching process...")

# Iterate through each activity in the data_cleanedup sheet
for index, row in df_data.iterrows():
    data_activity = str(row[common_column]) # Ensure it's a string for checking 'in'

    found_category = None # Initialize to None for no match

    # Iterate through the category keywords to find an exact match within the data activity phrase
    # The loop will check all keywords but stop at the first exact match found
    for keyword in category_keywords:
        # Check if the exact keyword is present as a substring in the data activity phrase
        # You might want to add checks for whole words if necessary (e.g., using regex)
        if str(keyword) in data_activity:
            # If an exact keyword is found, get its category from the lookup dictionary
            found_category = category_lookup.get(keyword)
            break # Stop searching for keywords once the first match is found for this phrase
    if found_category is None:
        matched_categories.append("Other") # Append "Other" if no category was found
    else:
        matched_categories.append(found_category)

# Add the matched categories as a new column to the data DataFrame
df_data[column_to_join] = matched_categories

print("Exact keyword matching complete.")

# --- Save the Result ---

try:
    # Save the merged DataFrame to a new Excel file
    df_data.to_excel(output_file_name, index=False)

    print(f"Merged data saved successfully to '{output_file_name}'")

except Exception as e:
    print(f"An error occurred while saving the output file: {e}")


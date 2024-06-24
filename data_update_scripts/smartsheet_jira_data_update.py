import pandas as pd
from datetime import datetime
import os

# Define the file paths
smartsheet_file_path = '/Users/felipelucena/Downloads/Reman Report/Reman Report_smartsheet.xlsx'
sharepoint_file_path = '/Users/felipelucena/Downloads/Reman Report/reman_report_sharepoint.xlsx'
jira_export_path = '/Users/felipelucena/Downloads/Reman Report/2024-06-24-rr-sheet_jira.xlsx'

# Define the sheet names to be analyzed
smartsheet_sheet_name = 'Reman Report'
sharepoint_sheet_name = 'Sheet1'

# Define the foreign key names
smartsheet_key = 'unique_key'
jira_key = 'Summary'

# Extract the root directory from smartsheet_file_path
root_directory = os.path.dirname(smartsheet_file_path)

# Define output and logs directories
output_directory = os.path.join(root_directory, 'Output')
logs_directory = os.path.join(output_directory, 'logs')

# Create directories if they do not exist
os.makedirs(logs_directory, exist_ok=True)

print("Loading data from Smartsheet...")
smartsheet_data = pd.read_excel(smartsheet_file_path, sheet_name=smartsheet_sheet_name)
print("Smartsheet data loaded.")

print("Loading data from Sharepoint...")
sharepoint_data = pd.read_excel(sharepoint_file_path, sheet_name=sharepoint_sheet_name)
print("Sharepoint data loaded.")

# Get the columns from each spreadsheet
columns_1 = set(smartsheet_data.columns)
columns_2 = set(sharepoint_data.columns)

# Determine the columns that are present only in the first spreadsheet
unique_to_file_1 = columns_1 - columns_2

# Create DataFrame for the unique columns
unique_to_file_1_df = pd.DataFrame(list(unique_to_file_1), columns=['Unique to File 1'])
print("Unique columns in Smartsheet identified.")

print("Loading data from Jira export...")
jira_data = pd.read_excel(jira_export_path)
print("Jira data loaded.")

print("Verifying the presence of the jira_key column in Jira data...")
if jira_key not in jira_data.columns:
    raise KeyError(f"Column '{jira_key}' not found in the Jira export file.")

print(f"Renaming column '{jira_key}' to 'JIRA Summary'...")
jira_data.rename(columns={jira_key: 'JIRA Summary'}, inplace=True)
print("Column renamed.")

print("Merging Smartsheet data with Jira data...")
try:
    merged_data = pd.merge(smartsheet_data, jira_data[['Issue key', 'JIRA Summary']], left_on=smartsheet_key, right_on='JIRA Summary', how='left')
    print("Data merged successfully.")
except KeyError as e:
    print(f"Error during merge: {e}")
    raise

# Rename the 'Issue key' column to 'Issue Key' in the resulting DataFrame
merged_data.rename(columns={'Issue key': 'Issue Key'}, inplace=True)
print("Column 'Issue key' renamed to 'Issue Key'.")

# Reorder columns to place 'Issue Key' and 'JIRA Summary' first
cols = ['Issue Key', 'JIRA Summary'] + [col for col in merged_data.columns if col not in ['Issue Key', 'JIRA Summary']]
merged_data = merged_data[cols]
print("Columns reordered.")

# Identify records without a match and save to a log file
unmatched_records = merged_data[merged_data['Issue Key'].isnull()][smartsheet_key].tolist()
if unmatched_records:
    unmatched_count = len(unmatched_records)
    log_file_name = f"unmatched_records_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt"
    log_file_path = os.path.join(logs_directory, log_file_name)

    # Save unmatched records to an Excel file
    unmatched_data = merged_data[merged_data['Issue Key'].isnull()]
    unmatched_excel_name = f"{smartsheet_sheet_name}_unmatched_records_{datetime.now().strftime('%Y-%m-%d_%H%M')}.xlsx"
    unmatched_excel_path = os.path.join(logs_directory, unmatched_excel_name)
    unmatched_data.to_excel(unmatched_excel_path, index=False)

    # Write unmatched records to the log file
    with open(log_file_path, 'w') as log_file:
        log_file.write(f"No match found for records ({smartsheet_key}):\n")
        for record in unmatched_records:
            log_file.write(f"{record}\n")
        log_file.write(f"\nDetails saved to {unmatched_excel_path}")


# Remove rows where 'Issue Key' is null
merged_data = merged_data[merged_data['Issue Key'].notnull()]
print("Rows with null 'Issue Key' removed.")

# Create the name for the new file with datetime
output_file_name = f"{smartsheet_sheet_name}_full_version_{datetime.now().strftime('%Y-%m-%d %H%M')}.xlsx"
output_file_path = os.path.join(output_directory, output_file_name)

# Save the resulting DataFrame to a new Excel file
merged_data.to_excel(output_file_path, index=False)

# Generate the simplified file with the specified columns
simplified_columns = ['Issue Key', 'JIRA Summary', smartsheet_key] + list(unique_to_file_1)
simplified_data = merged_data[simplified_columns]

# Create the name for the simplified file with datetime
simplified_file_name = f"{smartsheet_sheet_name}_simplified_version_{datetime.now().strftime('%Y-%m-%d %H%M')}.xlsx"
simplified_file_path = os.path.join(output_directory, simplified_file_name)

# Save the simplified DataFrame to a new Excel file
simplified_data.to_excel(simplified_file_path, index=False)

# Print the unique columns in file 1 and details about unmatched records
print(f"\nUnique columns in {smartsheet_sheet_name} Smartsheet:\n{unique_to_file_1_df}")
if unmatched_records:
    print(f"No match found for {unmatched_count} records. Details saved to {log_file_path}")

print(f"Full version file saved as {output_file_path}")
print(f"Simplified file saved as {simplified_file_path}")

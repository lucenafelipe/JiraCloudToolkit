import pandas as pd
from datetime import datetime
import os

# Define the file paths
smartsheet_file_path = '/Users/felipelucena/Downloads/NPI2/NPI Service Sourcing Tracker.xlsx'
sharepoint_file_path = '/Users/felipelucena/Downloads/NPI2/Daily Refresh.xlsx'
jira_export_path = '/Users/felipelucena/Downloads/NPI2/2024-06-12-npi-service-sourcing-tracker.xlsx'

# Define the sheet names to be analyzed
smartsheet_sheet_name = 'NPI Service Sourcing Tracker'
sharepoint_sheet_name = 'NPI Sourcing Tracker Load'

# Define the foreign key names
smartsheet_key = 'Service PN'
jira_key = 'Service PN'

# Extract the root directory from smartsheet_file_path
root_directory = os.path.dirname(smartsheet_file_path)

# Define output and logs directories
output_directory = os.path.join(root_directory, 'Output')
logs_directory = os.path.join(output_directory, 'logs')

# Create directories if they do not exist
os.makedirs(logs_directory, exist_ok=True)

# Load the relevant sheets from the two spreadsheets
smartsheet_data = pd.read_excel(smartsheet_file_path, sheet_name=smartsheet_sheet_name)
sharepoint_data = pd.read_excel(sharepoint_file_path, sheet_name=sharepoint_sheet_name)

# Get the columns from each spreadsheet
columns_1 = set(smartsheet_data.columns)
columns_2 = set(sharepoint_data.columns)

# Determine the columns that are present only in the first spreadsheet
unique_to_file_1 = columns_1 - columns_2

# Create DataFrame for the unique columns
unique_to_file_1_df = pd.DataFrame(list(unique_to_file_1), columns=['Unique to File 1'])

# Display the unique columns
print("\nUnique columns in file 1:")
print(unique_to_file_1_df)

# Load the data from the default sheet of the Jira export file
jira_data = pd.read_excel(jira_export_path)

# Merge the data based on the foreign key
merged_data = pd.merge(smartsheet_data, jira_data[['Issue key', jira_key]], left_on=smartsheet_key, right_on=jira_key, how='left')

# Rename the 'Issue key' column to 'Issue Key' in the resulting DataFrame
merged_data.rename(columns={'Issue key': 'Issue Key'}, inplace=True)

# Identify records without a match
unmatched_records = merged_data[merged_data['Issue Key'].isnull()][smartsheet_key].tolist()
if unmatched_records:
    unmatched_count = len(unmatched_records)
    log_file_name = f"unmatched_records_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt"
    log_file_path = os.path.join(logs_directory, log_file_name)

    # Write unmatched records to the log file
    with open(log_file_path, 'w') as log_file:
        log_file.write(f"No match found for records ({smartsheet_key}):\n")
        for record in unmatched_records:
            log_file.write(f"{record}\n")

    # Print the number of unmatched records and the log file path
    print(f"No match found for {unmatched_count} records. Details saved to {log_file_path}")

# Create the name for the new file with datetime
output_file_name = f"NPI Service Sourcing Tracker {datetime.now().strftime('%Y-%m-%d %H%M')}.xlsx"
output_file_path = os.path.join(output_directory, output_file_name)

# Save the resulting DataFrame to a new Excel file
merged_data.to_excel(output_file_path, index=False)

print(f"File saved as {output_file_path}")

# Generate the simplified file with the specified columns
simplified_columns = [smartsheet_key, 'Issue Key'] + list(unique_to_file_1)
simplified_data = merged_data[simplified_columns]

# Create the name for the simplified file with datetime
simplified_file_name = f"NPI Service Sourcing Tracker Simplified {datetime.now().strftime('%Y-%m-%d %H%M')}.xlsx"
simplified_file_path = os.path.join(output_directory, simplified_file_name)

# Save the simplified DataFrame to a new Excel file
simplified_data.to_excel(simplified_file_path, index=False)

print(f"Simplified file saved as {simplified_file_path}")

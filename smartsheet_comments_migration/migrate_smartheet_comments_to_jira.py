import pandas as pd
from datetime import datetime
import re

# Define file path variables
smartsheet_file_path = '/Users/felipelucena/Downloads/NPI Comments Migration/NPI Service Sourcing Tracker_smartsheet.xlsx'
jira_users_file_path = '/Users/felipelucena/Downloads/NPI Comments Migration/export_users_jira.csv'
jira_issues_file_path = '/Users/felipelucena/Downloads/NPI Comments Migration/2024-06-28-npi-service-sourcing-tracker_jira_issues.xlsx'

# Define the name of the Smartsheet tab and foreign keys
smartsheet_tab_name = 'NPI Service Sourcing Tracker'
smartsheet_key_column = 'Service PN'
jira_key_column = 'Service PN'

# Define output paths
output_dir = '/Users/felipelucena/Downloads/NPI Comments Migration/Output/'
current_datetime = datetime.now().strftime("%Y-%m-%d %H%M")
migration_output_file_path = f'{output_dir}/{smartsheet_tab_name}_comments_migration_{current_datetime}.csv'
log_file_path = f'{output_dir}/log_comments_migration_{current_datetime}.txt'

# Default user ID - This account ID will be used if the user's account id is not found.
default_user_id = '612e588e6a4c09006a996ad9' # svc_jirascripts

# Load data
smartsheet_df = pd.read_excel(smartsheet_file_path, sheet_name=[smartsheet_tab_name, 'Comments'], header=None)
npi_service_sourcing_df = smartsheet_df[smartsheet_tab_name]
comments_df = smartsheet_df['Comments']
jira_users_df = pd.read_csv(jira_users_file_path)
jira_issues_df = pd.read_excel(jira_issues_file_path)

# Integrity check for Jira issues file
essential_columns = ['Issue key', 'Summary', jira_key_column]
if not all(column in jira_issues_df.columns for column in essential_columns):
    print(f"ERROR: The Jira issues file does not contain the essential columns: Issue key, Summary, {jira_key_column}.")
    print("Please perform a new data export from Jira including all necessary fields and try again.")
    exit(1)

# Adjust column names if necessary
npi_service_sourcing_df.columns = npi_service_sourcing_df.iloc[0]  # Assume the first row contains headers
npi_service_sourcing_df = npi_service_sourcing_df[1:]  # Remove the first row which is now the header
comments_df.columns = comments_df.iloc[0]
comments_df = comments_df[1:]

# Fill empty values in Column A with the last valid value
comments_df.loc[:, 'Row 1'] = comments_df['Row 1'].ffill()

# Remove rows where all columns are NaN
comments_df = comments_df.dropna(how='all')

# Prepare log
log_messages = set()
jira_not_found = set()

# Create a dictionary for quick lookup of Jira user IDs
user_lookup = dict(zip(jira_users_df['User name'], jira_users_df['User id']))

# Process comments and map task_id to issue details
comments_data = []

for index, row in comments_df.iterrows():
    try:
        row_number_str = row.iloc[0]  # First column as the row index

        # Extract the number from the string using regex
        row_number_match = re.search(r'\d+', str(row_number_str))
        if row_number_match:
            row_number = int(row_number_match.group())  # Convert to integer
        else:
            continue  # Skip if unable to extract the number

        comment_text = row.iloc[1]  # Second column as the comment text
        created_at = row.iloc[3]  # Fourth column as the comment date
        created_by = row.iloc[2]  # Third column as the comment author

        # Skip rows with essential NaN values
        if pd.isna(comment_text) or pd.isna(created_at) or pd.isna(created_by):
            continue

        # Look up the user ID in Jira
        jira_user_id = user_lookup.get(created_by, default_user_id)
        if jira_user_id == default_user_id:
            log_messages.add(
                f"Account ID not found for user {created_by}. The account ID was replaced by {default_user_id}.")
            comment_text = (f"*This comment was originally made by user '{created_by}' on {created_at}:*\n"
                            f"{comment_text}\n\n"
                            "_Note: The user was not found in the Jira database, so the comment was posted on behalf of the importing user._")

        # Find the corresponding issue in Jira
        smartsheet_row = npi_service_sourcing_df.iloc[row_number - 1]  # Adjust 1-based index to 0-based
        smartsheet_key_value = smartsheet_row[smartsheet_key_column]
        jira_issue_row = jira_issues_df[jira_issues_df[jira_key_column] == smartsheet_key_value]

        if not jira_issue_row.empty:
            issue_id = jira_issue_row['Issue key'].values[0]
            summary = jira_issue_row['Summary'].values[0]
            comment_body = f"{created_at}; {jira_user_id}; {comment_text}"
            comments_data.append({'Issue Id': issue_id, 'Summary': summary, 'Comment Body': comment_body})
        else:
            jira_not_found.add(smartsheet_key_value)

    except Exception as e:
        log_messages.add(f"Error processing row {index}: {e}")

# Save migrated comments
migration_comments_df = pd.DataFrame(comments_data)
migration_comments_df.to_csv(migration_output_file_path, index=False)

# Finalize log
with open(log_file_path, 'w') as log_file:
    if log_messages:
        log_file.write("Migration Log:\n")
        for message in log_messages:
            log_file.write(f"{message}\n")
    else:
        log_file.write("All users in this spreadsheet were successfully located.\n")

    if jira_not_found:
        log_file.write("\nCorrespondences not found in Jira:\n")
        log_file.write("No correspondence was found in Jira for the following records:\n")
        for key in jira_not_found:
            log_file.write(f"- {key}\n")

print(f"Migration comments saved to: {migration_output_file_path}")
print(f"Log file saved to: {log_file_path}")

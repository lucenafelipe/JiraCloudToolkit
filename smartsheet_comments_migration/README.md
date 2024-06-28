
# Migrate Smartsheet Comments to Jira

This script, `migrate_smartsheet_comments_to_jira.py`, is designed to generate an import file for Jira Cloud by migrating comments from Smartsheet data.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Script Details](#script-details)
- [Output](#output)
- [Logs](#logs)

## Introduction

The purpose of this script is to facilitate the migration of comments from a Smartsheet document to Jira Cloud. It reads comments from a specified Smartsheet file, maps them to corresponding Jira issues, and creates an import file suitable for Jira.

## Requirements

- Python 3.7 or higher
- pandas library

## Usage

1. **Install the required libraries:**

    ```bash
    pip install pandas
    ```

2. **Update the file paths and configurations:**

    Modify the following variables in the script to match your file paths and configurations:
    - `smartsheet_file_path`
    - `jira_users_file_path`
    - `jira_issues_file_path`
    - `output_dir`
    - `default_user_id`

3. **Run the script:**

    ```bash
    python migrate_smartsheet_comments_to_jira.py
    ```

## Script Details

The script performs the following steps:

1. **Load Data:**
    - Reads Smartsheet data from the specified Excel file.
    - Reads Jira users and issues data from the specified CSV and Excel files.

2. **Process Comments:**
    - Iterates through the comments in the Smartsheet data.
    - Matches comments to corresponding Jira issues based on a specified key column.
    - Handles missing user IDs by using a default ID and logs the occurrence.

3. **Generate Output:**
    - Creates a CSV file containing the migrated comments in a format suitable for Jira import.

## Output

The output of the script includes:
- A CSV file containing the migrated comments, saved in the specified output directory.

## Logs

The script generates a log file that includes:
- Any issues encountered during the migration process.
- A list of comments where the user ID was not found in the Jira database.
- A list of Smartsheet keys for which corresponding Jira issues were not found.

## Example Output Paths

- Migration comments file: `/path/to/output/NPI_Service_Sourcing_Tracker_comments_migration_YYYY-MM-DD_HHMM.csv`
- Log file: `/path/to/output/log_comments_migration_YYYY-MM-DD_HHMM.txt`

## Conclusion

This script simplifies the process of migrating comments from Smartsheet to Jira Cloud by automating the data transformation and ensuring compatibility with Jira's import format.

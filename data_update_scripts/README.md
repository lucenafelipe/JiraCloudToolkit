
# JiraCloudToolKit

## Overview

This repository contains tools and scripts to facilitate data integration and updates between various data sources and Jira Cloud. The primary script in this repository helps migrate and update data from Smartsheet to Jira Cloud.

## Folder Structure

- `jira_data_updates/`: Contains scripts related to updating data in Jira Cloud.

## Scripts

### `generate_update_payload.py`

This script is designed to assist in the migration and updating of data from Smartsheet to Jira Cloud. It performs the following tasks:

1. **Identifies Unique Columns**:
   - Compares the columns in the Smartsheet and Sharepoint files to identify columns that are unique to Smartsheet.

2. **Merges Data**:
   - Merges the Smartsheet data with the Jira export data, adding the "Issue Key" to the Smartsheet dataset, facilitating the correspondence between tickets in Smartsheet and Jira Cloud.

3. **Reorganizes and Cleans Data**:
   - Removes the duplicate "Unique Key" column from the merged dataset.
   - Reorders columns to ensure "Issue Key" is in the first position.
   - Removes records where "Issue Key" is null.

4. **Generates Output Files**:
   - Creates two versions of the output file:
     - A full version containing all the data from Smartsheet, including the "Issue Key".
     - A simplified version containing only the "Issue Key", the foreign key from Smartsheet, and the unique columns from Smartsheet.

5. **Logs Unmatched Records**:
   - Identifies and logs records in Smartsheet that do not have a corresponding issue in Jira Cloud.
   - Saves these unmatched records in a separate Excel file and adds a note in the text log file.

## Usage

### Prerequisites

- Python 3.x
- Pandas library

### Steps

1. Clone the repository:
   \`\`\`sh
   git clone https://github.com/yourusername/JiraCloudToolKit.git
   cd JiraCloudToolKit
   \`\`\`

2. Install the required dependencies:
   \`\`\`sh
   pip install pandas
   \`\`\`

3. Place your Smartsheet, Sharepoint, and Jira export files in the appropriate directory.
4. Update the file paths in `generate_update_payload.py` to point to your data files.
5. Run the script:
   \`\`\`sh
   python jira_data_updates/generate_update_payload.py
   \`\`\`

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

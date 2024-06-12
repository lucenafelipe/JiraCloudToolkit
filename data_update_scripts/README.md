# JiraCloudToolKit

## Overview

This repository contains tools and scripts to facilitate data integration and updates between various data sources and Jira Cloud. The primary script in this repository helps migrate and update data from Smartsheet to Jira Cloud.

## Folder Structure

- `jira_data_updates/`: Contains scripts related to updating data in Jira Cloud.

## Scripts

### `generate_update_payload.py`

This script is designed to assist in the migration and updating of data from Smartsheet to Jira Cloud. It performs the following tasks:

1. **Identifies Unique Columns**:
   - Compares the columns in the Smartsheet and Sharepoint files to identify columns that are unique to the Smartsheet.

2. **Adds Issue Key**:
   - Adds the "Issue Key" from the Jira Cloud export to the Smartsheet data, facilitating the correspondence between the tickets in Smartsheet and Jira Cloud.

3. **Generates Update Payloads**:
   - Creates two versions of the output file:
     - A comprehensive file containing all the data from Smartsheet, including the "Issue Key".
     - A simplified file containing only the foreign key, the "Issue Key", and the unique columns from Smartsheet.

4. **Logs Unmatched Records**:
   - Identifies and logs records in the Smartsheet that do not have a corresponding issue in Jira Cloud.

## Usage

### Prerequisites

- Python 3.x
- Pandas library

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/JiraCloudToolKit.git
   cd JiraCloudToolKit

2. Install the required dependencies: `pip install pandas`
3. 

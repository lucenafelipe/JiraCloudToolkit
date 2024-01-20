# JMWE Script: Custom Field Option Management

## Overview
This script, written for Jira Misc Workflow Extensions (JMWE) using Nunjucks templating language, is designed to efficiently manage options within a Jira custom field. Its primary function is to check the existence of a specified option in a given custom field and to add this option if it's not already present. This process significantly streamlines the dynamic management of custom field options in Jira Cloud environments.

## Functionality
- **Check Existence**: The script first verifies if the intended option, in this case, `"brown"`, already exists in the specified custom field.
- **Add Option**: If the option does not exist, the script will automatically add it to the custom field.

## Implementation Details
- **Custom Field and Context IDs**: The script is set up to work with a specific custom field (`customfield_id`) and context (`context_id`).
- **Target Option Value**: The option value intended to be checked and possibly added is defined as `"brown"`.
- **Jira API Integration**: The script constructs a URL to interact with the Jira API, fetching existing options and adding new ones as required.
- **Iteration and Verification**: It iterates through the pages of existing options, ensuring the option does not exist before adding it.
- **Efficient Execution**: The script is optimized to handle multiple pages of options, halting the process as soon as the target option is found or after checking all available options.

## Usage
This script is particularly useful in scenarios where custom field options need to be dynamically managed based on project requirements, ensuring that required options are always available for selection in Jira issues.

## Author
Felipe Lucena

### Version
1.0

---

> Note: The execution of this script is subject to the permissions and constraints of the Jira Cloud environment where it is deployed.

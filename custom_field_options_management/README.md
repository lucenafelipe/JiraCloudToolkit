# JMWE Script: Custom Field Option Management

## Overview
This script, written for Jira Misc Workflow Extensions (JMWE) using Nunjucks templating language, efficiently manages options within a Jira custom field. It checks the existence of specified options in a given custom field and adds them if they are not already present, streamlining the dynamic management of custom field options in Jira Cloud environments.

## Functionality
- **Version 1.0**: Initially, the script verified the existence of a single specified option, `"brown"`, and added it if not present.
- **Version 1.1 (Updated)**: Enhanced to handle multiple values. The script now splits a string of values, such as `"Green, Yellow, Red"`, into an array and processes each value individually, checking for its existence and adding it if necessary.

## Implementation Details
- **Custom Field and Context IDs**: Set up for specific custom fields (`customfield_id`) and contexts (`context_id`).
- **Target Option Values**: Version 1.1 supports multiple values, enabling broader customization and dynamic updating.
- **Jira API Integration**: Uses the Jira API to fetch existing options and add new ones.
- **Efficient Iteration and Verification**: Iterates through options, ensuring non-existent ones are added. Optimized to handle multiple pages of options.
- **Flexible Usage**: Ideal for scenarios requiring dynamic management of custom field options in Jira issues.

## Usage
Useful in scenarios where custom field options need dynamic updating based on project requirements, ensuring all necessary options are available for selection in Jira issues.

## Changelog
- **1.0**: Initial release for single option management.
- **1.1**: Added support for managing multiple options.

## Author
Felipe Lucena

---

> Note: The script's execution is subject to the permissions and constraints of the Jira Cloud environment where it's deployed.

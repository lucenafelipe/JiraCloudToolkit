# JMWE Script: Custom Field Option Management

## Overview
This script, designed for Jira Misc Workflow Extensions (JMWE) and written in Nunjucks templating language, automates the management of options within a Jira custom field. It verifies the existence of specified options and dynamically adds them if missing. This feature is particularly valuable for maintaining updated and organized selection fields, enhancing the flexibility of Jira Cloud environments.

## Practical Use Case
In client projects where a "Customer" field needs to be dynamically updated with each new customer added as an option, this script serves as a scalable solution. Instead of manually updating fields, the script enables automated updates based on project changes. For example, in a Jira project set up as a "Database," each new issue represents a client, and their information is added automatically to the "Customer" selection field. This approach enables advanced automations, like tracking each customer's specific contract details (e.g., plan type such as Standard, Premium), ensuring all relevant data is easily accessible and up-to-date.

## Functionality
- **Version 1.0**: Initially supported single-value management by adding an option if missing (e.g., adding `"brown"`).
- **Version 1.1 (Updated)**: Expanded to handle multiple values, processing strings like `"Green, Yellow, Red"` by splitting them into individual options, checking for each option's existence, and adding any that are missing.

## Implementation Details
- **Custom Field and Context IDs**: The script is pre-configured with specific `customfield_id` and `context_id` for targeted custom fields.
- **Target Option Values**: Version 1.1 enables management of multiple options, streamlining workflows where multiple selections are required.
- **Jira API Integration**: Accesses Jira's API to retrieve current options and add new entries dynamically.
- **Efficient Iteration and Verification**: Optimized to handle multiple pages of options, ensuring seamless management of extensive option lists.
- **Ideal Use Cases**: Perfect for dynamically updating custom field options based on evolving project requirements.

## Usage
This script is useful in scenarios where custom field options need continuous updating, such as in CRM-style projects in Jira, where new clients or contracts need to be easily accessible in selection fields without manual field updates. By keeping these fields current, you can create powerful automations and streamline workflows for better data management.

## Changelog
- **1.0**: Initial release for single option management.
- **1.1**: Expanded support to handle multiple options dynamically.

## Author
Felipe Lucena

---

> Note: This script relies on Jira Cloud environment permissions and constraints for successful execution.

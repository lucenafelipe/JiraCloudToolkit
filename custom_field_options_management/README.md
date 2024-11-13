# JMWE Script: Custom Field Option Management

## Overview
This script, designed for Jira Misc Workflow Extensions (JMWE) and written in Nunjucks templating language, automates the management of options within a Jira custom field. It verifies the existence of specified options and dynamically adds them if missing, ensuring that selection fields are always current and relevant. This feature is valuable for enhancing data organization and automation capabilities in Jira Cloud environments.

## Practical Use Case
In client projects where a "Customer" field must be updated dynamically, this script enables scalable field management. Each new issue representing a client is automatically added to the "Customer" selection field, allowing for advanced automations. For example, it becomes easy to track contract-specific details, such as plan type (Standard, Premium), ensuring data accuracy and availability for automation triggers.

## Functionality
- **Version 1.0**: Introduced support for single-value management, allowing the addition of a single option if it did not already exist (e.g., adding `"brown"`).
- **Version 1.1 (Updated)**: Enhanced to support multiple values. The script now splits strings like `"Green, Yellow, Red"` into individual options, verifying each one’s existence and adding any missing entries.

## Implementation Details
- **Custom Field and Context IDs**: Configured with `customfield_id` and `context_id` to target specific fields and contexts.
- **Target Option Values**: Supports multiple values in a single execution, improving flexibility for dynamic data management.
- **Jira API Integration**: Utilizes the Jira API to check and modify field options based on current field contents.
- **Efficient Iteration and Verification**: Handles multiple pages of options to ensure all options are checked and added without duplicates.
- **Ideal Use Cases**: Well-suited for projects requiring dynamic field management, like CRM setups where new clients or contracts are regularly added and need to appear in selection lists.

## Usage
This script is ideal for scenarios where custom field options require frequent updates, such as in CRM-like configurations in Jira. By maintaining these fields dynamically, teams can implement automated processes that rely on accurate, up-to-date data, improving efficiency and reducing manual intervention.

## Changelog
- **1.0**: Initial release for single option management.
- **1.1**: Expanded functionality to handle multiple options dynamically, with improved iteration for robust data management.

## Author
Felipe Lucena

---

> Note: This script relies on Jira Cloud environment permissions and constraints for successful execution.

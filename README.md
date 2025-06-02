# VersionUpdater CLI Tool

## Introduction

`VersionUpdater.exe` is a command-line tool designed to update the **File Version** and **Product Version** numbers in `.rc` files within a GitHub repository. This utility streamlines the versioning process for projects by allowing quick and easy updates.

---

## Requirements

To run this tool, ensure the following prerequisites are installed and configured:

- **Git Bash**
- **Properly configured JSON files**

---

## How to Use

### Step 1: Launch the Tool

Double-click the `VersionUpdater.exe` file to open the application.

### Step 2: Choose an Option

You will be prompted with a menu:

- **Generate a sample JSON**  
  Enter `1` when prompted:  
  `Enter your choice: 1`

- **Proceed with version update (if JSON is already configured)**  
  Enter `2` when prompted:  
  `Enter your choice: 2`

### Step 3: Post-Update Cleanup (Optional)

After the update process is complete, you may delete the cloned repository from your local machine.

---

## Sample JSON Formats

### `git_config.json`

```json
{
  "repo_url": "https://github.com/harie/test.git/",
  "clone_path": "",
  "access_token": "g*******************BxBR3mVDVy",
  "branch_name": "automation_test"
}

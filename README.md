# log_sort

Script to identify the most common string or entry in each column of a CSV.

## Project Plan and Scope Document
**Project Title**: Security Log Analysis Tool Development

---

### 1. Introduction

#### 1.1 Background
In today's digital landscape, organizations generate vast amounts of security logs that record various activities within their systems. Analyzing these logs is crucial for identifying potential security threats, understanding user behavior, and ensuring compliance with regulatory standards. Efficient log analysis can help in proactive threat detection and remediation.

#### 1.2 Purpose of the Project
The purpose of this project is to develop a Python-based tool that reads security log data from a CSV file, performs essential analysis, and outputs key insights. The tool will identify the most common entries in specified columns, count the total number of log entries, and extract log entries that start with a specific pattern.

---

### 2. Project Objectives
- Develop a script to read and parse security log data from a CSV file using Python.
- Identify and report the most common entries in specified columns (e.g., IP_Address, Username, Status).
- Count and report the total number of log entries in the dataset.
- Extract and display log entries that start with a specific character or string.
- Ensure error handling for scenarios such as missing files or columns.

---

### 3. Scope

#### 3.1 In-Scope
- Reading and processing CSV files containing security logs.
- Parsing specific columns for analysis.
- Computing and displaying the most common entries in the specified columns.
- Counting the total number of log entries.
- Extracting and displaying log entries that start with a specific pattern.
- Basic exception handling (e.g., file not found, missing columns).

#### 3.2 Out-of-Scope
- Advanced data visualization (e.g., charts, graphs).
- Real-time log monitoring or streaming data processing.
- Development of a graphical user interface (GUI).
- Integration with databases or external systems.
- Advanced error handling and logging mechanisms beyond basic exceptions.

---

### 4. Deliverables
- **Python Script**: A fully functional Python script (`log_analysis.py`) that performs the specified analyses.
- **User Documentation**: Instructions on how to set up and run the script, including any dependencies.
- **Project Documentation**: This project plan and scope document detailing the project's objectives and scope.
- **Test Cases**: A set of test cases used to validate the script's functionality.

---

### 5. Project Plan

#### 5.1 Tasks

1. **Requirements Analysis**
   - Confirm the structure of the CSV file and the columns available.
   - Identify any specific patterns to search for in the log entries.

2. **Environment Setup**
   - Install necessary Python packages (e.g., `pandas`).
   - Set up the development environment.

3. **Script Development**
   - Develop functionality to read and validate the CSV file.
   - Implement the function to find the most common entries in specified columns.
   - Add logic to count the total number of log entries.
   - Implement the search for log entries starting with a specific pattern.
   - Incorporate exception handling for missing files or columns.

4. **Testing and Validation**
   - Create test cases covering various scenarios (e.g., missing columns, empty files).
   - Validate the script against sample CSV files.

5. **Documentation**
   - Prepare user documentation with setup instructions.
   - Update the project plan and scope document as needed.

6. **Final Review**
   - Review the script and documentation for completeness.
   - Make any necessary revisions based on self-assessment.

#### 5.2 Timeline
This project is designed to be completed in a short time frame, suitable for same-day completion. The tasks outlined can be approached sequentially or in parallel as needed.

---

### Usage

To run the script:
```bash
python log_analysis.py <path_to_csv_file>

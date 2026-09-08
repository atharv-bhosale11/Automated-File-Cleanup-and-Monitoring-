# Automated File Cleanup and Monitoring

A Python-based automation tool designed to monitor a directory, identify and remove empty files, handle file-system exceptions, and generate timestamped execution logs with a detailed execution summary.

## 📌 Overview

**Automated File Cleanup and Monitoring** automates routine directory-cleanup tasks using Python.

The application scans a specified directory and its subdirectories, identifies empty files, removes them automatically, and records every operation in a timestamped log file.

It also provides exception handling and an execution summary containing statistics about the scanning and cleanup process.

## 🚀 Features

* 🔍 **Recursive Directory Scanning**

  * Scans the specified directory and all its subdirectories using `os.walk()`.

* 🧹 **Automatic Empty File Detection**

  * Identifies files with zero bytes.

* 🗑️ **Automatic File Cleanup**

  * Removes detected empty files automatically.

* 📝 **Deleted File Tracking**

  * Records the complete path of every successfully deleted file.

* ⏱️ **Timestamped Log Files**

  * Generates a unique log file for every execution.
  * Example:

    ```text
    FileLog_2026-09-08_20-30-15.log
    ```

* ⚠️ **Exception Handling**

  * Handles permission-related and operating-system file errors without terminating the entire scanning process.

* 📊 **Execution Summary**

  * Reports:

    * Directory scanned
    * Total files scanned
    * Empty files found
    * Files successfully deleted
    * Failed operations
    * Total execution time

* 🔄 **Scheduled Monitoring**

  * Uses the Python `schedule` library to automatically execute the cleanup process at a fixed interval.

## 🛠️ Technologies Used

| Technology             | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| **Python**             | Core programming language                           |
| **os**                 | File-system and directory operations                |
| **sys**                | Command-line argument handling                      |
| **time**               | Timestamp generation and execution-time measurement |
| **schedule**           | Periodic task scheduling                            |
| **Exception Handling** | Robust file-operation error management              |

## 📂 Project Structure

```text
Automated-File-Cleanup-and-Monitoring/
│
├── DirectoryHealthMonitor.py
├── README.md
├── LICENSE
└── FileLog_YYYY-MM-DD_HH-MM-SS.log
```

> Log files are generated automatically when the application runs.

## ⚙️ Requirements

* Python 3.x
* `schedule` Python package

Install the required dependency:

```bash
pip install schedule
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/Automated-File-Cleanup-and-Monitoring.git
```

Navigate to the project directory:

```bash
cd Automated-File-Cleanup-and-Monitoring
```

Run the application by providing the directory to monitor:

```bash
python DirectoryHealthMonitor.py Data
```

Replace `Data` with the directory you want to monitor.

## 💻 Example Execution

```text
----------------------------------------------------
---------------Atharv Automation Suite--------------
----------------------------------------------------
Directory to Scan: Data

Empty Files Deleted: 3

Log File Created: FileLog_2026-09-08_20-30-15.log
```

The application continues monitoring the directory according to the configured schedule.

Press:

```text
Ctrl + C
```

to stop the continuously running monitoring process.

## 📝 Sample Log

A generated log file contains information similar to:

```text
----------------------------------------------------
This is a log file created by Marvellous Automation
This is Directory Cleaner Script
----------------------------------------------------

Deleted File: Data\test.txt
Deleted File: Data\demo.txt
Deleted File: Data\empty.txt

----------------------------------------------------
EXECUTION SUMMARY
----------------------------------------------------
Directory Scanned       : Data
Total Files Scanned     : 10
Empty Files Found       : 3
Files Deleted           : 3
Files Failed            : 0
Execution Time          : 0.01 seconds
Status                  : Completed
----------------------------------------------------
```

## 🔐 Exception Handling

The application handles common file-system errors such as:

### PermissionError

Occurs when the application does not have sufficient permission to access or delete a file.

The error is recorded in the log:

```text
Permission Denied: Data\protected.txt
```

### OSError

Handles other operating-system-level file errors during file processing.

Example:

```text
Error: [Errno ...] ...
```

The application continues processing other files instead of terminating the complete scan.

## 📊 Execution Summary

Every execution generates a summary containing key metrics:

```text
Directory Scanned       : Data
Total Files Scanned     : 25
Empty Files Found       : 5
Files Deleted           : 4
Files Failed            : 1
Execution Time          : 0.03 seconds
Status                  : Completed
```

This provides a quick overview of the directory's health and the actions performed by the automation system.

## 🔄 Automation Workflow

```text
             Start
               │
               ▼
      Receive Directory
               │
               ▼
       Validate Directory
               │
               ▼
       Scan Files Recursively
               │
               ▼
        Check File Size
               │
          ┌────┴────┐
          │         │
       Empty      Non-Empty
          │         │
          ▼         ▼
       Delete      Skip
          │
          ▼
    Record File Name
          │
          ▼
    Handle Exceptions
          │
          ▼
   Generate Execution
       Summary
          │
          ▼
   Create Timestamped
        Log File
          │
          ▼
    Scheduled Re-run
```

## 🎯 Project Objectives

This project was developed to demonstrate practical implementation of:

* Python automation
* File-system programming
* Recursive directory traversal
* File management
* Scheduled task execution
* Exception handling
* Logging and monitoring
* Command-line argument processing
* Execution-time measurement
* Automation workflow design

## 🔮 Future Enhancements

Planned improvements include:

* [ ] Configurable monitoring interval
* [ ] Dedicated `Logs/` directory
* [ ] Configurable file-cleanup rules
* [ ] Support for files based on age
* [ ] Disk-space monitoring
* [ ] Email notifications
* [ ] Desktop/system notifications
* [ ] Configurable logging levels
* [ ] JSON-based configuration
* [ ] Unit testing
* [ ] Improved command-line interface
* [ ] Dashboard for monitoring directory health

## 📈 Skills Demonstrated

**Programming:**
Python

**Core Concepts:**
File Handling · Exception Handling · Loops · Conditional Statements · Functions · Command-Line Arguments

**Automation:**
Scheduled Execution · Directory Monitoring · Automated Cleanup

**File-System Operations:**
Directory Traversal · File Detection · File Deletion · File Metadata

**Monitoring & Logging:**
Timestamped Logs · Execution Metrics · Error Logging · Execution Summary

## 👨‍💻 Author

**Atharv Tushar Bhosale**

GitHub: [Atharv Bhosale](https://github.com/atharv-bhosale11)

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

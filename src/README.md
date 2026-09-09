# Source Code

This directory contains the core Python implementation of the **Automated File Cleanup and Monitoring** system.

## filecleanup.py

`filecleanup.py` is the main application responsible for monitoring a specified directory, identifying empty files, removing them automatically, and generating detailed execution logs.

### Responsibilities

* Validate the provided directory path.
* Recursively scan directories and subdirectories.
* Identify empty files.
* Remove empty files automatically.
* Track scanned, detected, deleted, and failed files.
* Handle file-system related exceptions.
* Generate timestamped log files.
* Record deleted file paths and processing errors.
* Generate an execution summary.
* Continuously monitor the directory using scheduled execution.

## Core Modules

| Module     | Purpose                                                                     |
| ---------- | --------------------------------------------------------------------------- |
| `os`       | Directory traversal, file validation, file-size checking, and file deletion |
| `sys`      | Command-line argument handling                                              |
| `time`     | Timestamp generation, execution-time measurement, and scheduling delay      |
| `schedule` | Periodic execution of the directory monitoring task                         |

## Execution Flow

```text
Command-Line Argument
        ↓
Directory Validation
        ↓
Recursive Directory Scan
        ↓
File Detection
        ↓
Empty File Identification
        ↓
File Deletion
        ↓
Exception Handling
        ↓
Execution Summary
        ↓
Timestamped Log Generation
        ↓
Scheduled Monitoring
```

## Key Implementation Concepts

### 1. Recursive Directory Traversal

The application uses `os.walk()` to recursively traverse the target directory and its subdirectories.

```python
for FolderName, SubFolder, FileName in os.walk(DirName):
```

### 2. Empty File Detection

A file is identified as empty when its size is `0` bytes.

```python
if os.path.getsize(fname) == 0:
```

### 3. Automated File Deletion

Detected empty files are removed using Python's `os.remove()` function.

```python
os.remove(fname)
```

### 4. Exception Handling

The application handles common file-system errors, including:

* `PermissionError`
* `OSError`

This ensures that an error while processing an individual file does not unnecessarily terminate the monitoring process.

### 5. Execution Metrics

The application maintains execution statistics including:

* Total files scanned
* Empty files found
* Files successfully deleted
* Files that failed to process
* Total execution time

### 6. Timestamped Logging

Each execution generates a uniquely timestamped log file.

Example:

```text
FileLog_2026-09-09_11-30-45.log
```

The log records:

* Deleted file paths
* Permission errors
* File-system errors
* Directory scanned
* Execution statistics
* Total execution time
* Completion status

## Scheduled Monitoring

The application uses the `schedule` library to execute the directory monitoring process periodically.

```python
schedule.every(1).minutes.do(DirectoryScanner, DirectoryName)
```

The monitoring process continuously runs until manually stopped using:

```text
Ctrl + C
```

## Command-Line Usage

Run the application by providing the directory path as a command-line argument:

```bash
python filecleanup.py <directory_path>
```

Example:

```bash
python filecleanup.py D:\TestDirectory
```

## Source Code Design

The implementation demonstrates practical application of:

* Python File-System Automation
* Recursive Directory Traversal
* Command-Line Argument Processing
* Exception Handling
* Timestamped Logging
* Execution-Time Measurement
* Scheduled Task Automation
* File Management
* Python Standard Library

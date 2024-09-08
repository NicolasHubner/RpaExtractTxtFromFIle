# Text File Data Extractor

## Overview

This project extracts structured data from `.txt` files within a specified directory, processes the data to replace commas with dashes to avoid issues with CSV formatting, and writes the cleaned data into a single CSV file.

## Features

- Reads all `.txt` files from a specified directory.
- Extracts structured data based on a predefined format.
- Replaces commas with dashes to prevent conflicts with CSV parsing in Excel.
- Excludes the first 9 and the last 2 rows from each file.
- Writes the processed data into a single CSV file.

## Requirements

- Python 3.x
- `re` (Regular Expressions)
- `csv`
- `os`
- `glob`

## Usage

1. **Prepare Your Environment:**
   - Ensure Python 3.x is installed on your machine.

2. **Place Your `.txt` Files:**
   - Put all `.txt` files in a directory of your choice.

3. **Configure the Script:**
   - Open `extract_from_directory.py`.
   - Replace `'your_directory_here'` with the path to your directory containing `.txt` files.
   - Adjust `output_file_path` if necessary.

4. **Run the Script:**
   - Execute the script from the command line:

     ```bash
     python extract_from_directory.py
     ```

5. **Check the Output:**
   - The script will generate a file named `output.csv` in the same directory as the script, containing the cleaned and combined data.

## Example

Given `.txt` files in the directory, the script processes each file, replaces commas with dashes, excludes the first 9 and last 2 rows, and saves the results into `output.csv`.


## Contact

For any questions or feedback, please contact [Nicolas](mailto:hubnersantos15@gmail.com).

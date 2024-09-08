import re
import csv
import os
import glob

# Function to replace commas with dashes
def replace_commas_with_dashes(text):
    return text.replace(',', '-')

# Function to extract data from each file and write to CSV
def extract_and_write_to_csv(input_dir, output_file):
    # Prepare a list to hold all matches from all files
    all_matches = []

    # Find all .txt files in the input directory
    txt_files = glob.glob(os.path.join(input_dir, '*.txt'))

    # Regular expression to capture the relevant information
    pattern = re.compile(r'''
        (.*)                            # Name of the entity (Group 1)
        \n(.*)                          # Address (Group 2)
        \n(.*)                          # City (Group 3)
        \n(\d{5}-\d{3})                 # Postal Code (CEP) (Group 4)
        \n([A-Z]{2})                    # State (Group 5)
        \n(\d{8}/\d{4}-\d{2})           # CGC (Group 6)
    ''', re.VERBOSE)

    # Process each file
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as file:
            data = file.read()

        # Find all matches in the current file
        matches = pattern.findall(data)

        # Exclude the first 9 and the last 2 rows
        filtered_matches = matches[9:-2]
        
        # Replace commas with dashes in each field of the matches
        processed_matches = [
            tuple(replace_commas_with_dashes(field) for field in match)
            for match in filtered_matches
        ]
        
        all_matches.extend(processed_matches)

    # Write the extracted data from all files to a CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(["Name", "Address", "City", "Postal Code (CEP)", "State", "CGC"])

        # Writing all filtered rows from all files
        for match in all_matches:
            writer.writerow(match)

    print(f"CSV file '{output_file}' has been created successfully.")

# Specify the directory containing the .txt files and the output CSV file path
input_directory = './textos'  # Replace with your directory path containing .txt files
output_file_path = 'output.csv'  # Specify the output CSV file path

# Run the function
extract_and_write_to_csv(input_directory, output_file_path)

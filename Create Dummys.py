import pandas as pd


# Function to replace values in specific columns with unique dummy data
def replace_with_unique_dummy_data(file_path, output_path):
    # Read the CSV file
    df = pd.read_csv(file_path, delimiter=';')

    # Generate unique dummy emails and notes for each row
    df['User Email'] = df.index.map(lambda x: f'dummy{x}@email.com')
    df['Note to Recipient'] = df.index.map(lambda x: f'dummy_note_{x}')

    # Save the modified DataFrame back to a new CSV file
    df.to_csv(output_path, sep=';', index=False)


# File paths
input_file_path = 'original_file.csv'  # Replace with your actual input file path
output_file_path = 'dummy_file.csv'  # Replace with your desired output file path

# Run the function
replace_with_unique_dummy_data(input_file_path, output_file_path)

import csv
import sys

def check_argv():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")

def main():
    check_argv()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Try and exit if first file couldn't be opened
    try:
        # Open the input file for reading
        with open(input_file, 'r') as csv_input:
            # Create an iterable object with dictionaries using the first row of the CSV as the keys
            reader = csv.DictReader(csv_input)

            # Create a list to hold the dictionaries within the DictReader object data
            transformed_data = []

            # Process each dictionary in the iterable object and append it to the new list
            for row in reader:
                # Split the name into first name and last name (they're reversed in the original file)
                last_name, first_name = row['name'].split(', ')

                # Create a new row with the transformed data and append it to the list of dicts/rows
                transformed_row = {'first': first_name, 'last': last_name, 'house': row['house']}
                transformed_data.append(transformed_row)

        # Open the new output file for writing
        with open(output_file, 'w') as csv_output:
            # Define the fieldnames for the output file
            fieldnames = ['first', 'last', 'house']

            # Create a CSV writer object
            writer = csv.DictWriter(csv_output, fieldnames=fieldnames)

            # Write the fieldnames as the header row
            writer.writeheader()

            # Write the transformed data rows using the passed fieldnames as keys
            for row in transformed_data:
                writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == '__main__':
    main()
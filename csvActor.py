# Import csv module
import csv

# Read csv file
with open('past_nominations.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterates through each line of the csv file that was read
        for line in csv_reader:
            print(line[1]) # Prints the category of award
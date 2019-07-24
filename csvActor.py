# Import csv module
import csv

# Read csv file
with open('past_nominations.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        print(csv_reader)
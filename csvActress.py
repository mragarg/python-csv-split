# Import csv module
import csv

# Read csv file
with open('past_nominations.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Loops over the first line that contains col names
        # next(csv_reader)

        # Write new file
        with open('actress_table.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file)

            # Iterates through each line of the csv file that was read
            for line in csv_reader:
                if line[1] == 'Award' or line[1] == 'ACTRESS IN A LEADING ROLE' or line[1] == 'ACTRESS IN A SUPPORTING ROLE':
                    csv_writer.writerow(line)
                # print(line[1]) # Prints the Award name
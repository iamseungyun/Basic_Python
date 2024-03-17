import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_file) skip first line
    #for line in csv_reader:
       #print(line)

    with open('new_names.csv', 'w') as new_files:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)

    
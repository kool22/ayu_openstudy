from __future__ import print_function
# Text file
# CSV
# Excel file to CSV
# Read CSV file

import csv

with open('sample_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print('|'.join(row))

with open('sample_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row['Name'], row['Relation'])

with open('sample_export.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('sample_export2.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

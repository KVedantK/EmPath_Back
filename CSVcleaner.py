import csv
with open('ManhattanNew.csv', 'r') as in_file:
    with open('CleanManhattanNew.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)

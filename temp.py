import csv
fields=['Commit Number', 'Commit message', 'Datetime']
with open('log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
def log_format_check(log_file_path):
    with open(log_file_path, 'r') as log_file:
        csv_reader = csv.reader(log_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
    
log_format_check('log.csv')
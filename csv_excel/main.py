import csv

def print_csv_as_list():
    file = open('./res/my_csv_list.csv', 'rU')
    try:
        reader = csv.reader(file)
        print('Printing file as list: ')
        print(list(reader))
    finally:
        fh.close()


def print_csv_as_dict():
    file = open('./res/my_csv_list.csv', 'rU')
    try:
        reader = csv.DictReader(file)
        print('Printing file as dictionary: ')
        print(reader.fieldnames)
        for row in reader:
            print(row['first_name'], row['last_name'], row['email'])
    finally:
        file.close()

print_csv_as_dict()
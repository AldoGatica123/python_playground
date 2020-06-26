import csv


def read_csv_as_list():
    file_handler = open('res/my_email_list.csv', 'rU')
    try:
        reader = csv.reader(file_handler)
        print('Printing file as list: ')
        print(list(reader))
    finally:
        file_handler.close()


def read_csv_as_dict():
    file_handler = open('res/my_email_list.csv', 'rU')
    try:
        reader = csv.DictReader(file_handler)
        print('Printing file as dictionary: ')
        print(reader.fieldnames)
        for row in reader:
            print(row['first_name'], row['last_name'], row['email'])
    finally:
        file_handler.close()


def write_csv_from_list():
    names = ['John', 'Eve', 'Fate', 'Jadon']
    grades = ['C', 'A+', 'A', 'B-']
    file_handler = open('res/my_grades_list.csv', 'wt')
    try:
        writer = csv.writer(file_handler, delimiter=',', lineterminator='\n')
        writer.writerow(('Sr.', 'Names', 'Grades'))
        for i in range(4):
            writer.writerow((i+1, names[i], grades[i]))
    finally:
        file_handler.close()


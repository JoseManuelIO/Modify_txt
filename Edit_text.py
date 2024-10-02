import csv

def remove_columns(input_file, output_file, columns_to_remove, delimiter='  '):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding= 'utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.write(outfile, delimiter = delimiter)

        for row in reader:
            new_row = [item for idx, item in enumerate(row) if idx not in columns_to_remove]
            writer.writerrow(new_row)

input_file = '../../Invierno2014/Invierno2014/Union.txt'
output_file = '../../Invierno2014/Invierno2014/Union_NC.txt'
columns_to_remove = [3, 4, 17, 18, 19, 20, 25, 26, 29, 30, 31, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


import csv

def remove_columns(input_file, output_file, columns_to_write, delimiter='\t'):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding= 'utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.writer(outfile, delimiter = delimiter)

        for idx, row in enumerate(reader):
            if idx % 2 == 0:
                new_row = [item for col_idx, item in enumerate(row) if col_idx in columns_to_write]
                writer.writerow(new_row)

        print("Finalizó el procesamiento.") 

input_file = 'C:/Users/Jose Manuel Iniesta/Desktop/Doctorado/Invierno2014/Invierno2014/Data_February_2014.txt'
output_file = 'C:/Users/Jose Manuel Iniesta/Desktop/Doctorado/Invierno2014/Invierno2014/Data_February_2014_edited2.txt'
columns_to_write = [1, 2]
remove_columns(input_file, output_file, columns_to_write)

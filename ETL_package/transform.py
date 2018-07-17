import csv

from ETL_package.transformators import etl_interface


def transform(data: csv.DictReader) -> list:
    # create header: etl_interface keys have order as it is an OrderedDict
    output_matrix = [list(etl_interface.keys())]

    for row in data:
        has_errors = False
        output_row = []
        # etl_interface is an OrderedDict so "for" loop has an order too
        for column_name, transform_method in etl_interface.items():
            # remove whitespaces
            value = str(row[column_name]).strip(" ")
            # do not write row if it has an empty cell
            if value == "" or value == "-":
                has_errors = True
                break

            """
            There are no exceptions in the file, I used it for the debug 
            but it may prevent program crash in future with different files
            """
            try:
                output_row.append(transform_method(value))
            except Exception as e:
                print(e)
                has_errors = True
                break

        if not has_errors:
            output_matrix.append(output_row)

    return output_matrix


def write_csv_output(matrix: list, output_csv_path: str):
    if not output_csv_path.endswith(".csv"):
        print("Incorrect file name in file path %s" % output_csv_path)
        return

    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(matrix)


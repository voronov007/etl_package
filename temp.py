from ETL_package import transform, load
from ETL_package.transform import write_csv_output

data_file = load('Challenge_me.txt')
output = transform(data_file)
write_csv_output(output, "output.csv")

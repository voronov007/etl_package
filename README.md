# ETL (Extract Transform Load) package

Read txt file, transform and clean the data, load
to matrix(list of lists) and save to CSV file.

- Python 3.5

## Usage
1. Install and activate virtual environment: `virtualenv -p python3.5 venv`, 
`source venv/bin/activate`
2. Install package.

   - `pip install -e .` if you have downloaded the package project
   
   - `pip install <path_to_package>` if you have a `*.tar.gz` file

3. Copy input txt file in the project root or provide full path to the txt data file.
Below is an example for the file which lay in project root. In python module write:
```
from ETL_package import load, transform, write_csv_output

data = load("<imput_file_path>.txt")
transformed_data = transform(data)
# optional
write_csv_output(transformed_data, "<output_file_path>.csv")
```
`transformed_data` data is a list of lists.
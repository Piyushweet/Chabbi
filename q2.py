
'''Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.'''


def get_file_type(ext_type, lst):
    types = {}
    for ext_type in ext_type:
        ext, f_type = ext_type.split(',')
        types[ext] = f_type

    result = {}  # Dictionary to store file - name - type mapping
    for file_name in lst:
        if '.' in file_name:
            ext = file_name.split( '.' ) [ - 1 ]
            if ext in types:
                result[file_name] = types[ext]
            else:
                result[file_name] = 'unknown'
        else:
            result[file_name] = 'unknown'

    return result


ext_type = input("Enter extension and type values: ")
file_list = input("Enter the file names: ").split(",")

ext_type_list = ext_type.split(';')
file_types = get_file_type(ext_type_list, file_list)
print(file_types)

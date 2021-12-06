import os
import csv



# why newline="" ?
# https://stackoverflow.com/questions/16864683/empty-space-in-between-rows-after-using-writer-in-python



def read_csv_dict(filepath):
    dict_list = []
    with open(filepath, mode='r') as f:
        reader = csv.DictReader(f)
        for d in map(dict, reader):
            dict_list.append(d)
    return dict_list



def write_dict_csv(filepath, data_list, header_list):
    with open(filepath, mode='w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header_list)
        writer.writeheader()
        writer.writerows(data_list)
        print('\nthe data is successfully exported')




# get the directory of 'data' in 'py_02_intermediate' folder
HERE = os.path.dirname(os.path.abspath(__file__))
foldername = 'data'
DIR = os.path.join(HERE, foldername)



# get the filename to read
filename = 'test_read.csv'
filepath = os.path.join(DIR, filename)
data = read_csv_dict(filepath)
print('\ncsv is successfully loaded as \n{}'.format(data))



# file to save
header_list = ['info_a', 'info_b', 'info_c']
data_list = [
    {'info_a': 1, 'info_b': '1_2', 'info_c': '1_3'},
    {'info_a': 2, 'info_b': '2_2', 'info_c': '2_3'},
    {'info_a': 3, 'info_b': '3_2', 'info_c': '3_3'},
    {'info_a': 4, 'info_b': '4_2', 'info_c': '4_3'},
    {'info_a': 5, 'info_b': '5_2', 'info_c': '5_3'}
]

# get the filename to write
filename = 'test_write.csv'
filepath = os.path.join(DIR, filename)

# write_csv
write_dict_csv(filepath, data_list, header_list)

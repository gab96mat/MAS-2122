import os
import json


def read_json(filename):
    with open(filename, 'r') as f:
        output = json.load(f)
    return output

def write_json(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


# get the directory of 'data' in 'py_02_intermediate' folder
HERE = os.path.dirname(os.path.abspath(__file__))
foldername = 'data'
DIR = os.path.join(HERE, foldername)

# get the filename to read
filename = 'test_read.json'
filepath = os.path.join(DIR, filename)
print(filepath)

# read json
data = read_json(filepath)
print(data)

# edit dict
data['new'] = 'new'

# write json
filename = 'test_write.json'
filepath = os.path.join(DIR, filename)
write_json(filepath, data)

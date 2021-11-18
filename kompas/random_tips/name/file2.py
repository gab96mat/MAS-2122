'https://rosettacode.org/wiki/Special_variables#Python'

def print_special_var():
    names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
    print( '\n'.join(' '.join(names[i:i+8]) for i in range(0, len(names), 8)) )

def print_name_file2():
    print("The __name__ variable of 'file2.py' is ", __name__)

if __name__ == "__main__":
    print("\nYou are executing a 'file2.py' from 'file2.py'")
    print_name_file2()
    print_special_var()

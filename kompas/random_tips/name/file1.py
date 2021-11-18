def print_name_file1():
    print("The __name__ variable of 'file1.py' is ", __name__)


print("I want to run this only inside the file1.py !!!")


if __name__ == "__main__":
    print("\nYou are executing a 'file1.py' from 'file1.py'")
    print_name_file1()
    
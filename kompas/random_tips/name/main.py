import file1
import file2

def print_name_main():
    print("The __name__ variable of 'main.py' is ", __name__)

if __name__ == "__main__":
    print("\nYou are executing a 'file1.py' from 'main.py'")
    file1.print_name_file1()
    print("\nYou are executing a 'file2.py' from 'main.py'")
    file2.print_name_file2()
    print("\nYou are executing a 'main.py' from 'main.py'")
    print_name_main()

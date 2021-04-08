def main():

    while True:
        try:
            name_inp = input("Enter the name of an input file: ")
            input_file = open(name_inp, 'r', encoding="utf-8")
            try:
                first=int(input_file.readline())
            except ValueError:
                print("Error: file contents invalid.")
                continue
            input_file=input_file.read()
            is_number(input_file)
            count = lines_count(input_file)
            if first == count:
                sum_num(input_file)
            else:
                print("Error: End of file expected.")
                continue
        except FileNotFoundError:
             print("file not found")
             continue
        break

def sum_num(input_file):
    sum=0
    l = input_file.splitlines()
    for i in l:
        i = int(i)
        sum += i
    print("The sum is:  ", sum )


def is_number(input_file):
    for line in input_file:
        try:
            line.isdigit()
        except ValueError:
             print("Error: file contents invalid.")


def lines_count(input_file):
    count = input_file.count('\n')
    if not input_file.endswith('\n'):
        count += 1
        return count
main()

import  re   # regexp library for creating pattern

pattern = re.compile("([a-zA-Z-d_])")
file_dict = {}
final_dic = {}

def main():
    while True:
        try:
            name_inp = input("Enter the name of an input file: ")
            input_file = open(name_inp, 'r', encoding="utf-8")

        except FileNotFoundError:
             print("Oops... An error occurred - Try again")
             continue
        break
    index_data(input_file)

def index_data(input_file):
    count = 1
    for line in input_file:
        file_dict[count] = line.replace("\n", "")   #create dict
        count += 1
    for key, value in file_dict.items():
        if pattern.match(file_dict[key]):          #create dict using pattern
            if value not in final_dic:
                final_dic[value] = [key]
            else:
                final_dic[value].append(key)

    for elem in sorted(final_dic.items()):     #sorting dict
        print(elem[0],":", elem[1])

main()

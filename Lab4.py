symbol = ':'
sum = 0

while True:
    try:
        name_inp = input("Input file: ")
        name_out = input("Output file: ")
        input_file = open(name_inp, 'r')
        output_file = open(name_out, 'w')

    except FileNotFoundError:
         print("file not found")
         continue
    break





with open(name_inp) as input_file, open(name_out,'w') as output_file:
    for line in input_file.readlines():
        if symbol in line:     #skip lines without colons
            word = line.split(symbol, 1)[0]  #select words before colons
            ab = line.find(":")
            num = float(line[ab + 1:])   #select only numbers
            sum += num                   #count sum
            sum = round(sum,2)
            word = line.split(symbol, 1)[0]
            print('   '+"%s%s"   %(word.ljust(30), num), file=output_file) #write to outpyut file
    print("   Total:                       ",sum, file=output_file)
output_file.close()
input_file.close()

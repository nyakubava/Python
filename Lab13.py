import string

NUM_RUNS = 6

dict = {}

def main():
    for index in range(0,NUM_RUNS):
        translate()

def translate():
    val = input("Enter a message to be translated:\n")
    input_file = open("testabbrev.txt", 'r', encoding="utf-8")
    phrase = "The translated text is:"
    for line in input_file:
        word, abv = line.split(":")   #create dict
        dict[word] = abv.replace("\n", "")
    if val in dict:  #check if inputed word in dictionary
        print(phrase)
        print(dict[val])
    # check if punctuation mark
    elif any(char in string.punctuation for char in val):
        print(phrase)
        print(dict[val[:-1]]+val[-1:])
    else:
        print(phrase)   # if word is not an abbreviation
        print(val)
main()

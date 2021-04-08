from datetime import date
today = date.today()
print("Today is:", today)  
#date
lastname  = input("Input your last name: ")
while len(lastname)<2 or len(lastname)>15:
    print("Last name should be more than\
 2 characters and less than 15")
    lastname = input("Input your last name: ")
number = input("Input your student number: ", )
print (number.isdigit())

sum = 0
for num in number:
    sum += int(num)
my_id = sum
num_let = len(lastname)
print("my id is:", int(my_id))
print("my num_let is:", num_let)

exp1 = (my_id/2)            #arithmetic
exp1 = round(exp1, 2)
exp2 = my_id%2
count = 0
if num_let == 2:
    exp3 = num_let + 2
else:
    for i in range(2, num_let):
        count += i
    exp3 = num_let + count
exp4 = my_id + num_let
exp5 = abs(num_let -  my_id)
exp6 = float((my_id) / (num_let + 1100))
exp6 = round(exp6, 2)
exp7 = (num_let % num_let) and (my_id * my_id)
exp8 = 1 or (my_id / 0)
exp9 = round(3.15, 2)

print("expression 1:", exp1)
print("expression 2:", exp2)
print("expression 3:", exp3)
print("expression 4:", exp4)
print("expression 5:", exp5)
print("expression 6:", exp6)
print("expression 7:", exp7)
print("expression 8:", exp8)
print("expression 9:", exp9)
#print("expression 9:", {:10.2f}'.format(exp9) #example formating

result = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9]
print("Results:" , result)

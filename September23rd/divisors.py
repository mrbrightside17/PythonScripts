#September23rd Python Script
#Write a script which can return all the divisors of an input number.

#recieve a number
num = int(raw_input("Please choose a number to divide: "))

#make a list of the numbers between 1 and the recieved number.
listRange = list(range(1,num+1))

#empty list will contain divisor results.
divisorList = []

#cycle thru the numbers range.
for number in listRange:
    #if the recieved number is exactly divided by one in the listRange
    if num % number == 0:
        #then the script appends it to the results
        divisorList.append(number)

#print the results
print divisorList

#complement the script in order to indicate if it the number is a prime number or not.

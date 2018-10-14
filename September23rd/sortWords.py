# write a script that can revert a string order
# it should output the string in a word only reverted order
# like this input = 'my name is fernando' output = 'fernando is name my'

#declare results container.
results=[]
#recieve input from user.
inputString = raw_input("give me a string to revert the word order:\n")
#fracture user's input into words.
Liston = inputString.split(" ")
#cycle and append list reverted.
for word in Liston[::-1]:
    results.append(word)
#convert list strings into one.
print ' '.join(results)

import re
text= "I like to try new things from the internet"
for word in text:
    #word=word.rstrip()
    #""Object Oriented Pattern where we take variable name.method/ library name.function""
    #The if statement here returns true or false
    if re.search('I',word):
        print(word)
    #The is the same function as the regural expression
    if word.find('I')>=0:
        print (word)



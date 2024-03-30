import re
text= "I like to try new things: I find in the internet"
for word in text:
    #word=word.rstrip()
    #""Object Oriented Pattern where we take variable name.method/ library name.function""
    #The if statement here returns true or false
    #"Adding dot then * means followed by any number of words till word 'new' even if there is a space between them "
    x=re.search("^I.*new", text)
    print(x)
    #The is the same function as the regural expression
    #if word.find('I')>=0:
     #   print (word)





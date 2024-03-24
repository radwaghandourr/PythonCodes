text = open('excel.csv', 'r')
f=open('output.csv' , 'w')
#total=dict()
str= ""
for x in text:
    #print (x)
    words=x.split(',')
    words.pop(1)
    #print(words)
    #wordstr=str(words)

    for y in words:
        y+=','
        str= str + y 
print(str)
#print(str.join(words))
f.write(str)
#print(words)
#total+=words
#print (total) 
   
f.close()
#print(words[0])







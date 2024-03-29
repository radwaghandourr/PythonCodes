text = open('excel.csv', 'r')
f=open('output.csv' , 'w')
#total=dict()
str= ""
final=""
for x in text:
    #print (x)
    words=x.split(',')
    words.pop(1)
    #print(words)
    #wordstr=str(words)

    for y in words:
    
        str= str + ',' + y 
        z=str.split(',')
        z.pop(0)
        for n in z:
            final=final+n
print(z)
#print(str.join(words))
f.write(final)
#print(words)
#total+=words
#print (total) 
   
f.close()
#print(words[0])







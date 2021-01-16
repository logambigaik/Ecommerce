import re
import os

def text_count(dir,filename,lower):
    source = os.path.join(dir,filename)
    no_of_char = 0
    no_of_lowcase = 0
    no_of_words = 0
    with open (source,'r') as file:
        data=file.read()
        no_of_words=len(data.split())
        #words= re.findall("(\S+)", data)
        words=data.split()
        for i in words:
            #print(i)
            no_of_char=no_of_char+len(i)
            if i.islower() and lower=='yes':
                no_of_lowcase = no_of_lowcase + 1

    print('No of words present in the file:',no_of_words)
    print("No of character present in the file:",no_of_char)
    if lower == 'yes':
        print("No of lowercase present in the file:",no_of_lowcase)

    return

def copyfile(source,dest):
    with open(source, 'r') as file:
        data = file.read()
        copy=open(dest,'w')
        copy.write(data)
        copy.close()

text_count('C:/Users/ganes/Ecommerce','test.txt','yes')
copyfile('test.txt','test1.txt')


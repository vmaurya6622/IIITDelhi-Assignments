
import re      #importing 'regular expressions' to delete the consecutive strings like comma or full stops.
import random   #importing Random library to generate a random number
from collections import Counter     #importing counter to count the number of words

file_location=r"E:\IIITD Projects\IP\Project assignment - 3\Three\scores.txt"

def score_of_assignment(file_name):
    with open(file_name, "r") as f:
        text = f.read()

    text = re.sub("\.+", ".", text)    #Removing consecutive full stops and convert to lower case
    text = text.lower()

    # Computing F1 factor
    unique_words = set(text.split())
    total_words = len(text.split())
    def f1():
        return len(unique_words) / total_words
    
    top_5_words = dict(Counter(text.split()).most_common(5))
    # print(top_5_words)

    # Computing F2 factor
    def f2():
        return sum(top_5_words.values()) / total_words

    # Computing F3 factor
    sentences = re.split("[\.\?!]", text)
    def f3():
        return sum(1 for sentence in sentences if len(sentence.split()) < 5 or len(sentence.split()) > 35) / len(sentences)

    # Computing F4 factor
    def f4():
        return sum(text.count(punctuation) for punctuation in [",", ".", ":", ";"]) / total_words

    # Computing F5 factor
    def f5():
        if total_words > 750:
            return 1
        else:
            return 0

    # Computing net score
    score = 4 + (f1() * 6 ) + (f2() * 6 )- f3() - f4() - f5()
    
    t=unique_words.copy()
    j=[]
    for i in t:
        c=i.replace(",","")
        d=c.replace(".","")
        e=d.replace(":","")
        f=e.replace(";","")
        g=f.replace("-","")
        j.append(g)
    random_words = random.sample(list(j),5) 
    # Writing results to file
    with open(file_location, "a") as f:
        f.write(" \n")
        f.write(file_name + "\n")
        f.write("Marks scored by the studet is : " + str(score) + "\n")
        f.write("Top most used words in the text are : " + ", ".join(top_5_words.keys()) + "\n")
        f.write("Five Random words are : " + ", ".join(random_words) + "\n")
        f.close()

number_of_files = 5 #int(input("Enter the number of files: "))
for i in range(number_of_files):
    file_name = "E:\IIITD Projects\IP\Project assignment - 3\Three\FILE" + str(i + 1) + ".txt"
    score_of_assignment(file_name)

print("All the tasks have been performed successfully! you can check the file",file_location)

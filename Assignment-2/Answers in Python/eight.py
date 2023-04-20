file_location="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\eight\pages.txt"
file=open(file_location)
dic={}
for i in range(16):
    k=file.readline().strip().split(',')
    dic[k[0]]=k[1:]
lst = [i for i in dic.keys()]
dictionary = {}
var = 0
for i in dic.values():
    k=i[0].split(":") 
    imp=k[0]   
    val=k[1]
    c=i[1:]
    l=[val]
    for i in c:
        l.append(i)
    t=set(l)
    x=[float(imp),t,len(t)]
    dictionary[lst[var]] = x 
    var += 1
# print(dictionary)

n=int(input("Enter the value of N :- "))
'''
Pages are ranked according to their overall importance. Let the total number of unique links in a page i be links[i] 
(i.e. these many unique pages this page refers to). The overall importance of a page i is sum over all the pages (j) 
which have a link to page i of: init_importance[j]/ links[j] (i.e. all the pages to which the page j has a link are
 distributed the importance of this page equally)

'''
counter=0
importance=[]
for i in dictionary.keys():
    x=[]
    for j in dictionary.values():
        k=j[1]
        if i in k:
            x.append(j[0]/j[2])
    importance.append(sum(x))  
    x.clear()  

score= importance.copy()
score.sort()
reverse_score=score[::-1]

lst=[i for i in dictionary.keys()]
for i in range(n):
    print(lst[importance.index(reverse_score[i])],": Rank :",i+1,"With Score of :",reverse_score[i])
    importance[importance.index(reverse_score[i])]='null'
    
file.close()

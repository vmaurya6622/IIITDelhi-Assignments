my_file=r"E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\seven\Bonus\me.json"
friend_file=r"E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\seven\Bonus\myfriend.json"
import json
file = open(my_file)
dicti = json.loads(file.read())
file.close()
# print(d)

a = open(friend_file)
dic = json.loads(a.read())
a.close()

mearge_file=r"E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\seven\Bonus\mearged.json"
k=dicti | dic

b=open(mearge_file,'w')
print("Your friend's and your's addressbook has been mearged successfully !")
json.dump(k, b,indent=4,separators=(',',': '))
b.close()

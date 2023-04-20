# i have made dictionary of 100 elements !
dic=['Abuse','Adult','Agent','Anger','Apple','Award','Loose','Basis','Beach','Birth','Block','Blood','Board','Brain','Bread','Break','Brown','Buyer','Cause','Chain','Chair','Chest','Chief','Child','China','Claim','Class','Clock','Coach','Coast','Court','Cover','Cream','Crime','Cross','Crowd','Crown','Cycle','Dance','Death','Depth','Doubt','Draft','Drama','Dream','Dress','Drink','Drive','Earth','Enemy','Entry','Error','Event','Faith','Fault','Field','Fight','Final','Floor','Focus','Force','Frame','Frank','Front','Fruit','Glass','Grant','Grass','Green','Group','Guide','Heart','Henry','Horse','Hotel','House','Image','Index','Input','Issue','Japan','Jones','Judge','Shirt','Shock','Sight','Simon','Skill','Sleep','Smile','Smith','Smoke','Imply','Issue','Judge','Laugh','Learn','Leave','Letus','Limit','Marry']
list=[]
for i in dic:
    k=i.lower()
    list.append(k)

import random
x=random.randint(0,100)
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=  Welcome! to the game of guessing 5-letter words  =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")

word=list[x]
counter=6     #chances given to the player
# print(word)


while True:
    print()
    print("you have",counter,"chances left play wisely, Good Luck !!")
    word_id=str(input("Hey! Enter your guess : "))
    import requests
    app_id  = "d6c2d722"
    app_key  = "eb5340d8e9fd099cc04610929e31c036"
    endpoint = "entries"
    language_code = "en-us"
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

    if r.status_code == 200:
        guess=word_id
    
        if len(guess) ==5:

            if guess == word:
                print()
                print("Congratulations! You have won the game ╰(*°▽°*)╯ ")
                print()
                break
            else:
                counter-=1
                r=[]
                for i in range(len(word)):
                    if word[i]==guess[i]:
                        r.append(guess[i])
                    else:
                        t='-'
                        r.append(t)
                for i in r:
                    print(i,end='')
                print()
                k=[]
                for i in guess:
                    for j in word:
                        if i==j:
                            k.append(i)
                        else:
                            continue
                g=[]
                for i in k:
                    if i not in g:
                        g.append(i)
                m=[]
                for i in g:
                    if i not in r:
                            m.append(i)

                c=''.join(m)        
                print("Other Characters Present : ",c)  
        else:
            print()
            print("Guess the correct word of five letter word only !")                  
                
    else:
        print("This word doesn't exist.")
        print("Error! Guess a word correctly in the dictionary only !") 
        print()
        # counter+=1
        # if counter<=0:
        #     counter=0
        # else:
        #     counter-=1 
    if counter == 0:
        print()
        print("Sorry! You lose the game ( ˘︹˘ ) ")
        print("The word was :",word)
        print("But, you can Retry! :^)")
        print()
        break
    

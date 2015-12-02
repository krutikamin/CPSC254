index = 0
temp = ""
containsY = None


def checkForY(string):
    global containsY
    global index
    i = len(string)
    
    while (i != 0):
        if(string[index] == "y"):
            return True
        else:
            index += 1
            i -= 1
        
    index = 0    
    return False
    
def consonent(word):
    global index
    global temp
    flag = 1
    
    while (flag == 1):
        if((word[index] == "a") or \
        (word[index] == "e") or \
        (word[index] == "i") or \
        (word[index] == "o") or \
        (word[index] == "u")):
            flag = 0
            break
        else:
            temp += word[index]
            index += 1
    print(word[index:] + temp + "ay")


word = input("Enter a word: ")


containsY = checkForY(word) #check if word contains "y"
if(containsY == True):
    if (word[0] == "y"):
        consonent(word)
    else:
        print(word + "way")
elif((word[0] == "a") or \
    (word[0] == "e") or \
    (word[0] == "i") or \
    (word[0] == "o") or \
    (word[0] == "u")):
    print(word + "way")     # add "way" to the word starting with vowel
elif((word[0] == "q") and (word[1] == "u")):
            print(word[2:] + word[0] + word[1] + "ay")
else:
    consonent(word)
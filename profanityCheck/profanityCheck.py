global data #global variable data
data = ["cat", "lama", "dog", "cow"] #list of profane words for comparison

def profanity(text):

    #we split the input text by a space
    newText = text.split(" ")

    #This will be either True of False depending on whether we find profance words (initialized with None)
    status = None
    
    #this array will hold the index number of the profance words, if we find any, present in the 'newText' list
    mark = []
    index = 0

    #get the index value of the profane words 
    for everyItem in newText:
        for everyText in data:
        #comparing if profance data words exits in 'newText' list
            status = everyText.upper() in everyItem.upper()
            #if True (We find the word)
            if status:
         	#flow control; makes sure that the length of current word is same as that of a profane word
                if len(everyText) == len(everyItem):
                    mark.append(index)
                #if length doen't matche by 1 character, the profane word might have colon, semicolon, commas, or period in the end.
                #it is marked if that is the case too
                elif (len(everyItem) == len(everyText)+1) and everyItem[-1] in ";,: ":
                    mark.append(index)
        index += 1
        
    #removing items specified by the index values that are stored in 'mark' array 
    for i in range(len(newText)-1,-1, -1):
        for j in mark:
            if i == j:
                del(newText[i])
     
    #itearte over the remaining items in the 'newText' array and print contents          
    for everyItem in newText:
        print(everyItem, "", end= "")

#function call
print("The profane words being checked are: {}".format(data))
_ = input("Enter sentence for profanity check: ")
if _:
	profanity(_)
else:
	print("Please provide an input for checking!")

#Yadav, Anil (Coppin State University)
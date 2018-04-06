def prc():
    
    print("Welocm to Rock, Paper, Scissors Game !")
    print()
    
    #getting player information 
    player_a_name = str(input("Player 1 name: "))
    
    #(note the user can put just the initials or the entire move)
    arg_a = str(input("Enter your move (Options: Rock, Paper, Scissors): "))
    
    player_b_name = str(input("Player 2 name: "))
    arg_b = str(input("Enter your move (Options: Rock, Paper, Scissors): "))
    print()

  #availabe array data for comparisons
    data = [("PR","Paper cuts rock"),("RS","Rock breaks scissors"),("SP","Scissors cut paper")]
  
  #initialze exception case first
    winner = False
  
  #loop through every data in our data array
    for everyData in data:
        
    #unpacking the tuple
        comparingData, message = everyData[0], everyData[1]

        #program flow control
        if comparingData[:1] == arg_a[0].upper() and comparingData[1:] == arg_b[0].upper():
          print("Winner name - {0}:\n{1}".format(player_a_name, message))
          winner = True #there is a winner

        elif comparingData[:1] == arg_b[0].upper() and comparingData[1:] == arg_a[0].upper():
          print("Winner name - {0}:\n{1}".format(player_b_name, message))
          winner = True #there is a winner
      
  #handles if no winner is found    
    if winner is not True:
        print("No one won :-)")
    
    
    
#function call
prc()

#Yadav, Anil (Coppin State University)
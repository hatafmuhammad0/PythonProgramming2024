
#! Write a program to read text from a file and check if it contain a word in it if yes then return that line? 

# def finder(li,word):
#     for i in li:
#         if word in i:
#             print(i)


# with open("poem.txt") as li:
#     x = li.readlines()
    

# finder(x,"good")

import random

#!Write a function which let user play a game and return a score as an integer , You need Socre.txt file which will be updated by this function


def game(scoreFile):
    player1Score = 0
    player2Score = 0
    game = 1


    while game <= 5:
        player1Num = random.randint(1,10)
        player2Num = random.randint(1,10)
        if player1Num > player2Num:
            player1Score += 1
            print(f'''
            Player 1 Num : {player1Num} 
            Player 2 Num : {player2Num}
            Player 1 Score : {player1Score}
            Player 2 Score : {player2Score}
            '''
            )
        else:
            player2Score += 1
            print(f'''
            Player 1 Num : {player1Num} 
            Player 2 Num : {player2Num}
            Player 1 Score : {player1Score}
            Player 2 Score : {player2Score}
            '''
            )
        f = open(scoreFile,"w")
        f.write(f"Player 1 Score is {player1Score} \n")
        f.write(f"Player 2 Score is {player2Score} ")
        f.close()
        game +=1
    
game("score.txt")




    










